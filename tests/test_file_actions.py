from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

from twelve_tone.export.files import open_score, reveal_file


class FileActionTests(unittest.TestCase):
    def test_macos_sibelius_and_reveal_paths_are_single_arguments(self):
        filename = 'test scores/a score.xml'
        path = str(Path(filename).resolve())
        with patch('twelve_tone.export.files.sys.platform', 'darwin'), \
             patch('twelve_tone.export.files.subprocess.run') as run:
            open_score(filename)
            run.assert_called_once_with(['open', '-a', 'Sibelius', path], check=True)
            run.reset_mock()
            reveal_file(filename)
            run.assert_called_once_with(['open', '-R', path], check=True)

    def test_linux_uses_default_application_and_parent_directory(self):
        filename = str(Path('test.xml').resolve())
        with patch('twelve_tone.export.files.sys.platform', 'linux'), \
             patch('twelve_tone.export.files.os.name', 'posix'), \
             patch('twelve_tone.export.files.subprocess.run') as run:
            open_score(filename)
            run.assert_called_once_with(['xdg-open', filename], check=True)
            run.reset_mock()
            reveal_file(filename)
            run.assert_called_once_with(['xdg-open', str(Path(filename).parent)], check=True)

    def test_os_error_is_propagated_to_presenter(self):
        with patch('twelve_tone.export.files.sys.platform', 'darwin'), \
             patch('twelve_tone.export.files.subprocess.run', side_effect=OSError('missing app')):
            with self.assertRaises(OSError):
                open_score('test.xml')
