"""Tk workspace: tone-row controls, matrix rendering and composition settings."""

import random
import tkinter as tk
from tkinter import ttk, messagebox

from ..matrix import build_matrix, build_variants, parse_tone_row
from ..composition.engine import AdvancedTwelveToneComposer
from .generation import GenerationTask
from .results import ResultPresenter


class TwelveToneSuite:
    UI_COLORS = {
        'background': '#F7F7F7',
        'surface': '#FFFFFF',
        'text': '#111111',
        'muted_text': '#666666',
        'status': '#EEEEEE',
        'primary': '#111111',
        'primary_active': '#000000',
        'secondary': '#333333',
        'secondary_active': '#000000',
        'architect': '#FFFFFF',
        'architect_active': '#EEEEEE',
        'danger': '#FFFFFF',
        'danger_active': '#EEEEEE',
        'border': '#D4D4D4',
    }

    def __init__(self, root):
        self.root = root
        self.root.title("十二音序列专业工具套件")
        self.root.geometry("760x620")
        self.root.minsize(700, 560)
        self.root.configure(bg=self.UI_COLORS['background'])

        self.style = ttk.Style(self.root)
        self.style.theme_use('clam')
        self.style.configure(
            'Suite.Primary.TButton',
            background=self.UI_COLORS['primary'],
            foreground='#FFFFFF',
            font=('Arial', 13, 'bold'),
            padding=(18, 11),
            borderwidth=0,
        )
        self.style.map(
            'Suite.Primary.TButton',
            background=[('active', self.UI_COLORS['primary_active'])],
            foreground=[('active', '#FFFFFF')],
        )
        self.style.configure(
            'Suite.Secondary.TButton',
            background=self.UI_COLORS['secondary'],
            foreground='#FFFFFF',
            font=('Arial', 13, 'bold'),
            padding=(18, 11),
            borderwidth=0,
        )
        self.style.map(
            'Suite.Secondary.TButton',
            background=[('active', self.UI_COLORS['secondary_active'])],
            foreground=[('active', '#FFFFFF')],
        )
        self.style.configure(
            'Suite.Architect.TButton',
            background=self.UI_COLORS['architect'],
            foreground='#FFFFFF',
            font=('Arial', 12, 'bold'),
            padding=(18, 9),
            borderwidth=0,
        )
        self.style.map(
            'Suite.Architect.TButton',
            background=[('active', self.UI_COLORS['architect_active'])],
            foreground=[('active', '#FFFFFF')],
        )
        self.style.configure(
            'Suite.Danger.TButton',
            background=self.UI_COLORS['surface'],
            foreground=self.UI_COLORS['text'],
            font=('Arial', 11, 'bold'),
            padding=(16, 8),
            borderwidth=1,
        )
        self.style.map(
            'Suite.Danger.TButton',
            background=[('active', self.UI_COLORS['danger_active'])],
            foreground=[('active', self.UI_COLORS['text'])],
        )
        self.style.configure(
            'Suite.Light.TButton',
            background=self.UI_COLORS['surface'],
            foreground=self.UI_COLORS['text'],
            font=('Arial', 10, 'bold'),
            padding=(10, 7),
            borderwidth=1,
        )
        self.style.map(
            'Suite.Light.TButton',
            background=[('active', '#EEEEEE')],
            foreground=[('active', self.UI_COLORS['text'])],
        )

        # 存储共享数据
        self.composer_data = {}
        self.current_row = []
        self.current_matrix = []
        self.current_matrix_data = {}
        self.workspace_row_var = tk.StringVar(value='等待生成')
        self.last_output_file = None

        # 创建主界面
        self.generation_task = GenerationTask()
        self.create_main_interface()
        self.results = ResultPresenter(self.root, self.status_label, self.UI_COLORS)

    def create_main_interface(self):
        colors = self.UI_COLORS
        self.root.title('十二音矩阵')
        self.root.geometry('1100x980')
        self.root.minsize(900, 760)
        self.root.configure(bg=colors['background'])

        header = tk.Frame(self.root, bg=colors['background'])
        header.pack(fill=tk.X, padx=30, pady=(24, 12))
        tk.Label(
            header,
            text='十二音矩阵',
            font=('Arial', 24, 'bold'),
            bg=colors['background'],
            fg=colors['text'],
        ).pack()
        tk.Label(
            header,
            text='十二音 · 序列矩阵',
            font=('Arial', 13),
            bg=colors['background'],
            fg=colors['muted_text'],
        ).pack(pady=(3, 0))

        status_frame = tk.Frame(self.root, bg=colors['status'])
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_label = tk.Label(
            status_frame,
            text='同一界面完成音列生成、矩阵查看与音乐生成',
            anchor=tk.W,
            bg=colors['status'],
            fg=colors['muted_text'],
            font=('Arial', 10),
        )
        self.status_label.pack(fill=tk.X, padx=14, pady=7)

        scroll_shell = tk.Frame(self.root, bg=colors['background'])
        scroll_shell.pack(fill=tk.BOTH, expand=True, padx=24, pady=(0, 12))
        canvas = tk.Canvas(scroll_shell, bg=colors['background'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_shell, orient=tk.VERTICAL, command=canvas.yview)
        scrollable = tk.Frame(canvas, bg=colors['background'])
        scroll_window = canvas.create_window((0, 0), window=scrollable, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollable.bind('<Configure>', lambda _event: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.bind('<Configure>', lambda event: canvas.itemconfigure(scroll_window, width=event.width))
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        content = tk.Frame(scrollable, bg=colors['background'])
        content.pack(fill=tk.X, padx=6, pady=4)
        content.columnconfigure(0, weight=1)

        def make_card(parent, title, subtitle=''):
            card = tk.Frame(
                parent,
                bg=colors['surface'],
                highlightbackground=colors['border'],
                highlightthickness=1,
            )
            top = tk.Frame(card, bg=colors['surface'])
            top.pack(fill=tk.X, padx=18, pady=(17, 7))
            tk.Label(
                top,
                text=title,
                font=('Arial', 16, 'bold'),
                bg=colors['surface'],
                fg=colors['text'],
            ).pack(anchor=tk.W)
            if subtitle:
                tk.Label(
                    top,
                    text=subtitle,
                    font=('Arial', 9),
                    bg=colors['surface'],
                    fg=colors['muted_text'],
                ).pack(anchor=tk.W, pady=(3, 0))
            return card

        # 第一张卡片：按参考图的横向按钮组布局
        sequence_card = make_card(
            content,
            '序列生成器',
            '输入 12 个不重复的数字或音名，生成后将在本页显示完整矩阵。',
        )
        sequence_card.pack(fill=tk.X, pady=(0, 14))
        sequence_body = tk.Frame(sequence_card, bg=colors['surface'])
        sequence_body.pack(fill=tk.X, padx=18, pady=(4, 18))
        tk.Label(
            sequence_body,
            text='当前音列',
            font=('Arial', 10, 'bold'),
            bg=colors['surface'],
            fg=colors['text'],
        ).pack(anchor=tk.W)
        self.sequence_entry = tk.Entry(
            sequence_body,
            font=('Arial', 16),
            bg='#FFFFFF',
            fg=colors['text'],
            relief=tk.SOLID,
            bd=1,
        )
        self.sequence_entry.insert(0, 'C C# D D# E F F# G G# A A# B')
        self.sequence_entry.pack(fill=tk.X, pady=(7, 14), ipady=8)
        self.sequence_entry.bind('<Return>', lambda _event: self.generate_matrix_from_entry())

        matrix_actions = tk.Frame(sequence_body, bg=colors['surface'])
        matrix_actions.pack(fill=tk.X)
        for column in range(4):
            matrix_actions.columnconfigure(column, weight=1)
        ttk.Button(matrix_actions, text='生成', command=self.open_matrix_generator,
                   style='Suite.Primary.TButton').grid(row=0, column=0, sticky='ew', padx=(0, 7))
        ttk.Button(matrix_actions, text='随机', command=self.randomize_workspace_row,
                   style='Suite.Light.TButton').grid(row=0, column=1, sticky='ew', padx=7)
        ttk.Button(matrix_actions, text='默认', command=self.set_workspace_default,
                   style='Suite.Light.TButton').grid(row=0, column=2, sticky='ew', padx=7)
        ttk.Button(matrix_actions, text='清空', command=self.clear_workspace_sequence,
                   style='Suite.Light.TButton').grid(row=0, column=3, sticky='ew', padx=(7, 0))

        self.workspace_matrix_status_var = tk.StringVar(value='尚未生成矩阵')
        tk.Label(sequence_body, textvariable=self.workspace_matrix_status_var,
                 font=('Arial', 10), bg=colors['surface'], fg=colors['muted_text'],
                 anchor=tk.W).pack(anchor=tk.W, pady=(10, 0))

        # 第二张卡片：四种序列变体
        variants_card = make_card(
            content,
            '序列变体',
            '生成后可复制原形、倒影、逆行与逆行倒影。',
        )
        variants_card.pack(fill=tk.X, pady=(0, 14))
        variants_body = tk.Frame(variants_card, bg=colors['surface'])
        variants_body.pack(fill=tk.X, padx=18, pady=(2, 12))
        self.workspace_sequence_vars = {}
        variant_info = [
            ('P', '原形', '原位序列'),
            ('I', '倒影', '倒影序列'),
            ('R', '逆行', '逆行序列'),
            ('RI', '逆行倒影', '逆行倒影序列'),
        ]
        for index, (variant, title, subtitle) in enumerate(variant_info):
            row = tk.Frame(variants_body, bg=colors['surface'])
            row.pack(fill=tk.X, pady=(0 if index == 0 else 8, 0))
            row.columnconfigure(1, weight=1)
            badge = tk.Label(row, text=variant, width=4, height=2,
                             font=('Arial', 12, 'bold'), bg=colors['surface'],
                             fg=colors['text'], relief=tk.SOLID, bd=1)
            badge.grid(row=0, column=0, rowspan=2, sticky='nw', padx=(0, 12))
            tk.Label(row, text=title, font=('Arial', 11, 'bold'),
                     bg=colors['surface'], fg=colors['muted_text']).grid(
                         row=0, column=1, sticky='sw')
            sequence_var = tk.StringVar(value='等待生成')
            self.workspace_sequence_vars[variant] = sequence_var
            tk.Label(row, textvariable=sequence_var, font=('Arial', 12),
                     bg=colors['surface'], fg=colors['text'], anchor=tk.W).grid(
                         row=1, column=1, sticky='ew', pady=(2, 0))
            ttk.Button(row, text='复制', command=lambda key=variant: self.copy_workspace_sequence(key),
                       style='Suite.Light.TButton').grid(row=0, column=2, rowspan=2,
                                                         sticky='e', padx=(12, 0))
            if index < len(variant_info) - 1:
                tk.Frame(variants_body, height=1, bg=colors['border']).pack(fill=tk.X, pady=(8, 0))

        # 第三张卡片：始终可见的十二音矩阵
        matrix_card = make_card(
            content,
            '十二音矩阵',
            '完整矩阵固定在当前界面中显示。',
        )
        matrix_card.pack(fill=tk.X, pady=(0, 14))
        matrix_body = tk.Frame(matrix_card, bg=colors['surface'])
        matrix_body.pack(fill=tk.X, padx=18, pady=(3, 18))
        matrix_toolbar = tk.Frame(matrix_body, bg=colors['surface'])
        matrix_toolbar.pack(fill=tk.X, pady=(0, 8))
        self.workspace_matrix_hint_var = tk.StringVar(value='12 × 12')
        tk.Label(matrix_toolbar, text='序列矩阵', font=('Arial', 14, 'bold'),
                 bg=colors['surface'], fg=colors['text']).pack(side=tk.LEFT)
        tk.Label(matrix_toolbar, textvariable=self.workspace_matrix_hint_var,
                 font=('Arial', 11), bg=colors['surface'], fg=colors['muted_text']).pack(side=tk.RIGHT)
        self.matrix_table = tk.Frame(matrix_body, bg=colors['surface'])
        self.matrix_table.pack(expand=True)

        # 第四张卡片：与矩阵同页的音乐生成器
        music_card = make_card(
            content,
            '音乐生成器',
            '直接使用上方当前矩阵生成 XML，并可一键交给 Sibelius。',
        )
        music_card.pack(fill=tk.X, pady=(0, 14))
        music_body = tk.Frame(music_card, bg=colors['surface'])
        music_body.pack(fill=tk.X, padx=18, pady=(4, 18))
        music_body.columnconfigure(0, weight=1)
        music_body.columnconfigure(1, weight=1)

        composer = AdvancedTwelveToneComposer()
        technique_ids = list(composer.settings.composition_techniques.keys())
        technique_labels = [composer.settings.composition_techniques[key]['name'] for key in technique_ids]
        self.workspace_technique_map = dict(zip(technique_labels, technique_ids))
        self.workspace_technique_var = tk.StringVar(value=technique_labels[0])
        self._workspace_field(music_body, '作曲技法', self.workspace_technique_var,
                              technique_labels, 0, 0)
        self.workspace_emotion_var = tk.StringVar(value='默认')
        self._workspace_field(music_body, '音乐情感', self.workspace_emotion_var,
                              ['默认', '戏剧性', '抒情', '激动'], 0, 1)

        tempo_items = [f'{name} ({bpm} BPM)' for name, bpm in composer.settings.tempo_options.items()]
        self.workspace_tempo_lookup = dict(zip(tempo_items, composer.settings.tempo_options.values()))
        tempo_items.append('自定义速度')
        self.workspace_tempo_var = tk.StringVar(value='Andante (85 BPM)')
        self._workspace_field(music_body, '速度', self.workspace_tempo_var,
                              tempo_items, 1, 0)
        self.workspace_custom_bpm_var = tk.StringVar(value='120')
        self.workspace_custom_bpm_entry = tk.Entry(
            music_body,
            textvariable=self.workspace_custom_bpm_var,
            font=('Arial', 10),
            bg='#FFFFFF',
            fg=colors['text'],
            relief=tk.SOLID,
            bd=1,
            state=tk.DISABLED,
        )
        self.workspace_custom_bpm_entry.grid(row=2, column=0, sticky='w', padx=(0, 12), pady=(0, 12))
        self.workspace_tempo_var.trace_add('write', self.update_workspace_tempo)
        self.update_workspace_tempo()

        settings_row = tk.Frame(music_body, bg=colors['surface'])
        settings_row.grid(row=1, column=1, sticky='ew', padx=(12, 0), pady=(0, 12))
        self.workspace_measures_var = tk.StringVar(value='45')
        self.workspace_language_var = tk.StringVar(value='中文')
        tk.Label(settings_row, text='小节数', font=('Arial', 10, 'bold'),
                 bg=colors['surface'], fg=colors['text']).pack(anchor=tk.W)
        tk.Entry(settings_row, textvariable=self.workspace_measures_var, width=7,
                 font=('Arial', 10), bg='#FFFFFF', fg=colors['text'],
                 relief=tk.SOLID, bd=1).pack(anchor=tk.W, pady=(5, 10), ipady=2)
        tk.Label(settings_row, text='输出语言', font=('Arial', 10, 'bold'),
                 bg=colors['surface'], fg=colors['text']).pack(anchor=tk.W)
        ttk.Combobox(
            settings_row,
            textvariable=self.workspace_language_var,
            values=['中文', 'English'],
            state='readonly',
        ).pack(fill=tk.X, pady=(5, 0))

        tk.Label(music_body, text='乐器（可多选）', font=('Arial', 10, 'bold'),
                 bg=colors['surface'], fg=colors['text']).grid(row=3, column=0,
                                                                columnspan=2, sticky='w')
        self.workspace_instruments = [
            'Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet',
            'Trombone', 'Tuba', 'Violin', 'Viola', 'Cello', 'Contrabass',
            'Piano', 'Harp', 'Timpani', 'Snare Drum', 'Bass Drum', 'Cymbal',
            'Violin I', 'Violin II', 'Double Bass'
        ]
        instrument_frame = tk.Frame(music_body, bg=colors['surface'])
        instrument_frame.grid(row=4, column=0, columnspan=2, sticky='ew', pady=(5, 10))
        instrument_frame.columnconfigure(0, weight=1)
        self.workspace_instrument_list = tk.Listbox(
            instrument_frame,
            selectmode=tk.MULTIPLE,
            exportselection=False,
            height=6,
            font=('Arial', 9),
            bg='#FFFFFF',
            fg=colors['text'],
            selectbackground=colors['primary'],
            selectforeground='#FFFFFF',
            relief=tk.SOLID,
            bd=1,
        )
        instrument_scroll = ttk.Scrollbar(instrument_frame, orient=tk.VERTICAL,
                                          command=self.workspace_instrument_list.yview)
        self.workspace_instrument_list.configure(yscrollcommand=instrument_scroll.set)
        self.workspace_instrument_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        instrument_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        for instrument in self.workspace_instruments:
            self.workspace_instrument_list.insert(tk.END, instrument)
        for instrument in ['Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Piano']:
            self.workspace_instrument_list.selection_set(self.workspace_instruments.index(instrument))

        self.workspace_music_status_var = tk.StringVar(value='准备就绪：请先生成或修改音列。')
        tk.Label(
            music_body,
            textvariable=self.workspace_music_status_var,
            font=('Arial', 9),
            bg=colors['surface'],
            fg=colors['muted_text'],
            wraplength=300,
            justify=tk.LEFT,
        ).grid(row=5, column=0, columnspan=2, sticky='w', pady=(0, 8))
        self.workspace_generate_button = ttk.Button(
            music_body,
            text='使用当前魔方生成 XML',
            command=self.open_professional_composer,
            style='Suite.Primary.TButton',
        )
        self.workspace_generate_button.grid(row=6, column=0, sticky='ew', padx=(0, 6))
        self.workspace_open_sibelius_button = ttk.Button(
            music_body,
            text='一键打开 Sibelius',
            command=self.open_last_output_in_sibelius,
            style='Suite.Light.TButton',
            state=tk.DISABLED,
        )
        self.workspace_open_sibelius_button.grid(row=6, column=1, sticky='ew', padx=(6, 0))

        self.generate_matrix_from_entry()

    def _workspace_field(self, parent, label, variable, values, row, column):
        """创建统一工作台中的黑白下拉字段。"""
        field = tk.Frame(parent, bg=self.UI_COLORS['surface'])
        field.grid(row=row, column=column, sticky='ew',
                   padx=(0 if column == 0 else 12, 0), pady=(0, 8))
        tk.Label(field, text=label, font=('Arial', 10, 'bold'),
                 bg=self.UI_COLORS['surface'], fg=self.UI_COLORS['text']).pack(anchor=tk.W)
        ttk.Combobox(field, textvariable=variable, values=values,
                     state='readonly').pack(fill=tk.X, pady=(5, 0))

    def update_workspace_tempo(self, *_):
        """仅在选择自定义速度时启用 BPM 输入。"""
        self.workspace_custom_bpm_entry.config(
            state=tk.NORMAL if self.workspace_tempo_var.get() == '自定义速度' else tk.DISABLED
        )

    def open_matrix_generator(self):
        """在当前工作台生成并显示十二音魔方。"""
        self.generate_matrix_from_entry()

    def open_professional_composer(self):
        """使用当前界面中的魔方和音乐参数直接生成作品。"""
        self.start_workspace_generation()

    def _create_workspace_matrix(self, numbers):
        return build_matrix(numbers), build_variants(numbers)

    def generate_matrix_from_entry(self):
        """验证音列，并在当前工作台刷新矩阵。"""
        input_text = self.sequence_entry.get().strip()
        try:
            numbers = parse_tone_row(input_text)
        except (ValueError, KeyError) as error:
            messagebox.showerror('音列输入错误', str(error), parent=self.root)
            self.sequence_entry.focus_set()
            return False

        self.current_row = numbers
        self.current_matrix, self.current_matrix_data = self._create_workspace_matrix(numbers)
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        note_row = [note_names[number] for number in numbers]
        self.composer_data['imported_sequence'] = note_row
        self.composer_data['matrix_data'] = self.current_matrix_data
        self.workspace_row_var.set('  '.join(note_row))
        self.workspace_matrix_status_var.set('矩阵已生成：12 行 × 12 列，可直接用于音乐生成。')
        self.status_label.config(text='音列魔方已生成，右侧可直接设置并生成 XML。')
        self.render_workspace_matrix()
        self.render_workspace_sequences()
        return True

    def render_workspace_matrix(self):
        """把当前矩阵绘制到主工作台中央。"""
        for widget in self.matrix_table.winfo_children():
            widget.destroy()

        if not self.current_matrix:
            tk.Label(
                self.matrix_table,
                text='请输入音列后点击“生成”',
                font=('Arial', 14),
                bg=self.UI_COLORS['surface'],
                fg=self.UI_COLORS['muted_text'],
                padx=40,
                pady=60,
            ).pack()
            return

        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        colors = self.UI_COLORS
        diagonal_bg = '#F8F8F8'
        row_bg = '#F1F1F1'
        column_bg = '#F1F1F1'
        data_bg = '#FFFFFF'
        cell_font = ('Arial', 9, 'bold')

        corner = tk.Label(
            self.matrix_table,
            text='M',
            width=4,
            height=2,
            bg=colors['text'],
            fg='#FFFFFF',
            font=cell_font,
            relief=tk.SOLID,
            bd=1,
        )
        corner.grid(row=0, column=0, padx=1, pady=1, sticky='nsew')
        for column_index in range(12):
            label = tk.Label(
                self.matrix_table,
                text=f'I{(self.current_row[0] + self.current_row[column_index]) % 12}',
                width=4,
                height=2,
                bg=column_bg,
                fg=colors['text'],
                font=cell_font,
                relief=tk.SOLID,
                bd=1,
            )
            label.grid(row=0, column=column_index + 1, padx=1, pady=1, sticky='nsew')

        for row_index in range(12):
            row_label = tk.Label(
                self.matrix_table,
                text=f'P{(self.current_row[0] - self.current_row[row_index]) % 12}',
                width=4,
                height=2,
                bg=row_bg,
                fg=colors['text'],
                font=cell_font,
                relief=tk.SOLID,
                bd=1,
            )
            row_label.grid(row=row_index + 1, column=0, padx=1, pady=1, sticky='nsew')
            for column_index in range(12):
                background = data_bg
                if row_index == column_index:
                    background = diagonal_bg
                if row_index == 0:
                    background = '#F6F6F6'
                if column_index == 0:
                    background = '#F6F6F6'
                cell = tk.Label(
                    self.matrix_table,
                    text=note_names[self.current_matrix[row_index][column_index]],
                    width=4,
                    height=2,
                    bg=background,
                    fg=colors['text'],
                    font=cell_font,
                    relief=tk.SOLID,
                    bd=1,
                )
                cell.grid(row=row_index + 1, column=column_index + 1,
                          padx=1, pady=1, sticky='nsew')

    def render_workspace_sequences(self):
        """刷新 P/I/R/RI 四种基本序列。"""
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        for variant, variable in self.workspace_sequence_vars.items():
            sequence = self.current_matrix_data.get(variant, {}).get(0)
            if sequence is None:
                variable.set('等待生成')
            else:
                variable.set('  '.join(note_names[note] for note in sequence))

    def copy_workspace_sequence(self, variant):
        """复制当前序列变体到系统剪贴板。"""
        sequence = self.current_matrix_data.get(variant, {}).get(0)
        if sequence is None:
            messagebox.showwarning('尚未生成', '请先生成音列矩阵。', parent=self.root)
            return
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        text = ' '.join(note_names[note] for note in sequence)
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.status_label.config(text=f'{variant} 序列已复制到剪贴板。')

    def set_workspace_default(self):
        """恢复参考图风格的默认半音音列。"""
        default_row = 'C C# D D# E F F# G G# A A# B'
        self.sequence_entry.delete(0, tk.END)
        self.sequence_entry.insert(0, default_row)
        self.generate_matrix_from_entry()

    def clear_workspace_sequence(self):
        """清空音列和矩阵显示。"""
        self.sequence_entry.delete(0, tk.END)
        self.current_row = []
        self.current_matrix = []
        self.current_matrix_data = {}
        self.composer_data.pop('imported_sequence', None)
        self.composer_data.pop('matrix_data', None)
        self.workspace_row_var.set('等待生成')
        self.workspace_matrix_status_var.set('尚未生成矩阵')
        self.render_workspace_matrix()
        self.render_workspace_sequences()
        self.status_label.config(text='已清空，请输入新的音列。')

    def randomize_workspace_row(self):
        """在当前工作台生成一个随机音列。"""
        numbers = list(range(12))
        random.shuffle(numbers)
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.sequence_entry.delete(0, tk.END)
        self.sequence_entry.insert(0, ' '.join(note_names[value] for value in numbers))
        self.generate_matrix_from_entry()

    def pentatonic_workspace_row(self):
        """在当前工作台生成五声性音列。"""
        composer = AdvancedTwelveToneComposer()
        note_row = composer.generate_chinese_pentatonic_row()
        numbers = [composer.settings.note_to_num[note] for note in note_row]
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.sequence_entry.delete(0, tk.END)
        self.sequence_entry.insert(0, ' '.join(note_names[value] for value in numbers))
        self.generate_matrix_from_entry()

    def start_workspace_generation(self):
        """读取右侧音乐设置，直接使用当前矩阵开始后台生成。"""
        if not self.generate_matrix_from_entry():
            return

        selected_indices = self.workspace_instrument_list.curselection()
        if not selected_indices:
            messagebox.showwarning('缺少乐器', '请至少选择一种乐器。', parent=self.root)
            return
        instruments = [self.workspace_instruments[index] for index in selected_indices]

        tempo_selection = self.workspace_tempo_var.get()
        if tempo_selection == '自定义速度':
            try:
                tempo_value = int(self.workspace_custom_bpm_var.get())
                if tempo_value <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror('速度输入错误', '自定义 BPM 必须是大于 0 的整数。', parent=self.root)
                self.workspace_custom_bpm_entry.focus_set()
                return
            tempo_mark = f'Custom ({tempo_value} BPM)'
        else:
            tempo_value = self.workspace_tempo_lookup[tempo_selection]
            tempo_mark = tempo_selection.split(' (', 1)[0]

        try:
            num_measures = int(self.workspace_measures_var.get() or '45')
            if num_measures <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror('小节数输入错误', '小节数必须是大于 0 的整数。', parent=self.root)
            return

        emotion_map = {'默认': 'default', '戏剧性': 'dramatic', '抒情': 'lyrical', '激动': 'agitated'}
        language = 'en-US' if self.workspace_language_var.get() == 'English' else 'zh-CN'
        inputs = (
            self.composer_data['imported_sequence'],
            instruments,
            tempo_mark,
            tempo_value,
            num_measures,
            self.workspace_technique_map.get(self.workspace_technique_var.get(), 'schoenberg'),
            True,
            self.current_matrix_data,
            emotion_map.get(self.workspace_emotion_var.get(), 'default'),
        )
        self.workspace_music_status_var.set('正在使用当前 12×12 魔方生成 XML，请稍候……')
        self.status_label.config(text='正在根据当前魔方生成专业乐谱……')
        self.start_composer_generation(inputs, language)


    def start_composer_generation(self, inputs, language):
        if self.generation_task.running:
            return
        self.generation_task.start(inputs, language)
        self.workspace_generate_button.config(state=tk.DISABLED)
        self.root.after(50, self._poll_generation)

    def _poll_generation(self):
        result = self.generation_task.poll()
        if result is None:
            self.root.after(50, self._poll_generation)
            return
        succeeded, value = result
        if succeeded:
            self.composer_generation_complete(value)
        else:
            self.composer_generation_failed(value)

    def composer_generation_complete(self, filename):
        self.last_output_file = filename
        if hasattr(self, 'workspace_generate_button'):
            self.workspace_generate_button.config(state=tk.NORMAL)
        if hasattr(self, 'workspace_open_sibelius_button'):
            self.workspace_open_sibelius_button.config(state=tk.NORMAL)
        if hasattr(self, 'workspace_music_status_var'):
            self.workspace_music_status_var.set('生成完成：XML 已保存到桌面，可直接打开 Sibelius。')
        self.status_label.config(text=f'生成完成：{filename}')
        self.show_generation_success(filename)

    def show_generation_success(self, filename):
        self.results.show_success(filename)

    def open_last_output_in_sibelius(self):
        """从统一工作台直接打开最近一次生成的 XML。"""
        if not self.last_output_file:
            messagebox.showwarning('尚未生成', '请先使用当前魔方生成 XML。', parent=self.root)
            return
        self.open_in_sibelius(self.last_output_file)

    def open_in_sibelius(self, filename, parent=None):
        self.results.open_in_sibelius(filename, parent)

    def reveal_output_file(self, filename):
        self.results.reveal_output_file(filename)

    def composer_generation_failed(self, error_text):
        if hasattr(self, 'workspace_generate_button'):
            self.workspace_generate_button.config(state=tk.NORMAL)
        if hasattr(self, 'workspace_music_status_var'):
            self.workspace_music_status_var.set('生成失败，请检查设置或依赖库。')
        self.status_label.config(text='生成失败，请检查设置或依赖库。')
        messagebox.showerror('生成失败', error_text, parent=self.root)

    def run(self):
        self.root.mainloop()
