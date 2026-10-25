"""The single desktop application entry point."""


def main():
    try:
        import tkinter as tk
        from .ui.workspace import TwelveToneSuite
    except ImportError as error:
        if error.name in ('tkinter', '_tkinter'):
            raise SystemExit('当前 Python 缺少 Tk 支持，请使用包含 tkinter 的 Python。') from error
        raise
    root = tk.Tk()
    TwelveToneSuite(root).run()
