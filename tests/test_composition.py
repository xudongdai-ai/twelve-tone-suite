import contextlib
import io
from pathlib import Path
import random
import tempfile
import unittest
import xml.etree.ElementTree as ET

from twelve_tone.composition.engine import AdvancedTwelveToneComposer
from twelve_tone.dependencies import music21
from twelve_tone.matrix import build_variants


@unittest.skipIf(music21 is None, 'music21 is optional; install .[score] for integration tests')
class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.composer = AdvancedTwelveToneComposer(output_dir=self.temporary.name)
        self.matrix = self.composer.generate_matrix(range(12))

    def test_six_techniques_score_and_xml_roundtrip(self):
        for style in self.composer.settings.composition_techniques:
            with self.subTest(style=style), contextlib.redirect_stdout(io.StringIO()):
                random.seed(42)
                score = self.composer.create_professional_score(
                    ['Flute', 'Piano'], self.matrix, 'Andante', 85, 4, style)
                self.assertEqual(len(score.parts), 3)
                for part in score.parts:
                    measures = list(part.getElementsByClass('Measure'))
                    self.assertEqual(len(measures), 4)
                    for measure in measures:
                        self.assertAlmostEqual(float(measure.duration.quarterLength), 4.0)
                filename = Path(self.composer.generate_sibelius_files(score))
                self.assertEqual(filename.parent, Path(self.temporary.name))
                document = ET.parse(filename).getroot()
                self.assertEqual(document.tag, 'score-partwise')
                self.assertEqual(len(document.findall('part')), 3)
                self.assertEqual(len(music21.converter.parse(filename).parts), 3)

    def test_gui_input_path_with_imported_matrix(self):
        inputs = (list(range(12)), ['Flute'], 'Andante', 85, 2,
                  'webern', True, build_variants(range(12)), 'lyrical')
        with contextlib.redirect_stdout(io.StringIO()):
            filename = self.composer.run_with_inputs(inputs)
        root = ET.parse(filename).getroot()
        self.assertEqual(len(root.find('part').findall('measure')), 2)

    def test_bad_import_fails_before_export(self):
        inputs = (list(range(12)), ['Flute'], 'Andante', 85, 2,
                  'webern', True, {'P': {0: list(range(12))}}, 'default')
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaisesRegex(ValueError, 'P1'):
            self.composer.run_with_inputs(inputs)
        self.assertEqual(list(Path(self.temporary.name).iterdir()), [])

    def test_invalid_composition_settings(self):
        for instruments, bpm, bars, style in (([], 85, 4, 'webern'),
                                             (['Flute'], 0, 4, 'webern'),
                                             (['Flute'], 85, 0, 'webern'),
                                             (['Flute'], 85, 4, 'unknown')):
            with self.subTest(settings=(instruments, bpm, bars, style)):
                with self.assertRaises(ValueError):
                    self.composer.create_professional_score(
                        instruments, self.matrix, 'Andante', bpm, bars, style)

    def test_distinct_export_names(self):
        with contextlib.redirect_stdout(io.StringIO()):
            score = self.composer.create_professional_score(
                ['Flute'], self.matrix, 'Andante', 85, 1)
            first = self.composer.generate_sibelius_files(score)
            second = self.composer.generate_sibelius_files(score)
        self.assertNotEqual(first, second)
        self.assertTrue(Path(first).is_file())
        self.assertTrue(Path(second).is_file())

    def test_articulations_and_ornaments_use_correct_collections(self):
        note = music21.note.Note('C4')
        instrumentation = self.composer.instrumentation
        for name in ('accent', 'staccato', 'fermata', 'trill', 'tremolo', 'arco'):
            instrumentation.apply_articulation(note, name)
        self.assertEqual([type(a).__name__ for a in note.articulations], ['Accent', 'Staccato'])
        self.assertEqual([type(e).__name__ for e in note.expressions],
                         ['Fermata', 'Trill', 'Tremolo', 'TextExpression'])
