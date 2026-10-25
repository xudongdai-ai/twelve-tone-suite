"""Platform file actions, independent of Tk and score generation."""

import os
from pathlib import Path
import subprocess
import sys


def open_score(filename):
    path = str(Path(filename).resolve())
    if sys.platform == 'darwin':
        subprocess.run(['open', '-a', 'Sibelius', path], check=True)
    elif os.name == 'nt':
        os.startfile(path)
    else:
        subprocess.run(['xdg-open', path], check=True)


def reveal_file(filename):
    path = str(Path(filename).resolve())
    if sys.platform == 'darwin':
        subprocess.run(['open', '-R', path], check=True)
    elif os.name == 'nt':
        subprocess.run(['explorer', '/select,', path], check=True)
    else:
        subprocess.run(['xdg-open', str(Path(path).parent)], check=True)
