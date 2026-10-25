from pathlib import Path
import subprocess
import sys
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ImportTests(unittest.TestCase):
    def run_isolated(self, code):
        result = subprocess.run([sys.executable, '-c', textwrap.dedent(code)],
                                cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_matrix_and_composer_import_without_tk_or_music21(self):
        output = self.run_isolated('''
            import sys
            sys.modules['tkinter'] = None
            sys.modules['music21'] = None
            from twelve_tone.matrix import build_matrix
            from twelve_tone.composition.engine import AdvancedTwelveToneComposer
            assert build_matrix(range(12))[0] == list(range(12))
            composer = AdvancedTwelveToneComposer()
            assert len(composer.generate_matrix(range(12))) == 48
            try:
                composer.run_with_inputs(None)
            except RuntimeError as error:
                assert 'music21' in str(error)
            else:
                raise AssertionError('Expected an actionable dependency error')
        ''')
        self.assertEqual(output, '')

    def test_entry_import_has_no_gui_side_effect(self):
        self.run_isolated('''
            import importlib.util, sys
            sys.modules['tkinter'] = None
            import twelve_tone.app, twelve_tone.__main__
            spec = importlib.util.spec_from_file_location('launcher', '十二音.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        ''')

    def test_both_launchers_invoke_main_once(self):
        self.run_isolated('''
            import runpy
            from unittest.mock import patch
            with patch('twelve_tone.app.main') as main:
                runpy.run_module('twelve_tone', run_name='__main__')
                main.assert_called_once_with()
            with patch('twelve_tone.app.main') as main:
                runpy.run_path('十二音.py', run_name='__main__')
                main.assert_called_once_with()
        ''')
