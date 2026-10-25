"""Optional real Tk smoke test: RUN_GUI_TESTS=1 python -m unittest discover -s tests."""

import contextlib
from functools import partial
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from twelve_tone.dependencies import music21


@unittest.skipUnless(os.environ.get('RUN_GUI_TESTS') == '1' and music21 is not None,
                     'set RUN_GUI_TESTS=1 on a desktop with Tk and music21')
class DesktopTests(unittest.TestCase):
    def test_workspace_controls_and_background_generation(self):
        import tkinter as tk
        from twelve_tone.composition.engine import AdvancedTwelveToneComposer
        from twelve_tone.ui.workspace import TwelveToneSuite

        root = tk.Tk()
        root.withdraw()
        self.addCleanup(root.destroy)
        suite = TwelveToneSuite(root)
        root.update_idletasks()
        self.assertEqual(suite.current_matrix[0], list(range(12)))
        self.assertEqual(len(suite.matrix_table.winfo_children()), 169)
        suite.clear_workspace_sequence()
        self.assertEqual(suite.current_matrix, [])
        suite.randomize_workspace_row()
        self.assertEqual(set(suite.current_row), set(range(12)))
        suite.sequence_entry.delete(0, tk.END)
        suite.sequence_entry.insert(0, '7 0 4 1 9 2 10 3 11 5 8 6')
        suite.generate_matrix_from_entry()
        self.assertEqual(suite.matrix_table.grid_slaves(row=0, column=1)[0]['text'], 'I2')
        self.assertEqual(suite.matrix_table.grid_slaves(row=1, column=0)[0]['text'], 'P0')
        suite.set_workspace_default()
        suite.workspace_measures_var.set('2')
        suite.workspace_instrument_list.selection_clear(0, tk.END)
        suite.workspace_instrument_list.selection_set(0)
        suite.workspace_tempo_var.set('自定义速度')
        suite.workspace_custom_bpm_var.set('90')
        self.assertEqual(str(suite.workspace_custom_bpm_entry['state']), 'normal')
        completions, failures = [], []
        suite.show_generation_success = completions.append
        suite.composer_generation_failed = failures.append

        with tempfile.TemporaryDirectory() as directory, \
             patch('twelve_tone.ui.generation.AdvancedTwelveToneComposer',
                   partial(AdvancedTwelveToneComposer, output_dir=directory)), \
             contextlib.redirect_stdout(io.StringIO()):
            suite.workspace_generate_button.invoke()
            self.assertEqual(str(suite.workspace_generate_button['state']), 'disabled')
            timeout = root.after(10000, root.quit)

            def check():
                if completions or failures:
                    root.quit()
                else:
                    root.after(20, check)

            root.after(20, check)
            root.mainloop()
            root.after_cancel(timeout)
            self.assertEqual(failures, [])
            self.assertEqual(len(completions), 1)
            self.assertTrue(Path(completions[0]).is_file())
            self.assertEqual(str(suite.workspace_generate_button['state']), 'normal')
            self.assertEqual(str(suite.workspace_open_sibelius_button['state']), 'normal')
            self.assertFalse(suite.generation_task.running)
