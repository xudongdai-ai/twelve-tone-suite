"""Generation result dialog and desktop file actions."""

import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

from ..export.files import open_score, reveal_file


class ResultPresenter:
    def __init__(self, root, status_label, colors):
        self.root = root
        self.status_label = status_label
        self.UI_COLORS = colors

    def show_success(self, filename):
        """显示生成结果，并提供一键打开 Sibelius 的入口。"""
        colors = self.UI_COLORS
        result_window = tk.Toplevel(self.root)
        result_window.title('生成完成')
        result_window.geometry('560x250')
        result_window.minsize(500, 220)
        result_window.configure(bg=colors['background'])
        result_window.transient(self.root)
        result_window.grab_set()

        tk.Label(
            result_window,
            text='专业乐谱已生成',
            font=('Arial', 18, 'bold'),
            bg=colors['background'],
            fg=colors['text'],
        ).pack(anchor=tk.W, padx=28, pady=(24, 6))
        tk.Label(
            result_window,
            text='XML 文件已经保存到桌面：',
            font=('Arial', 10),
            bg=colors['background'],
            fg=colors['muted_text'],
        ).pack(anchor=tk.W, padx=28)
        tk.Label(
            result_window,
            text=filename,
            font=('Arial', 10),
            bg=colors['surface'],
            fg=colors['text'],
            justify=tk.LEFT,
            anchor=tk.W,
            wraplength=500,
            padx=10,
            pady=8,
            relief=tk.SOLID,
            bd=1,
        ).pack(fill=tk.X, padx=28, pady=(6, 16))

        button_frame = tk.Frame(result_window, bg=colors['background'])
        button_frame.pack(fill=tk.X, padx=28, pady=(0, 22))
        ttk.Button(
            button_frame,
            text='在 Sibelius 中打开',
            command=lambda: self.open_in_sibelius(filename, result_window),
            style='Suite.Primary.TButton',
        ).pack(side=tk.LEFT)
        ttk.Button(
            button_frame,
            text='在桌面中显示',
            command=lambda: self.reveal_output_file(filename),
            style='Suite.Secondary.TButton',
        ).pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(
            button_frame,
            text='关闭',
            command=result_window.destroy,
            style='Suite.Danger.TButton',
        ).pack(side=tk.RIGHT)
        result_window.protocol('WM_DELETE_WINDOW', result_window.destroy)

    def open_in_sibelius(self, filename, parent=None):
        """调用系统打开命令，把生成的 MusicXML 交给 Sibelius。"""

        try:
            open_score(filename)
            self.status_label.config(text='已请求 Sibelius 打开生成的 XML 文件。')
        except (OSError, subprocess.CalledProcessError) as error:
            messagebox.showerror(
                '无法打开 Sibelius',
                f'未能自动打开 Sibelius。\n请确认已安装 Sibelius，或手动打开文件：\n{filename}\n\n原因：{error}',
                parent=parent or self.root,
            )

    def reveal_output_file(self, filename):
        """在文件管理器中定位生成的 XML 文件。"""

        try:
            reveal_file(filename)
            self.status_label.config(text='已在桌面中定位生成的 XML 文件。')
        except (OSError, subprocess.CalledProcessError) as error:
            messagebox.showerror('无法打开文件位置', f'无法定位文件：\n{filename}\n\n原因：{error}', parent=self.root)
