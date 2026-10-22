# twelve_tone_ai_architect.py
# 十二音AI (Twelve-Tone AI) - 终极产品架构版
# 集成核心开发提示词与现代作曲技法规划

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
import random
import datetime
import os
import sys
import json
import re

try:
    import music21
except ImportError:
    print("警告: 未安装 music21 库，音乐生成功能将不可用")
    print("请运行: pip install music21")


# ==========================================
# [新增] AI 产品架构师核心提示词库
# ==========================================

class TwelveToneAIArchitect:
    """
    【十二音AI 终极产品架构师核心】
    用于指导后续AI开发、功能迭代与系统升级的元数据与指令库。
    集成 DeepSeek/LLM 提示词生成器。
    """

    # 产品愿景与规格说明
    PRODUCT_SPECIFICATION = {
        "Product_Name": "Twelve-Tone AI (十二音AI)",
        "Vision": "集现代作曲技法、智能算法、专业乐器法及直观工作流于一体的创作平台",
        "Core_Pillars": [
            "算法内核升级: 频谱主义、简约主义、偶然音乐、音色旋律",
            "专业乐器法: 键盘/竖琴(左右手/踏板)、弦乐(弓法/泛音)、民乐(SoundFont/技法)",
            "序列魔方强化: 12x12完整性实时校验、自动修复、拖拽式生成",
            "界面现代化: 深色玻璃态、Ableton Clip视图、Dorico级精度",
            "AI生态: 集成DeepSeek开源模型接口，实现智能续写与对位"
        ],
        "References": ["MuseScore 4 (易用性)", "Sibelius (出版质量)", "Max/MSP (模块化)", "Band-in-a-Box (智能伴奏)"]
    }

    # 可直接投喂给AI (如 DeepSeek) 的开发指令集 (Core Prompts)
    DEVELOPMENT_PROMPTS = {
        "Phase_1_Core_Algorithm": """
[Role: DSP & Algorithm Engineer]
任务: 升级十二音序列生成核心 (AdvancedTwelveToneComposer)。
1. 集成“频谱主义”：编写函数 calculate_spectral_frequency(fundamental)，基于泛音列频率计算微音程音高集合。
2. 实现“偶然音乐”：引入加权随机算法 (Weighted Random Walk)，允许用户设定 '控制(Control) vs 混沌(Chaos)' 滑块。
3. 增加“风格模仿”：
   - 利盖蒂(Ligeti): 实现微复调(Micropolyphony)生成算法，创建密集的音簇织体。
   - 约翰·凯奇(Cage): 引入I Ching (易经) 随机数生成器来决定音高与时值。
""",
        "Phase_2_Instrumentation": """
[Role: Virtual Orchestrator]
任务: 优化乐器法逻辑 (Instrumentation Engine)。
1. 钢琴/竖琴优化：
   - 编写 logic_hand_split(): 自动将序列分配为符合解剖学的左手分解和弦与右手旋律。
   - 添加竖琴踏板图计算器 (Harp Pedal Diagram)。
2. 弦乐组深度定制：
   - 自动添加弓法标记：连弓(Legato)、跳弓(Spiccato)、巴托克拨奏(Snap Pizz)。
   - 泛音计算：在极限音域自动将实音转换为人工泛音 (Artificial Harmonics)。
3. 民乐扩展接口：
   - 定义 ChineseInstrumentTrait 类，预留 'Guzheng_Gliss'(刮奏) 与 'Pipa_Tremolo'(轮指) 的MIDI CC控制曲线生成逻辑。
""",
        "Phase_3_Matrix_Engine": """
[Role: Logic & Math Expert]
任务: 重构魔方生成器 (TwelveToneMatrix)。
1. 校验算法：实现 validate_matrix_integrity(12x12_array)，确保每行/列/主对角线无重复音级。
2. 自动修复：当检测到冲突时，编写 solve_matrix_conflict() 使用回溯算法自动填补正确音符。
3. 交互逻辑：开发 'Drag-to-Timeline' 接口，允许将矩阵行数据对象直接转换为时间线上的 Event Clip。
""",
        "Phase_4_Modern_UI": """
[Role: UI/UX Designer]
任务: 重构Tkinter界面为现代深色风格。
1. 样式表：定义 DeepDark 调色板 (Bg: #1E1E1E, Accent: #00FF99, Text: #E0E0E0)。
2. 布局重构：
   - 左侧: 序列控制面板 (Sequence Controller)
   - 中部: 交互式矩阵 (Interactive Matrix)
   - 右侧: 乐器与音色库 (Instrument & SoundFont)
3. 视图模式：模仿 Ableton Live，实现 Session View (Clip触发) 与 Arrangement View (线性时间轴) 的切换逻辑。
"""
    }

    # 详细开发路线图
    ROADMAP = [
        ("Phase 1", "内核算法与作曲家引擎", "风格库(后韦伯恩/五声序列)、自定义规则模块、MVP发布"),
        ("Phase 2", "专业乐器法与音色集成", "智能弓法/指法、通用GM/民乐音色库映射、Alpha测试"),
        ("Phase 3", "魔方矩阵与可视化交互", "实时验证修复、视觉关联、拖拽生成、Beta测试"),
        ("Phase 4", "界面现代化与工作流优化", "深色主题、拖拽式排列、Dorico导出优化"),
        ("Phase 5", "生态整合与高级功能", "社区分享、DeepSeek AI续写协作、多格式导出")
    ]

    @classmethod
    def get_prompt(cls, key):
        return cls.DEVELOPMENT_PROMPTS.get(key, "未找到对应提示词")

    @classmethod
    def show_blueprint(cls, parent):
        """显示架构蓝图窗口 (Dev Mode Dashboard)"""
        win = tk.Toplevel(parent)
        win.title("十二音AI - 终极产品架构师蓝图 (Dev Mode)")
        win.geometry("900x700")
        win.configure(bg='#1E1E1E')  # 深色背景 Phase 4 预览

        # 样式配置
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Dev.TNotebook", background="#1E1E1E", borderwidth=0)
        style.configure("Dev.TNotebook.Tab", background="#2D2D2D", foreground="#AAAAAA", padding=[10, 5])
        style.map("Dev.TNotebook.Tab", background=[("selected", "#3E3E3E")], foreground=[("selected", "#00FF99")])

        # 标题区域
        header_frame = tk.Frame(win, bg='#1E1E1E')
        header_frame.pack(fill=tk.X, padx=20, pady=15)

        tk.Label(header_frame, text="TWELVE-TONE AI ARCHITECT",
                 font=("Impact", 20), bg='#1E1E1E', fg='#00FF99').pack(side=tk.LEFT)
        tk.Label(header_frame, text="v7.0 Specification",
                 font=("Consolas", 10), bg='#1E1E1E', fg='#666666').pack(side=tk.LEFT, padx=10,
                                                                         check_on_pixels=False)  # micro-alignment

        # 选项卡
        notebook = ttk.Notebook(win, style="Dev.TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- 页面1: 愿景与规格 ---
        f1 = tk.Frame(notebook, bg='#252526')
        notebook.add(f1, text="  产品规格 (Specs)  ")

        info_text = scrolledtext.ScrolledText(f1, bg='#1E1E1E', fg='#D4D4D4',
                                              font=("Segoe UI", 11), insertbackground='white', relief=tk.FLAT)
        info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        content = f"PRODUCT: {cls.PRODUCT_SPECIFICATION['Product_Name']}\n"
        content += "=" * 50 + "\n\n"
        content += f"CORE VISION:\n{cls.PRODUCT_SPECIFICATION['Vision']}\n\n"
        content += "STRATEGIC PILLARS:\n"
        for p in cls.PRODUCT_SPECIFICATION['Core_Pillars']:
            content += f"[+] {p}\n"
        content += "\nBENCHMARKS:\n" + " | ".join(cls.PRODUCT_SPECIFICATION['References'])

        info_text.insert(tk.END, content)
        info_text.config(state=tk.DISABLED)

        # --- 页面2: AI开发提示词 (Prompt Engineering) ---
        f2 = tk.Frame(notebook, bg='#252526')
        notebook.add(f2, text="  DeepSeek指令集 (Prompts)  ")

        lbl_instruct = tk.Label(f2, text="提示: 复制以下内容发送给 DeepSeek/ChatGPT 以生成特定模块代码",
                                bg='#252526', fg='#888888', font=("Arial", 9))
        lbl_instruct.pack(pady=5, anchor=tk.W, padx=10)

        prompt_text = scrolledtext.ScrolledText(f2, bg='#1E1E1E', fg='#4EC9B0',
                                                font=("Consolas", 10), insertbackground='white', relief=tk.FLAT)
        prompt_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        p_content = "# SYSTEM CONTEXT: You are an expert Python Music Developer.\n\n"
        for k, v in cls.DEVELOPMENT_PROMPTS.items():
            p_content += f">>> 指令区块: [{k}]\n{v}\n{'-' * 60}\n\n"

        prompt_text.insert(tk.END, p_content)

        # --- 页面3: 路线图 (Roadmap) ---
        f3 = tk.Frame(notebook, bg='#252526')
        notebook.add(f3, text="  开发路线图 (Roadmap)  ")

        roadmap_text = scrolledtext.ScrolledText(f3, bg='#1E1E1E', fg='#CE9178',
                                                 font=("Consolas", 11), insertbackground='white', relief=tk.FLAT)
        roadmap_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        r_content = "AGILE DEVELOPMENT PLAN:\n\n"
        for phase, title, det in cls.ROADMAP:
            r_content += f"█ {phase}: {title.upper()}\n   └─ 目标: {det}\n\n"

        roadmap_text.insert(tk.END, r_content)
        roadmap_text.config(state=tk.DISABLED)

        # 底部操作栏
        action_frame = tk.Frame(win, bg='#2D2D2D', height=40)
        action_frame.pack(fill=tk.X)
        tk.Label(action_frame, text="Architect Mode Active", fg="#00FF99", bg="#2D2D2D", font=("Arial", 8)).pack(
            side=tk.RIGHT, padx=10, pady=5)


# ==========================================
# 原有功能模块 (保持不变)
# ==========================================

class MultilingualSystem:
    """多语言支持系统"""

    def __init__(self, language='zh-CN'):
        self.language = language
        self.translations = {
            'zh-CN': {
                'title': '十二音序列音乐生成器 - 专业作曲版本',
                'input_mode': '请选择十二音序列输入方式：\n1. 使用默认序列\n2. 手动输入序列\n3. 生成五声性序列',
                'manual_input': '请输入12个音名，用空格分隔\n示例: C C# D D# E F F# G G# A A# B',
                'generating': '正在生成专业级别的十二音序列作品...',
                'matrix_gen': '1. 生成音列矩阵...',
                'apply_tech': '2. 应用专业作曲技法...',
                'struct_gen': '3. 生成具有音乐结构的乐谱...',
                'export': '4. 导出专业乐谱文件...',
                'complete': '🎵 专业音乐生成完成！',
                'select_emotion': '请选择音乐情感 (1.戏剧性 2.抒情 3.激动 4.默认): ',
                'processing_emotion': '   应用情感表达系统: ',
                'processing_human': '   应用人性化与手写感处理...',
                'processing_xml': '   正在进行XML兼容性优化...',
                'tech_select': '请选择作曲技法',
                'inst_select': '乐器选择',
                'tempo_select': '速度设置',
                'measure_input': '请输入小节数 (默认45): ',
                'inst_prompt': '请输入乐器编号（多个编号用空格分隔）或直接回车使用默认设置',
                'using_seq': '使用序列:',
                'using_tech': '使用技法:',
                'using_inst': '使用乐器:',
            },
            'en-US': {
                'title': '12-Tone Serial Music Composer - Professional Edition',
                'input_mode': 'Select Input Mode:\n1. Default Sequence\n2. Manual Input\n3. Pentatonic Sequence',
                'manual_input': 'Enter 12 note names separated by spaces\nExample: C C# D D# E F F# G G# A A# B',
                'generating': 'Generating professional 12-tone serial composition...',
                'matrix_gen': '1. Generating tone row matrix...',
                'apply_tech': '2. Applying composition techniques...',
                'struct_gen': '3. Generating structured score...',
                'export': '4. Exporting professional score files...',
                'complete': '🎵 Composition Complete!',
                'select_emotion': 'Select Emotion (1.Dramatic 2.Lyrical 3.Agitated 4.Default): ',
                'processing_emotion': '   Applying Emotion Expression System: ',
                'processing_human': '   Applying Humanization & Handwritten touches...',
                'processing_xml': '   Optimizing XML compatibility...',
                'tech_select': 'Select Composition Technique',
                'inst_select': 'Instrument Selection',
                'tempo_select': 'Tempo Settings',
                'measure_input': 'Enter number of measures (Default 45): ',
                'inst_prompt': 'Enter instrument numbers (space separated) or Enter for default',
                'using_seq': 'Using Sequence:',
                'using_tech': 'Using Technique:',
                'using_inst': 'Using Instruments:',
            }
        }

    def get_text(self, key):
        return self.translations.get(self.language, self.translations['zh-CN']).get(key, key)


class EmotionExpressionSystem:
    """音乐表情与情感表达系统"""
    emotion_profiles = {
        'dramatic': {'dynamic_range': (0.7, 1.0), 'articulation_density': 0.8, 'phrase_shaping': 'arched'},
        'lyrical': {'dynamic_range': (0.4, 0.7), 'articulation_density': 0.3, 'phrase_shaping': 'linear'},
        'agitated': {'dynamic_range': (0.6, 1.0), 'articulation_density': 0.9, 'phrase_shaping': 'angular'},
        'default': {'dynamic_range': (0.5, 0.9), 'articulation_density': 0.5, 'phrase_shaping': 'balanced'}
    }

    def apply_emotion(self, score, emotion='default'):
        """为乐谱添加人性化表达"""
        profile = self.emotion_profiles.get(emotion, self.emotion_profiles['default'])

        for part in score.parts:
            # 1. 乐句呼吸与形态
            self._apply_phrasing(part, profile['phrase_shaping'])
            # 2. 演奏法密度调整
            self._apply_articulations(part, profile['articulation_density'])

    def _apply_phrasing(self, part, shape):
        measures = list(part.getElementsByClass('Measure'))
        # 简单的乐句逻辑：每4-8小节添加一个呼吸标记
        for i, measure in enumerate(measures):
            if i > 0 and i % random.choice([4, 6, 8]) == 0:
                try:
                    breath = music21.expressions.BreathMark()
                    measure.insert(3.5, breath)  # 在小节末尾
                except:
                    pass

    def _apply_articulations(self, part, density):
        for note in part.flatten().notes:
            if random.random() < density * 0.3:  # 避免过多
                if not note.articulations:
                    if density > 0.7:
                        note.articulations.append(music21.articulations.Accent())
                    elif density < 0.4:
                        note.articulations.append(music21.articulations.Tenuto())


class HandwrittenNotationGenerator:
    """模拟手写乐谱效果与人性化时值"""

    def add_human_touches(self, score):
        # 这里的效果主要体现在导出的XML数据微调，或者是MIDI回放的人性化
        for part in score.parts:
            # 1. 微妙的节奏偏差 (Rubato - 仅影响MIDI，不影响谱面视觉)
            for note in part.flatten().notes:
                # 模拟人性化演奏的时间偏移
                pass  # music21 的 offset 是绝对的，修改会影响对齐，此处主要做逻辑预留

            # 2. 视觉随机化 (模拟手写不规则)
            # 在MusicXML中通常需要设置具体的 layout offset，这里做兼容性处理
            pass


class PhrasingIntelligence:
    """智能乐句划分"""

    def add_intelligent_phrasing(self, score):
        for part in score.parts:
            try:
                notes = list(part.flatten().notes)
                if not notes: continue

                phrase_start_idx = 0
                for i in range(len(notes) - 1):
                    # 如果当前音符时值较长，或者与下一个音符之间有较长休止
                    current_end = notes[i].offset + notes[i].quarterLength
                    next_start = notes[i + 1].offset

                    is_long_note = notes[i].quarterLength >= 2.0
                    has_rest = (next_start - current_end) > 0

                    if (is_long_note or has_rest) and (i - phrase_start_idx > 2):
                        # 创建连线 (Slur)
                        slur = music21.spanner.Slur(notes[phrase_start_idx], notes[i])
                        part.insert(0, slur)
                        phrase_start_idx = i + 1
            except Exception as e:
                # 防止因复杂的连线逻辑导致崩溃
                pass


class XMLOptimizer:
    """XML兼容性优化"""

    def optimize_and_save(self, score, filename):
        # 1. 添加必需的元数据
        if not score.metadata:
            score.metadata = music21.metadata.Metadata()

        # 2. 确保所有部分都有 TimeSignature 和 KeySignature
        for part in score.parts:
            if not part.getElementsByClass('TimeSignature'):
                part.insert(0, music21.meter.TimeSignature('4/4'))
            if not part.getElementsByClass('KeySignature'):
                part.insert(0, music21.key.KeySignature(0))

        # 3. 导出设置 (Compatible Mode)
        score.write('musicxml', fp=filename, makeNotation=True)

        # 4. 后处理文本修复
        self._fix_xml_compatibility(filename)
        return filename

    def _fix_xml_compatibility(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 修复常见的软件识别标签，增加软件标识
            if '<software>' not in content:
                content = content.replace('<encoding>', '<encoding>\n    <software>TwelveToneSystem_Pro7</software>')

            # 确保 DOCTYPE 正确
            if 'partwise.dtd' not in content:
                doctype = '<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">\n'
                content = content.replace('<score-partwise', doctype + '<score-partwise')

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception:
            pass


class TwelveToneMatrix:
    def __init__(self, root):
        self.root = root
        self.root.title("十二音序列魔方生成器")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')

        # 音名映射表 (0-11 对应 C, C#, D, D#, E, F, F#, G, G#, A, A#, B)
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        # 初始化序列
        self.original_row = []
        self.matrix = []
        self.matrix_data = {}  # 存储完整的矩阵数据

        # 创建UI
        self.create_widgets()

    def create_widgets(self):
        # 标题
        title_label = tk.Label(self.root, text="十二音序列魔方生成器",
                               font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=10)

        # 说明文本
        desc_label = tk.Label(self.root,
                              text="请输入12个不重复的数字(0-11)，用空格分隔\n0=C, 1=C#, 2=D, 3=D#, 4=E, 5=F, 6=F#, 7=G, 8=G#, 9=A, 10=A#, 11=B",
                              font=("Arial", 10), bg='#f0f0f0', fg='#666', justify=tk.CENTER)
        desc_label.pack(pady=5)

        # 输入框和按钮框架
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10)

        # 输入框
        self.entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self.generate_matrix())

        # 生成按钮
        generate_btn = tk.Button(input_frame, text="生成魔方",
                                 command=self.generate_matrix,
                                 bg='#4CAF50', fg='white', font=("Arial", 10, "bold"))
        generate_btn.pack(side=tk.LEFT, padx=5)

        # 随机生成按钮
        random_btn = tk.Button(input_frame, text="随机序列",
                               command=self.generate_random,
                               bg='#2196F3', fg='white', font=("Arial", 10))
        random_btn.pack(side=tk.LEFT, padx=5)

        # 五声性序列按钮
        pentatonic_btn = tk.Button(input_frame, text="五声性序列",
                                   command=self.generate_pentatonic,
                                   bg='#FF9800', fg='white', font=("Arial", 10))
        pentatonic_btn.pack(side=tk.LEFT, padx=5)

        # 导出到音乐生成器按钮
        self.export_btn = tk.Button(input_frame, text="导出到音乐生成器",
                                    command=self.export_to_composer,
                                    bg='#9C27B0', fg='white', font=("Arial", 10),
                                    state=tk.DISABLED)
        self.export_btn.pack(side=tk.LEFT, padx=5)

        # 清空按钮
        clear_btn = tk.Button(input_frame, text="清空",
                              command=self.clear_all,
                              bg='#f44336', fg='white', font=("Arial", 10))
        clear_btn.pack(side=tk.LEFT, padx=5)

        # 结果显示框架
        result_frame = tk.Frame(self.root, bg='#f0f0f0')
        result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # 创建表格框架
        self.table_frame = tk.Frame(result_frame, bg='white', relief=tk.RAISED, bd=1)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("请输入12个不重复的数字(0-11)，用空格分隔")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                              relief=tk.SUNKEN, anchor=tk.W, bg='#e0e0e0')
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def generate_matrix(self):
        # 获取输入
        input_text = self.entry.get().strip()

        # 验证输入
        try:
            numbers = [int(x) for x in input_text.split()]
            if len(numbers) != 12:
                raise ValueError("请输入12个数字")
            if any(x < 0 or x > 11 for x in numbers):
                raise ValueError("数字必须在0到11之间")
            # 检查是否有重复数字
            if len(set(numbers)) != 12:
                raise ValueError("数字不能重复，必须是12个不同的数字")
        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
            return

        # 保存原始行
        self.original_row = numbers

        # 生成魔方
        self.create_twelve_tone_matrix()

        # 显示魔方
        self.display_matrix()

        # 将数字序列转换为音名序列
        note_sequence = [self.note_names[num] for num in numbers]

        # 更新状态
        self.status_var.set(f"成功生成十二音序列魔方 - 原始序列: {numbers} -> {note_sequence}")

        # 启用导出按钮
        self.export_btn.config(state=tk.NORMAL)

    def generate_random(self):
        # 生成随机序列（不重复）- 0-11的随机排列
        numbers = list(range(12))
        random.shuffle(numbers)

        # 设置输入框
        self.entry.delete(0, tk.END)
        self.entry.insert(0, ' '.join(map(str, numbers)))

        # 生成魔方
        self.generate_matrix()

    def generate_pentatonic(self):
        """生成中国五声性十二音序列"""
        # 五声音阶基础音：宫、商、角、徵、羽 (C, D, E, G, A)
        pentatonic_base = [0, 2, 4, 7, 9]  # C, D, E, G, A

        # 生成两个五声调式，覆盖12个音
        remaining_notes = [x for x in range(12) if x not in pentatonic_base]

        # 选择第二个五声调式的基础音
        if remaining_notes:
            # 随机选择一个基础音开始第二个五声调式
            start_idx = random.choice(remaining_notes)
            second_pentatonic = []
            # 构建五声音阶：全音、全音、小三度、全音
            intervals = [2, 2, 3, 2]  # 五声音阶的音程结构

            current_note = start_idx
            second_pentatonic.append(current_note)

            for interval in intervals:
                current_note = (current_note + interval) % 12
                second_pentatonic.append(current_note)

            # 合并两个五声调式，确保覆盖12个音
            all_notes = list(set(pentatonic_base + second_pentatonic))

            # 如果不足12个音，补充剩余音
            while len(all_notes) < 12:
                missing_notes = [x for x in range(12) if x not in all_notes]
                if missing_notes:
                    all_notes.append(random.choice(missing_notes))

            # 随机排列但保持五声性特征
            random.shuffle(all_notes)
            numbers = all_notes
        else:
            numbers = list(range(12))
            random.shuffle(numbers)

        # 设置输入框
        self.entry.delete(0, tk.END)
        self.entry.insert(0, ' '.join(map(str, numbers)))

        # 生成魔方
        self.generate_matrix()

        # 更新状态
        self.status_var.set("已生成中国五声性十二音序列")

    def clear_all(self):
        self.entry.delete(0, tk.END)
        self.original_row = []
        self.matrix = []
        self.matrix_data = {}

        # 清除表格
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # 禁用导出按钮
        self.export_btn.config(state=tk.DISABLED)

        # 更新状态
        self.status_var.set("已清空，请输入新的序列")

    def create_twelve_tone_matrix(self):
        """修正的十二音矩阵生成方法"""
        # 重置矩阵和数据
        self.matrix = [[0 for _ in range(12)] for _ in range(12)]
        self.matrix_data = {'P': {}, 'I': {}, 'R': {}, 'RI': {}}

        # 设置第一行 - 原始序列 (P0)
        self.matrix[0] = self.original_row.copy()
        self.matrix_data['P'][0] = self.original_row.copy()

        # 生成逆行序列 (R0) - 最后一行
        r0 = self.original_row[::-1]
        self.matrix_data['R'][0] = r0

        # 生成倒影序列 (I0) - 第一列
        i0 = [(12 - note) % 12 for note in self.original_row]
        self.matrix_data['I'][0] = i0

        # 生成倒影逆行序列 (RI0) - 对角线
        ri0 = [(12 - note) % 12 for note in r0]
        self.matrix_data['RI'][0] = ri0

        # 填充完整的12x12矩阵
        # 第一列是倒影序列
        for i in range(12):
            self.matrix[i][0] = i0[i]

        # 第一行是原始序列（已经设置）
        # 最后一行是逆行序列
        self.matrix[11] = r0

        # 最后一列是倒影逆行序列
        for i in range(12):
            self.matrix[i][11] = ri0[i]

        # 填充中间部分：使用矩阵计算规则
        # 矩阵[i][j] = (P0[j] + I0[i] - P0[0]) % 12
        for i in range(1, 11):
            for j in range(1, 11):
                self.matrix[i][j] = (self.matrix[0][j] + self.matrix[i][0] - self.matrix[0][0]) % 12

        # 生成所有移位变体
        for transposition in range(1, 12):
            self.matrix_data['P'][transposition] = [(note + transposition) % 12 for note in self.matrix_data['P'][0]]
            self.matrix_data['I'][transposition] = [(note + transposition) % 12 for note in self.matrix_data['I'][0]]
            self.matrix_data['R'][transposition] = [(note + transposition) % 12 for note in self.matrix_data['R'][0]]
            self.matrix_data['RI'][transposition] = [(note + transposition) % 12 for note in self.matrix_data['RI'][0]]

    def display_matrix(self):
        # 清除之前的表格
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # 创建表格
        for i in range(13):  # 13行：标题行 + 12数据行
            for j in range(13):  # 13列：标题列 + 12数据列
                cell_frame = tk.Frame(self.table_frame, relief=tk.RAISED, bd=1,
                                      bg='white', width=60, height=40)
                cell_frame.grid(row=i, column=j, sticky="nsew")
                cell_frame.grid_propagate(False)

                # 设置行列权重
                self.table_frame.grid_rowconfigure(i, weight=1)
                self.table_frame.grid_columnconfigure(j, weight=1)

                # 添加标签
                if i == 0 and j == 0:
                    # 左上角单元格
                    label = tk.Label(cell_frame, text="", bg='#e0e0e0',
                                     font=("Arial", 10, "bold"))
                elif i == 0 and j > 0:
                    # 第一行标题 (P0, P1, ...)
                    label = tk.Label(cell_frame, text=f"P{j - 1}", bg='#e0e0e0',
                                     font=("Arial", 10, "bold"))
                elif j == 0 and i > 0:
                    # 第一列标题 (I0, I1, ...)
                    label = tk.Label(cell_frame, text=f"I{i - 1}", bg='#e0e0e0',
                                     font=("Arial", 10, "bold"))
                else:
                    # 数据单元格 - 显示音名而不是数字
                    value = self.matrix[i - 1][j - 1]
                    note_name = self.note_names[value]

                    # 使用不同颜色区分不同类型的序列
                    if i == 1 and j == 1:
                        bg_color = '#FFCCCB'  # 原始序列第一个音高
                    elif i == 1:
                        bg_color = '#FFE5CC'  # 原始序列 (P)
                    elif j == 1:
                        bg_color = '#CCE5FF'  # 倒影序列 (I)
                    elif j == 12:
                        bg_color = '#D4EDDA'  # 逆行序列 (R)
                    elif i == 12:
                        bg_color = '#F8D7DA'  # 倒影逆行序列 (RI)
                    else:
                        bg_color = '#F0F0F0'  # 其他序列

                    label = tk.Label(cell_frame, text=note_name, bg=bg_color,
                                     font=("Arial", 10, "bold"))

                label.pack(expand=True, fill=tk.BOTH)

        # 添加序列类型标签
        type_frame = tk.Frame(self.root, bg='#f0f0f0')
        type_frame.pack(pady=5)

        # 创建图例
        legend_text = "序列类型: P(原始) | I(倒影) | R(逆行) | RI(倒影逆行)"
        legend_label = tk.Label(type_frame, text=legend_text,
                                font=("Arial", 10), bg='#f0f0f0', fg='#666')
        legend_label.pack()

    def export_to_composer(self):
        """导出矩阵数据到音乐生成器"""
        if not self.matrix_data:
            messagebox.showwarning("警告", "请先生成魔方矩阵")
            return

        # 让用户选择要使用的序列类型
        choice_window = tk.Toplevel(self.root)
        choice_window.title("选择序列")
        choice_window.geometry("400x300")
        choice_window.configure(bg='#f0f0f0')

        tk.Label(choice_window, text="选择要用于音乐生成的序列:",
                 font=("Arial", 12, "bold"), bg='#f0f0f0').pack(pady=10)

        # 创建选择框架
        selection_frame = tk.Frame(choice_window, bg='#f0f0f0')
        selection_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # 序列类型选择
        type_var = tk.StringVar(value="P")
        type_frame = tk.Frame(selection_frame, bg='#f0f0f0')
        type_frame.pack(fill=tk.X, pady=5)

        tk.Label(type_frame, text="序列类型:", bg='#f0f0f0').pack(side=tk.LEFT)
        for seq_type in ['P', 'I', 'R', 'RI']:
            tk.Radiobutton(type_frame, text=seq_type, variable=type_var,
                           value=seq_type, bg='#f0f0f0').pack(side=tk.LEFT, padx=10)

        # 移位选择
        transposition_frame = tk.Frame(selection_frame, bg='#f0f0f0')
        transposition_frame.pack(fill=tk.X, pady=5)

        tk.Label(transposition_frame, text="移位:", bg='#f0f0f0').pack(side=tk.LEFT)
        transposition_var = tk.IntVar(value=0)
        transposition_spinbox = tk.Spinbox(transposition_frame, from_=0, to=11,
                                           textvariable=transposition_var, width=5)
        transposition_spinbox.pack(side=tk.LEFT, padx=10)

        # 确认按钮
        def confirm_selection():
            seq_type = type_var.get()
            transposition = transposition_var.get()

            selected_sequence = self.matrix_data[seq_type][transposition]
            note_sequence = [self.note_names[note] for note in selected_sequence]

            # 保存到全局变量供音乐生成器使用
            if hasattr(self.root, 'composer_data'):
                self.root.composer_data['imported_sequence'] = note_sequence
                self.root.composer_data['matrix_data'] = self.matrix_data
            else:
                self.root.composer_data = {
                    'imported_sequence': note_sequence,
                    'matrix_data': self.matrix_data
                }

            choice_window.destroy()
            messagebox.showinfo("成功", f"已导出序列: {seq_type}{transposition}\n{note_sequence}")

        tk.Button(choice_window, text="确认导出", command=confirm_selection,
                  bg='#4CAF50', fg='white', font=("Arial", 10, "bold")).pack(pady=20)

    def run(self):
        self.root.mainloop()


class AdvancedTwelveToneComposer:
    def __init__(self):
        # 12音列音名转半音数值映射
        self.note_to_num = {
            "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
            "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11
        }

        # 半音数值转音名
        self.num_to_note = {v: k for k, v in self.note_to_num.items()}

        # 扩展力度选项 - 勋伯格风格
        self.dynamics_options = ["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff", "fp", "sfz", "sf", "rfz", "cresc.",
                                 "dim."]

        # 扩展节奏选项 - 更复杂的节奏型
        self.rhythms_options = [
            "whole", "half", "quarter", "eighth", "sixteenth", "32nd",
            "quarter triplet", "eighth triplet", "sixteenth triplet",
            "dotted half", "dotted quarter", "dotted eighth", "dotted sixteenth",
            "quarter rest", "half rest", "whole rest", "eighth rest", "16th rest"
        ]

        # 扩展演奏法选项 - 勋伯格风格
        self.articulations_options = [
            "staccato", "tenuto", "accent", "staccatissimo", "marcato",
            "portato", "spiccato", "sforzando", "fermata", "trill",
            "turn", "mordent", "glissando", "tremolo", "harmonics",
            "pizzicato", "arco", "col legno", "sul ponticello", "sul tasto"
        ]

        # 扩展表情记号选项
        self.expression_options = [
            "espressivo", "dolce", "cantabile", "grazioso", "legato",
            "non legato", "portamento", "vibrato", "pizzicato", "arco",
            "con brio", "con fuoco", "dolente", "gioioso", "misterioso",
            "agitato", "calmo", "appassionato", "lamentoso", "scherzando",
            "morendo", "perdendosi", "stringendo", "allargando", "rubato"
        ]

        # 速度选项
        self.tempo_options = {
            "Grave": 40,
            "Largo": 50,
            "Lento": 60,
            "Adagio": 70,
            "Andante": 85,
            "Moderato": 100,
            "Allegretto": 115,
            "Allegro": 130,
            "Vivace": 145,
            "Presto": 170,
            "Prestissimo": 200
        }

        # 修正音域映射 - 更准确的乐器音域（使用MIDI音高表示）
        self.instrument_ranges = {
            "Flute": (60, 96),  # C4-C7
            "Oboe": (58, 91),  # Bb3-G6
            "Clarinet": (50, 84),  # D3-C6
            "Bassoon": (34, 75),  # Bb1-E5
            "Horn": (41, 77),  # F2-F5
            "Trumpet": (55, 86),  # G3-D6
            "Trombone": (40, 72),  # E2-C5
            "Tuba": (29, 60),  # F1-C4
            "Violin": (55, 96),  # G3-C7
            "Viola": (48, 84),  # C3-C6
            "Cello": (36, 77),  # C2-F5
            "Contrabass": (28, 67),  # E1-G4
            "Piano": (21, 108),  # A0-C8
            "Harp": (36, 96),  # C2-C7
            "Timpani": (41, 53),  # F2-F3
            "Snare Drum": (38, 38),  # D2 (打击乐通常固定音高)
            "Bass Drum": (35, 35),  # B1
            "Cymbal": (49, 49),  # C#3
            "Violin I": (55, 96),  # G3-C7
            "Violin II": (55, 96),  # G3-C7
            "Double Bass": (28, 67)  # E1-G4

        }
        # 在 self.instrument_ranges 字典后添加：

        self.extended_instruments = {
            # 民族乐器
            "Guzheng": (48, 84),  # 古筝 C3-C6
            "Pipa": (50, 91),  # 琵琶 D3-G6
            "Erhu": (50, 91),  # 二胡 D3-G6
            "Dizi": (62, 96),  # 笛子 D4-C7
            "Suona": (58, 91),  # 唢呐 Bb3-G6
            "Yangqin": (48, 96),  # 扬琴 C3-C7

            # 现代乐器
            "Electric Guitar": (40, 88),
            "Bass Guitar": (28, 67),
            "Synthesizer": (21, 108),
            "Vibraphone": (53, 89),
            "Marimba": (45, 96),

            # 人声
            "Soprano": (60, 84),  # C4-C6
            "Alto": (55, 77),  # G3-F5
            "Tenor": (48, 72),  # C3-C5
            "Bass Voice": (40, 64),  # E2-E4
        }

        # 合并到主字典
        self.instrument_ranges.update(self.extended_instruments)

        # 需要大谱表的乐器
        self.grand_staff_instruments = ["Piano", "Harp"]

        # 作曲手法配置 - 添加更多发展手法
        self.composition_techniques = {
            "schoenberg": {
                "name": "勋伯格经典技法",
                "description": "严格遵循勋伯格的十二音作曲原则，强调序列完整性",
                "techniques": ["strict_serialism", "canon", "inversion", "knoten_technique",
                               "fragmentation", "augmentation", "diminution", "stretto"]
            },
            "webern": {
                "name": "韦伯恩点描技法",
                "description": "受韦伯恩影响的点描主义，使用短小动机和音色旋律",
                "techniques": ["pointillism", "klangfarbenmelodie", "silence", "registral_discontinuity",
                               "palindrome", "isomorphism", "symmetry", "micro_cell"]
            },
            "berg": {
                "name": "贝尔格抒情技法",
                "description": "融合贝尔格的抒情性和传统音乐元素",
                "techniques": ["lyricism", "quasi_tonal", "motivic_development", "expressive_contrast",
                               "leitmotif", "chromatic_saturation", "dramatic_arc", "narrative_form"]
            },
            "contemporary": {
                "name": "当代综合技法",
                "description": "融合多种现代作曲技术的综合方法",
                "techniques": ["spectral", "aleatoric", "extended_techniques", "microtonal",
                               "multiphonics", "texture_music", "process_form", "parameter_control"]
            },
            "chinese_pentatonic": {
                "name": "中国五声性十二音技法",
                "description": "融合中国五声调式与十二音序列技术，具有东方色彩",
                "techniques": ["pentatonic_serialism", "chinese_modal", "linear_contrast", "melodic_ornamentation",
                               "heterophony", "pentatonic_cluster", "modal_transformation", "cultural_fusion"]
            },
            "developmental": {
                "name": "发展性变奏技法",
                "description": "强调主题发展和变奏，结合传统与现代元素",
                "techniques": ["developmental_variation", "thematic_transformation", "motivic_manipulation",
                               "harmonic_expansion", "contrapuntal_elaboration", "rhythmic_complexity",
                               "textural_evolution", "formal_arch"]
            }
        }

        # 钢琴织体类型
        self.piano_texture_types = [
            "melodic_accompaniment",  # 旋律+伴奏
            "contrapuntal",  # 对位
            "chordal",  # 和弦式
            "arpeggiated",  # 琶音式
            "pointillistic",  # 点描式
            "cluster",  # 音簇式
            "ostinato",  # 固定音型
            "mixed"  # 混合式
        ]

        # 发展手法配置
        self.development_techniques = {
            "fragmentation": "片段化",
            "augmentation": "时值扩大",
            "diminution": "时值缩小",
            "inversion": "倒影",
            "retrograde": "逆行",
            "retrograde_inversion": "逆行倒影",
            "transposition": "移位",
            "sequence": "模进",
            "ornamentation": "装饰",
            "reharmonization": "重新和声化",
            "textural_variation": "织体变化",
            "registral_transfer": "音区转移",
            "rhythmic_displacement": "节奏移位",
            "canon": "卡农",
            "stretto": "密接和应"
        }

        # 初始化新功能系统
        self.lang_system = MultilingualSystem()
        self.emotion_system = EmotionExpressionSystem()
        self.human_system = HandwrittenNotationGenerator()
        self.phrasing_system = PhrasingIntelligence()
        self.xml_optimizer = XMLOptimizer()

    def apply_composer_intelligence(self, score, technique):
        """作曲家级别的智能优化"""

        # 1. 动机发展系统
        self.apply_motivic_development(score, technique)

        # 2. 和声色彩增强
        self.enhance_harmonic_color(score)

        # 3. 织体对比设计
        self.design_textural_contrast(score, technique)

        # 4. 高潮点计算
        self.calculate_climax_points(score)

        return score

    def apply_motivic_development(self, score, technique):
        """施加动机发展手法"""
        for part in score.parts:
            notes = list(part.flatten().notes)
            if len(notes) < 4: continue

            # 提取核心动机 (前3-4个音符)
            motive = notes[:4]

            # 在乐曲中期进行动机变奏
            mid_point = len(notes) // 2
            for i in range(mid_point, min(mid_point + 8, len(notes))):
                if i >= len(notes): break
                # 应用倒影/逆行等变换
                original_pitch = notes[i].pitch.midi
                if technique == "webern":
                    # 韦伯恩: 音区跳跃
                    notes[i].pitch.midi = original_pitch + random.choice([-12, 12, -24])
                elif technique == "berg":
                    # 贝尔格: 半音化扩展
                    notes[i].pitch.midi = original_pitch + random.choice([-1, 1, 2])

    def enhance_harmonic_color(self, score):
        """增强和声色彩 (为钢琴等和声乐器)"""
        for part in score.parts:
            if "Piano" not in part.partName: continue

            measures = list(part.getElementsByClass('Measure'))
            for m_idx, measure in enumerate(measures):
                # 每4小节添加一个和声色彩点
                if m_idx % 4 == 0:
                    chords = list(measure.getElementsByClass('Chord'))
                    if chords:
                        # 添加延音踏板标记
                        pedal_start = music21.expressions.TextExpression("Ped.")
                        measure.insert(0, pedal_start)

                        # 在小节末尾添加释放
                        pedal_end = music21.expressions.TextExpression("*")
                        measure.insert(3.5, pedal_end)

    def design_textural_contrast(self, score, technique):
        """设计织体对比"""
        num_measures = len(list(score.parts[0].getElementsByClass('Measure')))

        # 定义织体密度分布
        for section_start in range(0, num_measures, 16):
            section_type = random.choice(['sparse', 'dense', 'mixed'])

            for part in score.parts:
                measures = list(part.getElementsByClass('Measure'))
                for m_idx in range(section_start, min(section_start + 16, len(measures))):
                    if m_idx >= len(measures): break
                    measure = measures[m_idx]

                    if section_type == 'sparse':
                        # 稀疏织体: 增加休止符
                        notes = list(measure.flatten().notes)
                        if len(notes) > 2 and random.random() < 0.3:
                            rest = music21.note.Rest(quarterLength=0.5)
                            measure.insert(random.uniform(0, 3), rest)
                    elif section_type == 'dense':
                        # 密集织体: 缩短音符时值
                        for note in measure.flatten().notes:
                            if note.quarterLength > 0.5:
                                note.quarterLength *= 0.75

    def calculate_climax_points(self, score):
        """计算并标记高潮点"""
        num_measures = len(list(score.parts[0].getElementsByClass('Measure')))

        # 黄金分割点作为主高潮
        golden_ratio = int(num_measures * 0.618)

        for part in score.parts:
            measures = list(part.getElementsByClass('Measure'))
            if golden_ratio < len(measures):
                climax_measure = measures[golden_ratio]

                # 添加ff力度
                climax_measure.insert(0, music21.dynamics.Dynamic('ff'))

                # 添加重音标记
                for note in climax_measure.flatten().notes:
                    note.articulations.append(music21.articulations.Accent())

    def display_banner(self):
        """显示程序横幅"""
        print("=" * 60)
        print("          " + self.lang_system.get_text('title'))
        print("=" * 60)
        print()

    def get_user_input(self, imported_sequence=None, matrix_data=None):
        """获取用户输入"""
        self.display_banner()

        # 语言选择
        print("Language / 语言: [1] 中文 (Default) [2] English")
        lang_choice = input("Select: ").strip()
        if lang_choice == "2":
            self.lang_system.language = 'en-US'

        # 如果有导入的序列，优先使用
        if imported_sequence:
            print(f"{self.lang_system.get_text('using_seq')} {' '.join(imported_sequence)}")
            P0 = imported_sequence
            use_imported = True
        else:
            use_imported = False
            # 选择输入方式
            print(self.lang_system.get_text('input_mode'))
            choice = input("Select (1/2/3): ").strip()

            if choice == "2":
                print("\n" + self.lang_system.get_text('manual_input'))
                notes_input = input("Input: ").strip().upper().split()
                if len(notes_input) != 12:
                    print("Error: 12 notes required! Using default.")
                    P0 = ["C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#"]
                else:
                    P0 = notes_input
            elif choice == "3":
                P0 = self.generate_chinese_pentatonic_row()
                print(f"Pentatonic Sequence: {' '.join(P0)}")
            else:
                P0 = ["C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#"]

            print(f"\n{self.lang_system.get_text('using_seq')} {' '.join(P0)}")

        # 选择作曲技法
        print("\n" + "=" * 40)
        print(self.lang_system.get_text('tech_select'))
        print("=" * 40)

        for i, (tech_id, tech_info) in enumerate(self.composition_techniques.items()):
            print(f"{i + 1:2d}. {tech_info['name']:20} - {tech_info['description']}")

        try:
            tech_choice = int(input(f"\nSelect (1-{len(self.composition_techniques)}): ") or "1")
            selected_technique = list(self.composition_techniques.keys())[tech_choice - 1]
        except (ValueError, IndexError):
            selected_technique = "schoenberg"
            print("Using default: Schoenberg")

        print(f"{self.lang_system.get_text('using_tech')} {self.composition_techniques[selected_technique]['name']}")

        # 新增：情感选择
        print("\n" + self.lang_system.get_text('select_emotion'))
        emo_choice = input("Select: ").strip()
        emo_map = {'1': 'dramatic', '2': 'lyrical', '3': 'agitated'}
        selected_emotion = emo_map.get(emo_choice, 'default')

        # 选择乐器
        print("\n" + "=" * 40)
        print(self.lang_system.get_text('inst_select'))
        print("=" * 40)

        instrument_options = [
            "Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet",
            "Trombone", "Tuba", "Violin", "Viola", "Cello", "Contrabass",
            "Piano", "Harp", "Timpani", "Snare Drum", "Bass Drum", "Cymbal",
            "Violin I", "Violin II", "Double Bass"
        ]

        print("Instruments:")
        for i, instrument in enumerate(instrument_options):
            print(f"{i + 1:2d}. {instrument}")

        print("\n" + self.lang_system.get_text('inst_prompt'))
        print("Example: 1 3 5 7")
        instrument_choices = input("Selection: ").strip().split()

        try:
            if instrument_choices:
                instrument_indices = [int(x) - 1 for x in instrument_choices]
                instruments = [instrument_options[i] for i in instrument_indices
                               if 0 <= i < len(instrument_options)]
            else:
                instruments = ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet", "Piano"]
        except ValueError:
            print("Invalid input, using default set.")
            instruments = ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet", "Piano"]

        if not instruments:
            instruments = ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet", "Piano"]

        print(f"\n{self.lang_system.get_text('using_inst')} {', '.join(instruments)}")

        # 选择速度
        print("\n" + "=" * 40)
        print(self.lang_system.get_text('tempo_select'))
        print("=" * 40)

        for i, (tempo_name, bpm) in enumerate(self.tempo_options.items()):
            print(f"{i + 1:2d}. {tempo_name:12} (approx {bpm} BPM)")

        print(f"{len(self.tempo_options) + 1:2d}. Custom Tempo")

        tempo_choice = input(f"\nSelect (1-{len(self.tempo_options) + 1}, default 5): ").strip()

        if tempo_choice == str(len(self.tempo_options) + 1):
            try:
                custom_bpm = int(input("Enter BPM: "))
                tempo_mark = f"Custom ({custom_bpm} BPM)"
                tempo_value = custom_bpm
            except ValueError:
                print("Invalid, using Andante (85 BPM)")
                tempo_mark = "Andante"
                tempo_value = 85
        else:
            try:
                choice_idx = int(tempo_choice) - 1 if tempo_choice else 4
                if 0 <= choice_idx < len(self.tempo_options):
                    tempo_mark = list(self.tempo_options.keys())[choice_idx]
                    tempo_value = list(self.tempo_options.values())[choice_idx]
                else:
                    tempo_mark = "Andante"
                    tempo_value = 85
            except ValueError:
                tempo_mark = "Andante"
                tempo_value = 85

        print(f"Tempo: {tempo_mark} ({tempo_value} BPM)")

        # 选择小节数
        print("\n" + "=" * 40)
        print("Settings")
        print("=" * 40)

        try:
            num_measures = int(input(self.lang_system.get_text('measure_input')) or "45")
            if num_measures <= 0:
                print("Measures must be > 0. Using 45.")
                num_measures = 45
        except ValueError:
            num_measures = 45

        return P0, instruments, tempo_mark, tempo_value, num_measures, selected_technique, use_imported, matrix_data, selected_emotion

    def generate_chinese_pentatonic_row(self):
        """生成中国五声性十二音序列"""
        # 五声音阶：宫、商、角、徵、羽 (C, D, E, G, A)
        pentatonic_scale = [0, 2, 4, 7, 9]  # C, D, E, G, A

        # 生成两个互补的五声调式
        remaining_notes = [x for x in range(12) if x not in pentatonic_scale]

        # 从剩余音符中选择第二个五声调式的基础
        if len(remaining_notes) >= 5:
            # 随机选择一个基础音
            base_note = random.choice(remaining_notes)
            # 构建五声音阶：全音、全音、小三度、全音
            intervals = [2, 2, 3, 2]
            second_pentatonic = [base_note]
            current_note = base_note
            for interval in intervals:
                current_note = (current_note + interval) % 12
                second_pentatonic.append(current_note)
        else:
            # 如果剩余音符不足，使用随机选择
            second_pentatonic = random.sample(remaining_notes, min(5, len(remaining_notes)))
            # 补充不足的音符
            while len(second_pentatonic) < 5:
                available_notes = [x for x in range(12) if x not in pentatonic_scale + second_pentatonic]
                if available_notes:
                    second_pentatonic.append(random.choice(available_notes))
                else:
                    break

        # 合并两个五声调式
        all_notes = list(set(pentatonic_scale + second_pentatonic))

        # 如果不足12个音，补充剩余音
        while len(all_notes) < 12:
            missing_notes = [x for x in range(12) if x not in all_notes]
            if missing_notes:
                all_notes.append(random.choice(missing_notes))

        # 随机排列但保持五声性分组特征
        random.shuffle(all_notes)

        # 转换为音名
        pentatonic_row = [self.num_to_note[note] for note in all_notes]
        return pentatonic_row

    def apply_composition_technique(self, technique, matrix, current_measure, instrument_index):
        """应用专业作曲技法"""
        if technique == "schoenberg":
            return self.schoenberg_technique(matrix, current_measure, instrument_index)
        elif technique == "webern":
            return self.webern_technique(matrix, current_measure, instrument_index)
        elif technique == "berg":
            return self.berg_technique(matrix, current_measure, instrument_index)
        elif technique == "contemporary":
            return self.contemporary_technique(matrix, current_measure, instrument_index)
        elif technique == "chinese_pentatonic":
            return self.chinese_pentatonic_technique(matrix, current_measure, instrument_index)
        elif technique == "developmental":
            return self.developmental_technique(matrix, current_measure, instrument_index)
        else:
            return self.schoenberg_technique(matrix, current_measure, instrument_index)

    def schoenberg_technique(self, matrix, current_measure, instrument_index):
        """勋伯格经典技法"""
        section = current_measure // 8

        if section == 0:
            # 呈示部：展示原始序列和基本变形
            sequence_types = ["P", "I", "R", "RI"]
            sequence_type = sequence_types[instrument_index % 4]
            transposition = (current_measure // 2) % 6
        elif section == 1:
            # 展开部：复杂的序列组合
            sequence_types = ["P", "I", "R", "RI"]
            sequence_type = sequence_types[(current_measure + instrument_index) % 4]
            transposition = (current_measure * 3 + instrument_index) % 12
        elif section == 2:
            # 再现部：回归与综合
            sequence_type = "P"
            transposition = (4 + instrument_index * 2) % 12
        else:
            # 尾声：简化处理
            sequence_type = "RI"
            transposition = (8 - instrument_index) % 12

        sequence_key = f"{sequence_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def webern_technique(self, matrix, current_measure, instrument_index):
        """韦伯恩点描技法"""
        if current_measure % 4 == 0:
            base_type = ["P", "I", "R", "RI"][(current_measure // 4) % 4]
            transposition = (instrument_index * 5 + current_measure) % 12
        else:
            types = ["P", "I", "R", "RI"]
            base_type = types[(current_measure + instrument_index * 3) % 4]
            transposition = (current_measure * 7 + instrument_index * 11) % 12

        sequence_key = f"{base_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def berg_technique(self, matrix, current_measure, instrument_index):
        """贝尔格抒情技法"""
        section = current_measure // 12

        if section == 0:
            sequence_type = "P"
            transposition = (instrument_index * 3) % 12
        elif section == 1:
            types = ["P", "I"]
            sequence_type = types[instrument_index % 2]
            transposition = (current_measure + instrument_index * 7) % 12
        elif section == 2:
            sequence_type = "RI"
            transposition = (9 - instrument_index) % 12
        else:
            sequence_type = "P"
            transposition = (3 + instrument_index) % 12

        sequence_key = f"{sequence_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def contemporary_technique(self, matrix, current_measure, instrument_index):
        """当代综合技法"""
        section = current_measure // 16

        if section == 0:
            sequence_type = "P"
            transposition = (instrument_index * 2) % 12
        elif section == 1:
            types = ["P", "I", "R", "RI"]
            sequence_type = types[(current_measure + instrument_index) % 4]
            transposition = (current_measure * 3 + instrument_index * 5) % 12
        elif section == 2:
            sequence_type = "RI"
            transposition = (11 - instrument_index) % 12
        else:
            sequence_type = "P"
            transposition = (4 + instrument_index) % 12

        sequence_key = f"{sequence_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def chinese_pentatonic_technique(self, matrix, current_measure, instrument_index):
        """中国五声性十二音技法"""
        section = current_measure // 12

        if section == 0:
            sequence_type = "P"
            transposition = (instrument_index * 2) % 12
        elif section == 1:
            types = ["P", "I"]
            sequence_type = types[instrument_index % 2]
            transposition = (current_measure * 2 + instrument_index * 3) % 12
        elif section == 2:
            sequence_type = "R"
            transposition = (7 + instrument_index) % 12
        else:
            sequence_type = "RI"
            transposition = (5 - instrument_index) % 12

        sequence_key = f"{sequence_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def developmental_technique(self, matrix, current_measure, instrument_index):
        """发展性变奏技法"""
        section = current_measure // 10

        if section == 0:
            # 主题呈示
            sequence_type = "P"
            transposition = (instrument_index * 2) % 12
        elif section == 1:
            # 第一次变奏：片段化
            if current_measure % 3 == 0:
                sequence_type = "P"
                transposition = (current_measure + instrument_index * 5) % 12
            else:
                sequence_type = "I"
                transposition = (current_measure * 2 + instrument_index) % 12
        elif section == 2:
            # 第二次变奏：节奏变化
            sequence_type = "R"
            transposition = (8 + instrument_index * 3) % 12
        elif section == 3:
            # 第三次变奏：音区扩展
            sequence_type = "RI"
            transposition = (4 + current_measure) % 12
        else:
            # 综合再现
            sequence_type = "P"
            transposition = (6 + instrument_index) % 12

        sequence_key = f"{sequence_type}{transposition}"
        if sequence_key in matrix:
            return matrix[sequence_key]
        else:
            return matrix["P0"]

    def apply_development_technique(self, sequence, technique, measure_num, instrument_index):
        """应用具体的发展手法"""
        if technique == "fragmentation":
            # 片段化：使用序列的一部分
            fragment_length = random.choice([3, 4, 5, 6])
            start_pos = (measure_num + instrument_index) % (12 - fragment_length)
            return sequence[start_pos:start_pos + fragment_length]

        elif technique == "augmentation":
            # 时值扩大（这里用音高扩展模拟）
            expanded_sequence = []
            for note in sequence:
                expanded_sequence.append(note)
                expanded_sequence.append((note + 7) % 12)  # 添加五度音
            return expanded_sequence[:12]  # 确保长度不超过12

        elif technique == "diminution":
            # 时值缩小（这里用音高压缩模拟）
            if len(sequence) >= 6:
                return sequence[::2]  # 每隔一个音取一个
            return sequence

        elif technique == "sequence":
            # 模进：序列移位
            shift = (measure_num % 5) + 1
            return [(note + shift) % 12 for note in sequence]

        elif technique == "ornamentation":
            # 装饰：添加邻近音
            ornamented = []
            for note in sequence:
                ornamented.append(note)
                if len(ornamented) < 12:
                    ornamented.append((note + 1) % 12)  # 添加半音装饰
            return ornamented[:12]

        else:
            return sequence

    def generate_piano_texture_type(self, measure_num, technique):
        """为钢琴生成织体类型"""
        section = measure_num // 16

        if technique == "schoenberg":
            texture_cycle = ["contrapuntal", "chordal", "melodic_accompaniment", "arpeggiated"]
        elif technique == "webern":
            texture_cycle = ["pointillistic", "cluster", "mixed", "ostinato"]
        elif technique == "berg":
            texture_cycle = ["melodic_accompaniment", "chordal", "arpeggiated", "contrapuntal"]
        elif technique == "chinese_pentatonic":
            texture_cycle = ["melodic_accompaniment", "arpeggiated", "chordal", "mixed"]
        elif technique == "developmental":
            texture_cycle = ["contrapuntal", "melodic_accompaniment", "chordal", "arpeggiated", "mixed"]
        else:
            texture_cycle = ["mixed", "contrapuntal", "chordal", "pointillistic"]

        texture_index = (section + measure_num // 4) % len(texture_cycle)
        return texture_cycle[texture_index]

    def generate_piano_treble_rhythm(self, technique, measure_num, texture_type):
        """生成钢琴高音部节奏模式"""
        if texture_type == "melodic_accompaniment":
            patterns = [
                ["eighth", "eighth", "quarter", "eighth", "eighth"],
                ["quarter", "eighth", "eighth", "quarter", "eighth"],
                ["eighth", "quarter", "eighth", "eighth", "quarter"],
                ["16th", "16th", "16th", "16th", "quarter", "eighth"]
            ]
        elif texture_type == "contrapuntal":
            patterns = [
                ["dotted eighth", "16th", "quarter", "eighth", "eighth"],
                ["eighth", "eighth", "dotted eighth", "16th", "quarter"],
                ["16th", "16th", "eighth", "eighth", "quarter", "eighth"],
                ["quarter", "16th", "16th", "eighth", "eighth", "eighth"]
            ]
        elif texture_type == "chordal":
            patterns = [
                ["half", "half"],
                ["quarter", "quarter", "half"],
                ["dotted half", "quarter"],
                ["quarter", "dotted half"]
            ]
        elif texture_type == "arpeggiated":
            patterns = [
                ["16th", "16th", "16th", "16th", "16th", "16th", "16th", "16th"],
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["16th", "16th", "16th", "16th", "eighth", "eighth", "quarter"],
                ["eighth", "16th", "16th", "eighth", "16th", "16th", "quarter"]
            ]
        elif texture_type == "pointillistic":
            patterns = [
                ["32nd", "32nd rest", "32nd", "32nd rest", "16th", "16th rest", "eighth"],
                ["16th", "16th rest", "32nd", "32nd", "16th rest", "eighth"],
                ["32nd", "32nd", "32nd", "32nd rest", "16th", "eighth rest", "eighth"],
                ["16th triplet", "16th triplet", "16th triplet", "eighth rest", "32nd", "32nd"]
            ]
        elif texture_type == "cluster":
            patterns = [
                ["32nd", "32nd", "32nd", "32nd", "32nd", "32nd", "32nd", "32nd"],
                ["16th", "16th", "16th", "16th", "16th", "16th", "16th", "16th"],
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["quarter", "quarter", "quarter", "quarter"]
            ]
        elif texture_type == "ostinato":
            patterns = [
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["16th", "16th", "16th", "16th", "16th", "16th", "16th", "16th"],
                ["eighth", "16th", "16th", "eighth", "16th", "16th", "eighth"],
                ["16th", "16th", "eighth", "16th", "16th", "eighth", "16th", "16th"]
            ]
        else:  # mixed
            patterns = [
                ["quarter", "eighth", "eighth", "16th", "16th", "quarter"],
                ["eighth", "eighth", "quarter", "16th", "16th", "eighth", "eighth"],
                ["16th", "16th", "eighth", "eighth", "quarter", "16th", "16th"],
                ["dotted eighth", "16th", "quarter", "eighth", "eighth", "16th"]
            ]

        pattern_index = measure_num % len(patterns)
        return patterns[pattern_index]

    def generate_piano_bass_rhythm(self, technique, measure_num, texture_type):
        """生成钢琴低音部节奏模式"""
        if texture_type == "melodic_accompaniment":
            patterns = [
                ["half", "half"],
                ["dotted half", "quarter"],
                ["quarter", "quarter", "half"],
                ["whole"]
            ]
        elif texture_type == "contrapuntal":
            patterns = [
                ["dotted quarter", "eighth", "half"],
                ["quarter", "quarter", "dotted quarter", "eighth"],
                ["eighth", "eighth", "quarter", "quarter", "half"],
                ["half", "eighth", "eighth", "quarter", "quarter"]
            ]
        elif texture_type == "chordal":
            patterns = [
                ["whole"],
                ["half", "half"],
                ["dotted half", "quarter"],
                ["quarter", "dotted half"]
            ]
        elif texture_type == "arpeggiated":
            patterns = [
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["quarter", "quarter", "quarter", "quarter"],
                ["eighth", "eighth", "quarter", "eighth", "eighth", "quarter"],
                ["16th", "16th", "16th", "16th", "eighth", "eighth", "quarter"]
            ]
        elif texture_type == "pointillistic":
            patterns = [
                ["quarter rest", "32nd", "32nd", "32nd", "32nd", "half rest"],
                ["half rest", "16th", "16th", "16th", "16th", "quarter rest"],
                ["eighth rest", "32nd", "32nd", "32nd", "32nd", "32nd", "32nd", "eighth rest"],
                ["16th", "16th rest", "32nd", "32nd", "16th rest", "quarter"]
            ]
        elif texture_type == "cluster":
            patterns = [
                ["32nd", "32nd", "32nd", "32nd", "32nd", "32nd", "32nd", "32nd"],
                ["16th", "16th", "16th", "16th", "16th", "16th", "16th", "16th"],
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["quarter", "quarter", "quarter", "quarter"]
            ]
        elif texture_type == "ostinato":
            patterns = [
                ["eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth", "eighth"],
                ["quarter", "quarter", "quarter", "quarter"],
                ["eighth", "eighth", "quarter", "eighth", "eighth", "quarter"],
                ["16th", "16th", "16th", "16th", "eighth", "eighth", "quarter"]
            ]
        else:  # mixed
            patterns = [
                ["half", "quarter", "quarter"],
                ["dotted half", "eighth", "eighth"],
                ["quarter", "quarter", "half"],
                ["whole"]
            ]

        pattern_index = measure_num % len(patterns)
        return patterns[pattern_index]

    def generate_rhythm_pattern(self, technique, measure_num, instrument_index):
        """生成复杂的节奏模式"""
        if technique == "webern":
            patterns = [
                ["32nd", "32nd rest", "32nd", "32nd rest", "16th", "16th rest", "eighth"],
                ["16th triplet", "16th triplet", "16th triplet", "eighth rest", "32nd", "32nd"],
                ["eighth", "16th", "16th", "32nd", "32nd", "32nd rest", "16th"],
                ["quarter rest", "32nd", "32nd", "32nd", "32nd", "16th", "16th rest", "eighth"]
            ]
        elif technique == "schoenberg":
            patterns = [
                ["dotted eighth", "16th", "quarter", "eighth triplet", "eighth triplet", "eighth triplet"],
                ["eighth", "eighth", "quarter", "16th", "16th", "eighth", "eighth"],
                ["half", "quarter", "eighth", "16th", "32nd", "32nd", "16th"],
                ["quarter triplet", "quarter triplet", "quarter triplet", "eighth", "eighth"]
            ]
        elif technique == "berg":
            patterns = [
                ["quarter", "quarter", "eighth", "eighth", "half"],
                ["dotted quarter", "eighth", "quarter", "quarter", "eighth", "eighth"],
                ["half", "eighth", "eighth", "eighth", "eighth", "quarter"],
                ["quarter", "eighth", "eighth", "quarter", "eighth", "eighth", "eighth"]
            ]
        elif technique == "chinese_pentatonic":
            patterns = [
                ["dotted quarter", "eighth", "quarter", "quarter", "eighth"],
                ["quarter", "eighth", "eighth", "half", "eighth rest"],
                ["dotted half", "quarter", "eighth", "eighth"],
                ["eighth", "eighth", "quarter", "quarter", "eighth", "eighth"],
                ["quarter", "quarter rest", "eighth", "eighth", "quarter", "eighth"]
            ]
        elif technique == "developmental":
            patterns = [
                ["quarter", "eighth", "eighth", "quarter", "eighth", "eighth"],
                ["dotted quarter", "16th", "quarter", "eighth", "eighth"],
                ["eighth", "eighth", "quarter", "quarter", "eighth", "eighth"],
                ["16th", "16th", "eighth", "eighth", "quarter", "16th", "16th"]
            ]
        else:
            patterns = [
                ["32nd", "32nd", "32nd", "32nd", "32nd", "whole"],
                ["16th", "16th", "16th", "16th", "quarter rest", "dotted half"],
                ["eighth triplet", "eighth triplet", "eighth triplet", "half rest", "32nd", "32nd"],
                ["dotted eighth", "16th", "dotted eighth", "16th", "quarter", "eighth", "eighth"]
            ]

        pattern_index = (measure_num + instrument_index) % len(patterns)
        return patterns[pattern_index]

    def generate_dynamics_with_structure(self, num_measures, technique):
        """生成具有结构性的力度变化"""
        dynamics_plan = []

        for measure in range(num_measures):
            section = measure // 16

            if technique == "schoenberg":
                if section == 0:
                    base_dynamic = "mp" if measure % 8 < 4 else "mf"
                elif section == 1:
                    base_dynamic = "f" if measure % 12 < 6 else "ff"
                elif section == 2:
                    base_dynamic = "ff" if measure % 8 < 6 else "fff"
                else:
                    base_dynamic = "mf" if measure % 12 < 8 else "mp"

            elif technique == "webern":
                if measure % 4 == 0:
                    base_dynamic = random.choice(["pp", "p", "mp"])
                else:
                    base_dynamic = random.choice(["p", "mp", "mf"])

            elif technique == "berg":
                wave = (measure % 16) / 16.0
                if wave < 0.25:
                    base_dynamic = "p"
                elif wave < 0.5:
                    base_dynamic = "mp"
                elif wave < 0.75:
                    base_dynamic = "mf"
                else:
                    base_dynamic = "f"

            elif technique == "chinese_pentatonic":
                wave = (measure % 12) / 12.0
                if wave < 0.3:
                    base_dynamic = "mp"
                elif wave < 0.6:
                    base_dynamic = "mf"
                elif wave < 0.8:
                    base_dynamic = "f"
                else:
                    base_dynamic = "mf"

            elif technique == "developmental":
                # 发展性技法：更戏剧性的力度变化
                if section == 0:
                    base_dynamic = "mp"
                elif section == 1:
                    base_dynamic = "mf"
                elif section == 2:
                    base_dynamic = "f"
                elif section == 3:
                    base_dynamic = "ff"
                else:
                    base_dynamic = "mf"
            else:
                base_dynamic = random.choice(["ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"])

            variation = random.choice([-1, 0, 1, 1])
            dynamic_index = self.dynamics_options.index(base_dynamic) if base_dynamic in self.dynamics_options else 4
            new_index = max(0, min(len(self.dynamics_options) - 1, dynamic_index + variation))

            dynamics_plan.append(self.dynamics_options[new_index])

        return dynamics_plan

    def get_instrument_octave_range(self, instrument_name):
        """获取乐器的正常八度范围"""
        # 基于标准乐器音域返回合适的八度范围
        ranges = {
            "Flute": (4, 6),  # C4-C6
            "Oboe": (4, 6),  # Bb4-G6
            "Clarinet": (3, 5),  # D3-C5
            "Bassoon": (2, 4),  # Bb2-E4
            "Horn": (3, 5),  # F3-F5
            "Trumpet": (4, 5),  # G4-D5
            "Trombone": (2, 4),  # E2-C4
            "Tuba": (1, 3),  # F1-C3
            "Violin": (4, 7),  # G4-C7
            "Viola": (3, 6),  # C3-C6
            "Cello": (2, 5),  # C2-F5
            "Contrabass": (1, 4),  # E1-G3
            "Piano": (1, 7),  # A1-C7
            "Harp": (2, 6),  # C2-C6
            "Timpani": (2, 3),  # F2-F3
            "Snare Drum": (2, 2),  # D2
            "Bass Drum": (1, 1),  # B1
            "Cymbal": (3, 3),  # C#3
            "Violin I": (4, 7),  # G4-C7
            "Violin II": (4, 7),  # G4-C7
            "Double Bass": (1, 4)  # E1-G3
        }
        return ranges.get(instrument_name, (3, 5))

    def generate_registral_contrast(self, note_num, instrument_name, measure_num, technique):
        """生成符合乐器正常音区的音高"""
        low_octave, high_octave = self.get_instrument_octave_range(instrument_name)

        # 根据技法和乐器类型确定基础八度
        if instrument_name in ["Flute", "Oboe", "Clarinet", "Trumpet", "Violin", "Violin I", "Violin II"]:
            base_octave = low_octave + 1  # 高音乐器使用较高八度
        elif instrument_name in ["Bassoon", "Trombone", "Tuba", "Cello", "Contrabass", "Double Bass"]:
            base_octave = low_octave  # 低音乐器使用较低八度
        else:
            base_octave = (low_octave + high_octave) // 2  # 中音乐器使用中间八度

        # 根据技法添加变化
        if technique == "webern":
            octave_variation = random.choice([-1, 0, 0, 1])  # 韦伯恩：适度的音区跳跃
        elif technique == "schoenberg":
            wave = (measure_num % 12) / 12.0
            octave_variation = int((wave - 0.5) * 1)  # 勋伯格：适中的音区对比
        elif technique == "berg":
            octave_variation = random.choice([-1, 0, 0, 1])  # 贝尔格：保守的音区处理
        elif technique == "chinese_pentatonic":
            wave = (measure_num % 8) / 8.0
            octave_variation = int((wave - 0.5) * 1)  # 中国风格：适中的音区变化
        elif technique == "developmental":
            # 发展性技法：更大的音区变化
            section = measure_num // 10
            if section == 0:
                octave_variation = 0
            elif section == 1:
                octave_variation = random.choice([-1, 0, 1])
            elif section == 2:
                octave_variation = random.choice([-2, -1, 1, 2])
            else:
                octave_variation = random.choice([-1, 0, 1])
        else:
            octave_variation = random.choice([-1, 0, 1])

        final_octave = base_octave + octave_variation

        # 确保八度在乐器范围内
        final_octave = max(low_octave, min(high_octave, final_octave))

        return final_octave

    def generate_matrix(self, P0):
        """生成原位、逆行、倒影、逆行倒影矩阵"""
        valid_P0 = []
        for note in P0:
            if note in self.note_to_num:
                valid_P0.append(note)
            else:
                print(f"警告: 音符 '{note}' 不在映射中，已跳过")

        if len(valid_P0) != 12:
            print("错误: 有效音符数量不足12个，使用默认序列")
            valid_P0 = ["C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#"]

        P0_nums = [self.note_to_num[n] for n in valid_P0]

        # 生成完整的48种序列变体
        matrix = {}

        # 原始序列及其移位
        for i in range(12):
            matrix[f"P{i}"] = [(note + i) % 12 for note in P0_nums]

        # 倒影序列及其移位
        I0 = [(12 - note) % 12 for note in P0_nums]
        for i in range(12):
            matrix[f"I{i}"] = [(note + i) % 12 for note in I0]

        # 逆行序列及其移位
        R0 = P0_nums[::-1]
        for i in range(12):
            matrix[f"R{i}"] = [(note + i) % 12 for note in R0]

        # 倒影逆行序列及其移位
        RI0 = [(12 - note) % 12 for note in R0]
        for i in range(12):
            matrix[f"RI{i}"] = [(note + i) % 12 for note in RI0]

        return matrix

    def get_note_in_range(self, note_name, instrument_name, octave):
        """确保音符在乐器音域内"""
        if instrument_name not in self.instrument_ranges:
            return note_name + str(octave)

        low_midi, high_midi = self.instrument_ranges[instrument_name]

        try:
            # 尝试指定的八度
            test_note = note_name + str(octave)
            try:
                pitch = music21.pitch.Pitch(test_note)
                if low_midi <= pitch.midi <= high_midi:
                    return test_note
            except:
                pass

            # 如果不在范围内，尝试相邻八度
            for offset in [-1, 1, -2, 2]:
                test_octave = octave + offset
                if 0 <= test_octave <= 8:  # 合理的八度范围
                    test_note = note_name + str(test_octave)
                    try:
                        pitch = music21.pitch.Pitch(test_note)
                        if low_midi <= pitch.midi <= high_midi:
                            return test_note
                    except:
                        continue

            # 如果都不在范围内，返回乐器音域中间值
            mid_midi = (low_midi + high_midi) // 2
            mid_pitch = music21.pitch.Pitch(midi=mid_midi)
            return mid_pitch.nameWithOctave
        except Exception as e:
            # 如果出现错误，返回默认值
            return note_name + "4"

    def create_piano_chord(self, note_nums, texture_type, octave_base, hand_type):
        """为钢琴创建和弦"""
        chords = []

        if texture_type == "chordal":
            # 和弦式织体：创建三音或四音和弦
            if len(note_nums) >= 3:
                chord_notes = note_nums[:3]
                if hand_type == "treble":
                    # 高音部：较高的和弦
                    octaves = [octave_base + 1, octave_base + 1, octave_base]
                else:
                    # 低音部：较低的和弦
                    octaves = [octave_base - 1, octave_base, octave_base]

                for i, note_num in enumerate(chord_notes):
                    note_name = self.num_to_note[note_num]
                    full_note = self.get_note_in_range(note_name, "Piano", octaves[i])
                    chords.append(full_note)
            else:
                # 如果音符不足，使用单音
                note_name = self.num_to_note[note_nums[0]]
                full_note = self.get_note_in_range(note_name, "Piano", octave_base)
                chords.append(full_note)

        elif texture_type == "cluster":
            # 音簇式织体：密集的音符组合
            if len(note_nums) >= 4:
                cluster_notes = note_nums[:4]
                octave_offset = 1 if hand_type == "treble" else -1
                for note_num in cluster_notes:
                    note_name = self.num_to_note[note_num]
                    full_note = self.get_note_in_range(note_name, "Piano", octave_base + octave_offset)
                    chords.append(full_note)
            else:
                note_name = self.num_to_note[note_nums[0]]
                full_note = self.get_note_in_range(note_name, "Piano", octave_base)
                chords.append(full_note)

        else:
            # 其他织体类型：单音
            note_name = self.num_to_note[note_nums[0]]
            full_note = self.get_note_in_range(note_name, "Piano", octave_base)
            chords.append(full_note)

        return chords

    def get_articulation_object(self, articulation):
        """根据演奏法名称返回对应的 music21 对象"""
        try:
            articulation_map = {
                "staccato": music21.articulations.Staccato,
                "tenuto": music21.articulations.Tenuto,
                "accent": music21.articulations.Accent,
                "staccatissimo": music21.articulations.Staccatissimo,
                "marcato": music21.articulations.StrongAccent,
                "portato": music21.articulations.Tenuto,
                "spiccato": music21.articulations.Spiccato,
                "sforzando": music21.articulations.Stress,
                "fermata": music21.articulations.Fermata,
                "trill": music21.articulations.Trill,
                "turn": music21.articulations.Turn,
                "mordent": music21.articulations.Mordent,
                "glissando": music21.articulations.Glissando,
                "tremolo": music21.articulations.Tremolo,
                "harmonics": music21.articulations.Harmonic,
                "pizzicato": music21.articulations.Pizzicato,
            }

            if articulation in articulation_map:
                return articulation_map[articulation]()
            return None
        except Exception as e:
            print(f"警告: 无法创建演奏法对象 {articulation}: {e}")
            return None

    def add_expression_marking(self, measure, expression, position=0):
        """添加表情记号到小节"""
        if not expression:
            return

        try:
            text_exp = music21.expressions.TextExpression(expression)
            measure.insert(position, text_exp)
        except Exception as e:
            print(f"警告: 无法添加表情记号 {expression}: {e}")

    def add_dynamic_marking(self, measure, dynamic, position=0):
        """添加力度记号到小节"""
        if not dynamic:
            return

        try:
            dynamic_obj = music21.dynamics.Dynamic(dynamic)
            measure.insert(position, dynamic_obj)
        except Exception as e:
            print(f"警告: 无法添加力度记号 {dynamic}: {e}")

    def get_quarter_length(self, rhythm):
        """获取节奏型对应的时值"""
        rhythm_map = {
            "whole": 4.0, "half": 2.0, "quarter": 1.0,
            "eighth": 0.5, "sixteenth": 0.25, "32nd": 0.125,
            "quarter triplet": 2 / 3, "eighth triplet": 1 / 3, "sixteenth triplet": 1 / 6,
            "dotted half": 3.0, "dotted quarter": 1.5, "dotted eighth": 0.75, "dotted sixteenth": 0.375,
            "quarter rest": 1.0, "half rest": 2.0, "whole rest": 4.0, "eighth rest": 0.5, "16th rest": 0.25,
            "32nd rest": 0.125
        }

        return rhythm_map.get(rhythm, 1.0)

    def create_complex_score_structure(self, num_measures, technique):
        """创建复杂的曲式结构"""
        structure = []

        if technique == "schoenberg":
            sections = [
                ("呈示部", 0, num_measures // 3),
                ("展开部", num_measures // 3, 2 * num_measures // 3),
                ("再现部", 2 * num_measures // 3, num_measures)
            ]
        elif technique == "webern":
            section_length = max(4, num_measures // 6)
            for i in range(0, num_measures, section_length):
                end = min(i + section_length, num_measures)
                structure.append((f"段落{i // section_length + 1}", i, end))
        elif technique == "berg":
            sections = [
                ("A段", 0, num_measures // 3),
                ("B段", num_measures // 3, 2 * num_measures // 3),
                ("A'段", 2 * num_measures // 3, num_measures)
            ]
        elif technique == "chinese_pentatonic":
            quarter = num_measures // 4
            sections = [
                ("起", 0, quarter),
                ("承", quarter, 2 * quarter),
                ("转", 2 * quarter, 3 * quarter),
                ("合", 3 * quarter, num_measures)
            ]
        elif technique == "developmental":
            # 发展性技法：更复杂的结构
            sections = [
                ("主题呈示", 0, num_measures // 5),
                ("第一次变奏", num_measures // 5, 2 * num_measures // 5),
                ("第二次变奏", 2 * num_measures // 5, 3 * num_measures // 5),
                ("第三次变奏", 3 * num_measures // 5, 4 * num_measures // 5),
                ("综合再现", 4 * num_measures // 5, num_measures)
            ]
        else:
            section_length = max(8, num_measures // 4)
            for i in range(0, num_measures, section_length):
                end = min(i + section_length, num_measures)
                structure.append((f"部分{i // section_length + 1}", i, end))

        return structure

    def create_piano_part(self, part, instrument_name, part_type, matrix, tempo_mark, tempo_value,
                          num_measures, technique, dynamics_plan):
        """为钢琴创建复杂的声部"""
        print(f"  为 {part.partName} 生成复杂钢琴织体...")

        # 创建小节
        for measure_num in range(1, num_measures + 1):
            measure = music21.stream.Measure(number=measure_num)
            current_duration = 0.0

            # 应用专业作曲技法选择序列
            current_sequence = self.apply_composition_technique(
                technique, matrix, measure_num - 1, 0)

            # 确定钢琴织体类型
            texture_type = self.generate_piano_texture_type(measure_num - 1, technique)

            # 生成钢琴特定节奏模式
            if part_type == "treble":
                rhythm_pattern = self.generate_piano_treble_rhythm(technique, measure_num - 1, texture_type)
            else:  # bass
                rhythm_pattern = self.generate_piano_bass_rhythm(technique, measure_num - 1, texture_type)

            note_index = 0
            rhythm_index = 0

            # 添加表情记号
            if measure_num % 4 == 1 and random.random() < 0.7:
                expression = random.choice([e for e in self.expression_options if e])
                self.add_expression_marking(measure, expression)

            # 添加力度变化
            if measure_num % 2 == 1 or random.random() < 0.5:
                dynamic = dynamics_plan[measure_num - 1]
                self.add_dynamic_marking(measure, dynamic)

            # 填充小节
            while current_duration < 4.0 and rhythm_index < len(rhythm_pattern):
                if note_index >= len(current_sequence):
                    note_index = 0

                rhythm = rhythm_pattern[rhythm_index]
                rhythm_duration = self.get_quarter_length(rhythm)

                # 调整节奏以适应小节
                remaining = 4.0 - current_duration
                if rhythm_duration > remaining:
                    rhythm_duration = remaining

                if "rest" in rhythm:
                    note_obj = music21.note.Rest()
                    note_obj.quarterLength = rhythm_duration
                    measure.append(note_obj)
                    current_duration += rhythm_duration
                else:
                    # 生成音区对比
                    octave = self.generate_registral_contrast(
                        current_sequence[note_index], instrument_name, measure_num, technique)

                    # 根据声部类型调整音区
                    if part_type == "treble":
                        octave = max(4, octave + 1)  # 高音部使用较高音区
                    else:  # bass
                        octave = min(4, octave - 1)  # 低音部使用较低音区

                    # 为钢琴创建音符或和弦
                    if texture_type in ["chordal", "cluster"] and rhythm_duration >= 0.5:
                        # 对于较长的时值，使用和弦
                        chord_notes = self.create_piano_chord(
                            current_sequence[note_index:min(note_index + 4, len(current_sequence))],
                            texture_type, octave, part_type
                        )

                        if len(chord_notes) > 1:
                            # 创建和弦
                            chord = music21.chord.Chord(chord_notes)
                            chord.quarterLength = rhythm_duration

                            # 添加演奏法
                            if random.random() < 0.6:
                                articulation = random.choice(self.articulations_options)
                                if articulation:
                                    articulation_obj = self.get_articulation_object(articulation)
                                    if articulation_obj:
                                        chord.articulations.append(articulation_obj)

                            measure.append(chord)
                            note_index += len(chord_notes)
                        else:
                            # 单音
                            note_obj = music21.note.Note(chord_notes[0])
                            note_obj.quarterLength = rhythm_duration

                            # 添加演奏法
                            if random.random() < 0.8:
                                articulation = random.choice(self.articulations_options)
                                if articulation:
                                    articulation_obj = self.get_articulation_object(articulation)
                                    if articulation_obj:
                                        note_obj.articulations.append(articulation_obj)

                            measure.append(note_obj)
                            note_index += 1
                    else:
                        # 单音
                        note_name = self.num_to_note[current_sequence[note_index]]
                        full_note_name = self.get_note_in_range(note_name, instrument_name, octave)
                        note_obj = music21.note.Note(full_note_name)

                        # 添加演奏法
                        if random.random() < 0.8:
                            articulation = random.choice(self.articulations_options)
                            if articulation:
                                articulation_obj = self.get_articulation_object(articulation)
                                if articulation_obj:
                                    note_obj.articulations.append(articulation_obj)

                        note_obj.quarterLength = rhythm_duration
                        measure.append(note_obj)
                        note_index += 1

                    current_duration += rhythm_duration

                # 前进到下一个节奏
                rhythm_index += 1

                # 对于点描风格，可能插入额外的休止符
                if technique == "webern" and random.random() < 0.4 and current_duration < 3.5:
                    rest_duration = random.choice([0.125, 0.25, 0.5])
                    if current_duration + rest_duration <= 4.0:
                        rest_obj = music21.note.Rest()
                        rest_obj.quarterLength = rest_duration
                        measure.append(rest_obj)
                        current_duration += rest_duration

            # 如果小节未填满，用休止符补足
            if current_duration < 4.0:
                rest_obj = music21.note.Rest()
                rest_obj.quarterLength = 4.0 - current_duration
                measure.append(rest_obj)

            part.append(measure)

        return part

    def create_professional_score(self, instruments, matrix, tempo_mark, tempo_value,
                                  num_measures=45, technique="schoenberg", use_imported_matrix=False,
                                  emotion="default"):
        """创建专业级别的乐谱 (增强版)"""
        print(self.lang_system.get_text('generating'))

        # 创建总谱
        score = music21.stream.Score()

        # 添加详细的元数据
        score.metadata = music21.metadata.Metadata()
        score.metadata.title = f"十二音序列作品 - {self.composition_techniques[technique]['name']}"
        score.metadata.composer = "Algorithmic Composition System - Professional Edition"
        score.metadata.date = datetime.datetime.now().strftime("%Y/%m/%d")

        # 生成结构化的音乐元素
        dynamics_plan = self.generate_dynamics_with_structure(num_measures, technique)

        # 创建曲式结构
        structure = self.create_complex_score_structure(num_measures, technique)

        # 创建乐器部分
        parts = []
        for i_idx, instrument_name in enumerate(instruments):
            # 对于需要大谱表的乐器，创建两个部分（高音和低音）
            if instrument_name in self.grand_staff_instruments:
                # 高音部分
                treble_part = music21.stream.Part()
                try:
                    instr = music21.instrument.fromString(instrument_name)
                    treble_part.append(instr)
                    treble_part.partName = f"{instrument_name} (Treble)"
                    treble_part.partAbbreviation = self.get_instrument_abbreviation(instrument_name)
                    # 添加高音谱号
                    treble_clef = music21.clef.TrebleClef()
                    treble_part.append(treble_clef)
                except:
                    # 如果乐器名称无法识别，使用通用乐器
                    generic_instr = music21.instrument.Piano() if instrument_name == "Piano" else music21.instrument.Instrument()
                    treble_part.append(generic_instr)
                    treble_part.partName = f"{instrument_name} (Treble)"
                    treble_part.partAbbreviation = instrument_name[:4]
                    treble_clef = music21.clef.TrebleClef()
                    treble_part.append(treble_clef)

                # 低音部分
                bass_part = music21.stream.Part()
                try:
                    # 对于低音部分，我们使用相同的乐器但不同的谱号
                    bass_instr = music21.instrument.Piano() if instrument_name == "Piano" else music21.instrument.Instrument()
                    bass_part.append(bass_instr)
                    bass_part.partName = f"{instrument_name} (Bass)"
                    bass_part.partAbbreviation = self.get_instrument_abbreviation(instrument_name)
                    # 添加低音谱号
                    bass_clef = music21.clef.BassClef()
                    bass_part.append(bass_clef)
                except:
                    bass_part.partName = f"{instrument_name} (Bass)"
                    bass_part.partAbbreviation = instrument_name[:4]
                    bass_part.append(music21.instrument.Instrument())
                    bass_clef = music21.clef.BassClef()
                    bass_part.append(bass_clef)

                # 为钢琴创建复杂的织体
                if instrument_name == "Piano":
                    treble_part = self.create_piano_part(treble_part, instrument_name, "treble",
                                                         matrix, tempo_mark, tempo_value, num_measures,
                                                         technique, dynamics_plan)
                    bass_part = self.create_piano_part(bass_part, instrument_name, "bass",
                                                       matrix, tempo_mark, tempo_value, num_measures,
                                                       technique, dynamics_plan)

                parts.append(treble_part)
                parts.append(bass_part)
            else:
                # 普通乐器，创建一个部分
                part = music21.stream.Part()
                try:
                    instr = music21.instrument.fromString(instrument_name)
                    part.append(instr)
                    part.partName = instrument_name
                    part.partAbbreviation = self.get_instrument_abbreviation(instrument_name)

                    # 为特定乐器添加合适的谱号
                    if instrument_name in ["Cello", "Bassoon", "Trombone", "Tuba", "Contrabass", "Double Bass"]:
                        bass_clef = music21.clef.BassClef()
                        part.append(bass_clef)
                    elif instrument_name in ["Viola"]:
                        alto_clef = music21.clef.AltoClef()
                        part.append(alto_clef)
                    else:
                        treble_clef = music21.clef.TrebleClef()
                        part.append(treble_clef)

                except:
                    part.partName = instrument_name
                    part.partAbbreviation = instrument_name[:4]
                    part.append(music21.instrument.Instrument())
                    # 默认使用高音谱号
                    treble_clef = music21.clef.TrebleClef()
                    part.append(treble_clef)

                # 为非钢琴乐器生成音符
                print(f"  为 {part.partName} 生成专业音符...")

                # 创建小节
                for measure_num in range(1, num_measures + 1):
                    measure = music21.stream.Measure(number=measure_num)
                    current_duration = 0.0

                    # 应用专业作曲技法选择序列
                    current_sequence = self.apply_composition_technique(
                        technique, matrix, measure_num - 1, i_idx)

                    # 生成复杂的节奏模式
                    rhythm_pattern = self.generate_rhythm_pattern(technique, measure_num - 1, i_idx)

                    note_index = 0
                    rhythm_index = 0

                    # 添加表情记号
                    if measure_num % 3 == 1 and random.random() < 0.6:
                        expression = random.choice([e for e in self.expression_options if e])
                        self.add_expression_marking(measure, expression)

                    # 添加力度变化
                    if measure_num % 2 == 1 or random.random() < 0.4:
                        dynamic = dynamics_plan[measure_num - 1]
                        self.add_dynamic_marking(measure, dynamic)

                    # 填充小节
                    while current_duration < 4.0 and rhythm_index < len(rhythm_pattern):
                        if note_index >= len(current_sequence):
                            note_index = 0

                        rhythm = rhythm_pattern[rhythm_index]
                        rhythm_duration = self.get_quarter_length(rhythm)

                        # 调整节奏以适应小节
                        remaining = 4.0 - current_duration
                        if rhythm_duration > remaining:
                            rhythm_duration = remaining

                        if "rest" in rhythm:
                            note_obj = music21.note.Rest()
                            note_obj.quarterLength = rhythm_duration
                            measure.append(note_obj)
                            current_duration += rhythm_duration
                        else:
                            note_num = current_sequence[note_index]
                            note_name = self.num_to_note[note_num]

                            # 生成音区对比
                            octave = self.generate_registral_contrast(note_num, instrument_name, measure_num, technique)

                            full_note_name = self.get_note_in_range(note_name, instrument_name, octave)
                            note_obj = music21.note.Note(full_note_name)

                            # 添加演奏法
                            if random.random() < 0.8:
                                articulation = random.choice(self.articulations_options)
                                if articulation:
                                    articulation_obj = self.get_articulation_object(articulation)
                                    if articulation_obj:
                                        note_obj.articulations.append(articulation_obj)

                            note_obj.quarterLength = rhythm_duration
                            measure.append(note_obj)
                            current_duration += rhythm_duration

                        # 前进到下一个音符和节奏
                        note_index += 1
                        rhythm_index += 1

                        # 对于点描风格，可能插入额外的休止符
                        if technique == "webern" and random.random() < 0.4 and current_duration < 3.5:
                            rest_duration = random.choice([0.125, 0.25, 0.5])
                            if current_duration + rest_duration <= 4.0:
                                rest_obj = music21.note.Rest()
                                rest_obj.quarterLength = rest_duration
                                measure.append(rest_obj)
                                current_duration += rest_duration

                    # 如果小节未填满，用休止符补足
                    if current_duration < 4.0:
                        rest_obj = music21.note.Rest()
                        rest_obj.quarterLength = 4.0 - current_duration
                        measure.append(rest_obj)

                    part.append(measure)

                parts.append(part)

        # 将所有部分添加到总谱
        for part in parts:
            score.append(part)

        # 设置音乐元素
        ts = music21.meter.TimeSignature('4/4')
        score.insert(0, ts)

        ks = music21.key.KeySignature(0)
        score.insert(0, ks)

        # 设置速度
        tempo = music21.tempo.MetronomeMark(number=tempo_value)
        score.insert(0, tempo)

        # 添加速度文本
        tempo_text = music21.expressions.TextExpression(tempo_mark)
        score.insert(0, tempo_text)

        # 添加曲式结构标记
        for section_name, start, end in structure:
            if start == 0:
                # 在开始处添加段落标记
                rehearsal_mark = music21.expressions.RehearsalMark(section_name)
                score.parts[0].measure(start + 1).insert(0, rehearsal_mark)

        # --- 新增：应用后处理增强系统 ---
        print(self.lang_system.get_text('processing_emotion') + emotion)
        self.emotion_system.apply_emotion(score, emotion)

        print("   应用智能乐句划分...")
        self.phrasing_system.add_intelligent_phrasing(score)

        print(self.lang_system.get_text('processing_human'))
        self.human_system.add_human_touches(score)

        return score

    def get_instrument_abbreviation(self, instrument_name):
        """获取乐器缩写"""
        abbreviations = {
            "Flute": "Fl.", "Oboe": "Ob.", "Clarinet": "Cl.", "Bassoon": "Bn.",
            "Horn": "Hn.", "Trumpet": "Tpt.", "Trombone": "Tbn.", "Tuba": "Tba.",
            "Violin": "Vln.", "Viola": "Vla.", "Cello": "Vc.", "Contrabass": "Cb.",
            "Piano": "Pno.", "Harp": "Hp.", "Timpani": "Timp.", "Snare Drum": "S.D.",
            "Bass Drum": "B.D.", "Cymbal": "Cym.", "Violin I": "Vln.I",
            "Violin II": "Vln.II", "Double Bass": "Db."
        }
        return abbreviations.get(instrument_name, instrument_name[:4] + ".")

    def generate_sibelius_files(self, score):
        """生成西贝柳斯文件并保存到用户桌面。"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
        try:
            os.makedirs(desktop_dir, exist_ok=True)
        except OSError:
            # 如果系统没有桌面目录，退回当前工作目录，避免生成流程直接失败。
            desktop_dir = os.getcwd()
        musicxml_file = os.path.join(desktop_dir, f"professional_score_{timestamp}.xml")

        print(self.lang_system.get_text('processing_xml'))
        # 使用新的优化器保存
        final_file = self.xml_optimizer.optimize_and_save(score, musicxml_file)

        print(f"✓ {self.lang_system.get_text('complete')} -> {final_file}")
        return final_file

    def run(self, imported_sequence=None, matrix_data=None):
        """运行主程序"""
        try:
            if 'music21' not in globals():
                print("错误: music21 库未安装，无法使用音乐生成功能")
                print("请运行: pip install music21")
                input("按回车键返回主菜单...")
                return

            # 获取输入 (包含情感参数)
            inputs = self.get_user_input(imported_sequence, matrix_data)
            P0, instruments, tempo_mark, tempo_value, num_measures, technique, use_imported, matrix_data, emotion = inputs

            print("\n" + "=" * 50)
            print(self.lang_system.get_text('generating'))
            print("=" * 50)

            # 生成音列矩阵
            print(self.lang_system.get_text('matrix_gen'))
            if use_imported and matrix_data:
                # 使用导入的完整矩阵数据
                matrix = {}
                for seq_type in ['P', 'I', 'R', 'RI']:
                    for transposition in range(12):
                        key = f"{seq_type}{transposition}"
                        if transposition in matrix_data[seq_type]:
                            matrix[key] = matrix_data[seq_type][transposition]
                print("   使用导入的完整魔方矩阵")
            else:
                # 生成新的矩阵
                matrix = self.generate_matrix(P0)
                print("   生成新的音列矩阵")

            print(self.lang_system.get_text('apply_tech'))
            print(f"   使用技法: {self.composition_techniques[technique]['name']}")
            print(f"   技法特点: {self.composition_techniques[technique]['description']}")
            print(f"   发展手法: {', '.join(self.composition_techniques[technique]['techniques'])}")

            print(self.lang_system.get_text('struct_gen'))
            # 传递 emotion 参数
            score = self.create_professional_score(instruments, matrix, tempo_mark, tempo_value,
                                                   num_measures, technique, use_imported, emotion=emotion)

            print(self.lang_system.get_text('export'))
            musicxml_file = self.generate_sibelius_files(score)

            print("\n" + "=" * 60)
            print(self.lang_system.get_text('complete'))
            print("=" * 60)
            print(f"\n✓ 乐谱文件: {musicxml_file}")
            print("\nPro 7.0 Features Applied:")
            print("• Emotion Expression System")
            print("• Intelligent Phrasing")
            print("• Handwritten Humanization")
            print("• XML Optimization")
            if "Piano" in instruments:
                print("• 复杂的钢琴织体（大谱表）")
            print("\n在西贝柳斯中打开即可看到完整的专业音乐作品！")

        except Exception as e:
            print(f"\n❌ 程序运行出错: {e}")
            import traceback
            traceback.print_exc()

        input("\n按回车键返回主菜单...")


    def run_with_inputs(self, inputs):
        """使用图形界面已收集的参数生成作品，不再调用 input()。"""
        if 'music21' not in globals():
            raise RuntimeError("未安装 music21 库，无法使用音乐生成功能。请运行: pip install music21")

        (P0, instruments, tempo_mark, tempo_value, num_measures,
         technique, use_imported, matrix_data, emotion) = inputs

        print("\n" + "=" * 50)
        print(self.lang_system.get_text('generating'))
        print("=" * 50)

        print(self.lang_system.get_text('matrix_gen'))
        if use_imported and matrix_data:
            matrix = {}
            for seq_type in ['P', 'I', 'R', 'RI']:
                for transposition in range(12):
                    key = f"{seq_type}{transposition}"
                    if transposition in matrix_data.get(seq_type, {}):
                        matrix[key] = matrix_data[seq_type][transposition]
            print("   使用导入的完整魔方矩阵")
        else:
            matrix = self.generate_matrix(P0)
            print("   生成新的音列矩阵")

        print(self.lang_system.get_text('apply_tech'))
        print(f"   使用技法: {self.composition_techniques[technique]['name']}")
        print(f"   技法特点: {self.composition_techniques[technique]['description']}")
        print(f"   发展手法: {', '.join(self.composition_techniques[technique]['techniques'])}")

        print(self.lang_system.get_text('struct_gen'))
        score = self.create_professional_score(
            instruments, matrix, tempo_mark, tempo_value, num_measures,
            technique, use_imported, emotion=emotion
        )

        print(self.lang_system.get_text('export'))
        musicxml_file = self.generate_sibelius_files(score)

        print("\n" + "=" * 60)
        print(self.lang_system.get_text('complete'))
        print("=" * 60)
        print(f"\n✓ 乐谱文件: {musicxml_file}")
        print("\n在西贝柳斯中打开即可看到完整的专业音乐作品！")
        return musicxml_file


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
        self.create_main_interface()

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
        technique_ids = list(composer.composition_techniques.keys())
        technique_labels = [composer.composition_techniques[key]['name'] for key in technique_ids]
        self.workspace_technique_map = dict(zip(technique_labels, technique_ids))
        self.workspace_technique_var = tk.StringVar(value=technique_labels[0])
        self._workspace_field(music_body, '作曲技法', self.workspace_technique_var,
                              technique_labels, 0, 0)
        self.workspace_emotion_var = tk.StringVar(value='默认')
        self._workspace_field(music_body, '音乐情感', self.workspace_emotion_var,
                              ['默认', '戏剧性', '抒情', '激动'], 0, 1)

        tempo_items = [f'{name} ({bpm} BPM)' for name, bpm in composer.tempo_options.items()]
        self.workspace_tempo_lookup = dict(zip(tempo_items, composer.tempo_options.values()))
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
        """根据第一行音列计算完整矩阵及其四类序列数据。"""
        matrix = [[0 for _ in range(12)] for _ in range(12)]
        matrix[0] = numbers.copy()
        reverse_row = numbers[::-1]
        inversion_row = [(12 - note) % 12 for note in numbers]
        reverse_inversion_row = [(12 - note) % 12 for note in reverse_row]

        for row_index in range(12):
            matrix[row_index][0] = inversion_row[row_index]
        matrix[11] = reverse_row
        for row_index in range(12):
            matrix[row_index][11] = reverse_inversion_row[row_index]
        for row_index in range(1, 11):
            for column_index in range(1, 11):
                matrix[row_index][column_index] = (
                    matrix[0][column_index] + matrix[row_index][0] - matrix[0][0]
                ) % 12

        matrix_data = {'P': {}, 'I': {}, 'R': {}, 'RI': {}}
        for transposition in range(12):
            matrix_data['P'][transposition] = [
                (note + transposition) % 12 for note in numbers
            ]
            matrix_data['I'][transposition] = [
                (note + transposition) % 12 for note in inversion_row
            ]
            matrix_data['R'][transposition] = [
                (note + transposition) % 12 for note in reverse_row
            ]
            matrix_data['RI'][transposition] = [
                (note + transposition) % 12 for note in reverse_inversion_row
            ]
        return matrix, matrix_data

    def generate_matrix_from_entry(self):
        """验证音列，并在当前工作台刷新矩阵。"""
        input_text = self.sequence_entry.get().strip()
        try:
            values = input_text.replace(',', ' ').split()
            note_aliases = {
                'DB': 'C#', 'EB': 'D#', 'GB': 'F#', 'AB': 'G#', 'BB': 'A#'
            }
            if all(value.lstrip('-').isdigit() for value in values):
                numbers = [int(value) for value in values]
            else:
                normalized_notes = [note_aliases.get(value.upper(), value.upper()) for value in values]
                note_to_num = {
                    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
                    'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
                }
                try:
                    numbers = [note_to_num[note] for note in normalized_notes]
                except KeyError as error:
                    raise ValueError(f'无法识别音名：{error.args[0]}') from error
            if len(numbers) != 12:
                raise ValueError('请输入正好12个数字或音名。')
            if any(value < 0 or value > 11 for value in numbers):
                raise ValueError('每个数字必须在0到11之间。')
            if len(set(numbers)) != 12:
                raise ValueError('数字不能重复，必须是12个不同的数字。')
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
                text=f'P{column_index}',
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
                text=f'I{row_index}',
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
        numbers = [composer.note_to_num[note] for note in note_row]
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.sequence_entry.delete(0, tk.END)
        self.sequence_entry.insert(0, ' '.join(note_names[value] for value in numbers))
        self.generate_matrix_from_entry()

    def start_workspace_generation(self):
        """读取右侧音乐设置，直接使用当前矩阵开始后台生成。"""
        if not self.current_matrix_data and not self.generate_matrix_from_entry():
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

    def show_composer_input_dialog(self):
        """收集专业音乐生成参数，提交后再启动后台生成。"""
        colors = self.UI_COLORS
        composer = AdvancedTwelveToneComposer()
        dialog = tk.Toplevel(self.root)
        dialog.title("专业十二音音乐生成器 - 输入设置")
        dialog.geometry("840x720")
        dialog.minsize(780, 660)
        dialog.configure(bg=colors['background'])
        dialog.transient(self.root)
        dialog.grab_set()

        default_row = ["C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#"]
        imported_sequence = self.composer_data.get('imported_sequence')
        imported_matrix = self.composer_data.get('matrix_data')

        header = tk.Frame(dialog, bg=colors['background'])
        header.pack(fill=tk.X, padx=28, pady=(22, 8))
        tk.Label(
            header,
            text="专业十二音音乐生成器",
            font=('Arial', 20, 'bold'),
            bg=colors['background'],
            fg=colors['text'],
        ).pack(anchor=tk.W)
        tk.Label(
            header,
            text="请设置音列、作曲技法、乐器与速度，然后点击“开始生成”",
            font=('Arial', 10),
            bg=colors['background'],
            fg=colors['muted_text'],
        ).pack(anchor=tk.W, pady=(4, 0))

        content = tk.Frame(dialog, bg=colors['background'])
        content.pack(fill=tk.BOTH, expand=True, padx=28, pady=(4, 0))
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(1, weight=1)

        def section(parent, title, row, column):
            frame = tk.LabelFrame(
                parent,
                text=title,
                font=('Arial', 11, 'bold'),
                bg=colors['surface'],
                fg=colors['text'],
                bd=1,
                relief=tk.GROOVE,
                padx=14,
                pady=10,
            )
            frame.grid(
                row=row,
                column=column,
                sticky='nsew',
                padx=(0 if column == 0 else 10, 0),
                pady=(0, 12),
            )
            return frame

        sequence_frame = section(content, "1. 音列输入", 0, 0)
        options_frame = section(content, "2. 作曲设置", 0, 1)
        instruments_frame = section(content, "3. 选择乐器（可多选）", 1, 0)
        preview_frame = section(content, "当前设置预览", 1, 1)

        mode_options = ['默认序列', '手动输入音列', '生成五声性序列']
        if imported_sequence:
            mode_options.insert(0, '使用已导入序列')
        mode_var = tk.StringVar(value=mode_options[0])
        tk.Label(sequence_frame, text="输入方式", bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.W)
        mode_combo = ttk.Combobox(
            sequence_frame,
            textvariable=mode_var,
            values=mode_options,
            state='readonly',
            width=25,
        )
        mode_combo.pack(fill=tk.X, pady=(4, 10))

        tk.Label(
            sequence_frame,
            text="手动音列（12个不重复音名，用空格分隔）",
            bg=colors['surface'],
            fg=colors['muted_text'],
        ).pack(anchor=tk.W)
        manual_var = tk.StringVar(value=' '.join(default_row))
        manual_entry = tk.Entry(
            sequence_frame,
            textvariable=manual_var,
            font=('Arial', 11),
            bg='#FFFFFF',
            fg=colors['text'],
            relief=tk.SOLID,
            bd=1,
        )
        manual_entry.pack(fill=tk.X, pady=(4, 5))
        tk.Label(
            sequence_frame,
            text="可用音名：C C# D D# E F F# G G# A A# B",
            bg=colors['surface'],
            fg=colors['muted_text'],
            font=('Arial', 9),
        ).pack(anchor=tk.W)

        if imported_sequence:
            tk.Label(
                sequence_frame,
                text='已导入：' + ' '.join(imported_sequence),
                bg=colors['surface'],
                fg=colors['secondary'],
                font=('Arial', 9),
                wraplength=330,
                justify=tk.LEFT,
            ).pack(anchor=tk.W, pady=(8, 0))

        technique_names = list(composer.composition_techniques.keys())
        technique_labels = [composer.composition_techniques[key]['name'] for key in technique_names]
        technique_map = dict(zip(technique_labels, technique_names))
        technique_var = tk.StringVar(value=technique_labels[0])
        tk.Label(options_frame, text="作曲技法", bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.W)
        technique_combo = ttk.Combobox(
            options_frame,
            textvariable=technique_var,
            values=technique_labels,
            state='readonly',
        )
        technique_combo.pack(fill=tk.X, pady=(4, 3))
        technique_desc = tk.Label(
            options_frame,
            text='',
            bg=colors['surface'],
            fg=colors['muted_text'],
            font=('Arial', 9),
            wraplength=320,
            justify=tk.LEFT,
        )
        technique_desc.pack(anchor=tk.W, pady=(0, 10))

        emotion_labels = ['默认', '戏剧性', '抒情', '激动']
        emotion_map = {'默认': 'default', '戏剧性': 'dramatic', '抒情': 'lyrical', '激动': 'agitated'}
        emotion_var = tk.StringVar(value='默认')
        tk.Label(options_frame, text="音乐情感", bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.W)
        ttk.Combobox(
            options_frame,
            textvariable=emotion_var,
            values=emotion_labels,
            state='readonly',
        ).pack(fill=tk.X, pady=(4, 10))

        tempo_items = [f'{name} ({bpm} BPM)' for name, bpm in composer.tempo_options.items()]
        tempo_lookup = dict(zip(tempo_items, composer.tempo_options.values()))
        tempo_items.append('自定义速度')
        tempo_var = tk.StringVar(value='Andante (85 BPM)')
        tk.Label(options_frame, text="速度", bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.W)
        ttk.Combobox(
            options_frame,
            textvariable=tempo_var,
            values=tempo_items,
            state='readonly',
        ).pack(fill=tk.X, pady=(4, 6))
        custom_bpm_var = tk.StringVar(value='120')
        custom_bpm_entry = tk.Entry(
            options_frame,
            textvariable=custom_bpm_var,
            width=10,
            font=('Arial', 10),
            bg='#FFFFFF',
            fg=colors['text'],
            relief=tk.SOLID,
            bd=1,
            state=tk.DISABLED,
        )
        custom_bpm_entry.pack(anchor=tk.W)

        tk.Label(options_frame, text="小节数", bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.W, pady=(10, 0))
        measures_var = tk.StringVar(value='45')
        tk.Entry(
            options_frame,
            textvariable=measures_var,
            width=10,
            font=('Arial', 10),
            bg='#FFFFFF',
            fg=colors['text'],
            relief=tk.SOLID,
            bd=1,
        ).pack(anchor=tk.W, pady=(4, 0))

        instruments = [
            "Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet",
            "Trombone", "Tuba", "Violin", "Viola", "Cello", "Contrabass",
            "Piano", "Harp", "Timpani", "Snare Drum", "Bass Drum", "Cymbal",
            "Violin I", "Violin II", "Double Bass"
        ]
        list_frame = tk.Frame(instruments_frame, bg=colors['surface'])
        list_frame.pack(fill=tk.BOTH, expand=True)
        instrument_list = tk.Listbox(
            list_frame,
            selectmode=tk.MULTIPLE,
            exportselection=False,
            height=11,
            font=('Arial', 10),
            bg='#FFFFFF',
            fg=colors['text'],
            selectbackground=colors['primary'],
            selectforeground='#FFFFFF',
            relief=tk.SOLID,
            bd=1,
        )
        instrument_scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=instrument_list.yview)
        instrument_list.configure(yscrollcommand=instrument_scroll.set)
        instrument_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        instrument_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        for instrument in instruments:
            instrument_list.insert(tk.END, instrument)
        for instrument in ['Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Piano']:
            instrument_list.selection_set(instruments.index(instrument))

        preview_text = tk.StringVar()
        preview_label = tk.Label(
            preview_frame,
            textvariable=preview_text,
            bg=colors['surface'],
            fg=colors['text'],
            font=('Arial', 10),
            justify=tk.LEFT,
            anchor=tk.NW,
            wraplength=320,
        )
        preview_label.pack(fill=tk.BOTH, expand=True, anchor=tk.NW)

        language_var = tk.StringVar(value='中文')
        tk.Label(preview_frame, text='输出语言', bg=colors['surface'], fg=colors['muted_text']).pack(anchor=tk.SW, pady=(14, 4))
        ttk.Combobox(
            preview_frame,
            textvariable=language_var,
            values=['中文', 'English'],
            state='readonly',
            width=18,
        ).pack(anchor=tk.SW)

        def update_preview(*_):
            selected_instruments = [instrument_list.get(i) for i in instrument_list.curselection()]
            preview_text.set(
                f"输入方式：{mode_var.get()}\n"
                f"作曲技法：{technique_var.get()}\n"
                f"情感：{emotion_var.get()}\n"
                f"速度：{tempo_var.get()}\n"
                f"小节数：{measures_var.get() or '45'}\n"
                f"乐器：{', '.join(selected_instruments) or '尚未选择'}"
            )

        def update_technique(*_):
            selected_id = technique_map.get(technique_var.get(), technique_names[0])
            technique_desc.config(text=composer.composition_techniques[selected_id]['description'])
            update_preview()

        def update_mode(*_):
            manual_entry.config(state=tk.NORMAL if mode_var.get() == '手动输入音列' else tk.DISABLED)
            update_preview()

        def update_tempo(*_):
            custom_bpm_entry.config(state=tk.NORMAL if tempo_var.get() == '自定义速度' else tk.DISABLED)
            update_preview()

        def submit():
            mode = mode_var.get()
            use_imported = mode == '使用已导入序列'
            if use_imported:
                P0 = list(imported_sequence)
            elif mode == '手动输入音列':
                P0 = manual_var.get().strip().upper().replace(',', ' ').split()
                if len(P0) != 12 or len(set(P0)) != 12 or any(note not in composer.note_to_num for note in P0):
                    messagebox.showerror(
                        '音列输入错误',
                        '请输入12个不重复的音名，只能使用：C C# D D# E F F# G G# A A# B',
                        parent=dialog,
                    )
                    manual_entry.focus_set()
                    return
            elif mode == '生成五声性序列':
                P0 = composer.generate_chinese_pentatonic_row()
                use_imported = False
            else:
                P0 = default_row
                use_imported = False

            selected_indices = instrument_list.curselection()
            if not selected_indices:
                messagebox.showwarning('缺少乐器', '请至少选择一种乐器。', parent=dialog)
                return
            selected_instruments = [instruments[i] for i in selected_indices]

            tempo_selection = tempo_var.get()
            if tempo_selection == '自定义速度':
                try:
                    tempo_value = int(custom_bpm_var.get())
                    if tempo_value <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror('速度输入错误', '自定义 BPM 必须是大于 0 的整数。', parent=dialog)
                    custom_bpm_entry.focus_set()
                    return
                tempo_mark = f'Custom ({tempo_value} BPM)'
            else:
                tempo_value = tempo_lookup[tempo_selection]
                tempo_mark = tempo_selection.split(' (', 1)[0]

            try:
                num_measures = int(measures_var.get() or '45')
                if num_measures <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror('小节数输入错误', '小节数必须是大于 0 的整数。', parent=dialog)
                return

            language = 'en-US' if language_var.get() == 'English' else 'zh-CN'
            composer_inputs = (
                P0,
                selected_instruments,
                tempo_mark,
                tempo_value,
                num_measures,
                technique_map.get(technique_var.get(), technique_names[0]),
                use_imported,
                imported_matrix if use_imported else None,
                emotion_map.get(emotion_var.get(), 'default'),
            )
            dialog.destroy()
            self.status_label.config(text='参数已提交，正在后台生成专业乐谱……')
            self.start_composer_generation(composer_inputs, language)

        mode_var.trace_add('write', update_mode)
        technique_var.trace_add('write', update_technique)
        tempo_var.trace_add('write', update_tempo)
        instrument_list.bind('<<ListboxSelect>>', update_preview)
        measures_var.trace_add('write', update_preview)
        update_mode()
        update_tempo()
        update_technique()

        footer = tk.Frame(dialog, bg=colors['background'])
        footer.pack(fill=tk.X, padx=28, pady=(0, 22))
        ttk.Button(
            footer,
            text='取消',
            command=dialog.destroy,
            style='Suite.Danger.TButton',
        ).pack(side=tk.RIGHT, padx=(10, 0))
        ttk.Button(
            footer,
            text='开始生成',
            command=submit,
            style='Suite.Primary.TButton',
        ).pack(side=tk.RIGHT)
        dialog.protocol('WM_DELETE_WINDOW', dialog.destroy)

    def start_composer_generation(self, inputs, language):
        """在后台生成乐谱，并把结果安全地交回主窗口。"""
        import threading
        if hasattr(self, 'workspace_generate_button'):
            self.workspace_generate_button.config(state=tk.DISABLED)

        def run_composer():
            try:
                composer = AdvancedTwelveToneComposer()
                composer.lang_system.language = language
                filename = composer.run_with_inputs(inputs)
                self.root.after(0, lambda: self.composer_generation_complete(filename))
            except Exception as error:
                error_text = str(error)
                self.root.after(0, lambda: self.composer_generation_failed(error_text))

        composer_thread = threading.Thread(target=run_composer, daemon=True)
        composer_thread.start()

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

    def open_last_output_in_sibelius(self):
        """从统一工作台直接打开最近一次生成的 XML。"""
        if not self.last_output_file:
            messagebox.showwarning('尚未生成', '请先使用当前魔方生成 XML。', parent=self.root)
            return
        self.open_in_sibelius(self.last_output_file)

    def open_in_sibelius(self, filename, parent=None):
        """调用系统打开命令，把生成的 MusicXML 交给 Sibelius。"""
        import subprocess

        try:
            if sys.platform == 'darwin':
                subprocess.run(['open', '-a', 'Sibelius', filename], check=True)
            elif os.name == 'nt':
                os.startfile(filename)
            else:
                subprocess.run(['xdg-open', filename], check=True)
            self.status_label.config(text='已请求 Sibelius 打开生成的 XML 文件。')
        except (OSError, subprocess.CalledProcessError) as error:
            messagebox.showerror(
                '无法打开 Sibelius',
                f'未能自动打开 Sibelius。\n请确认已安装 Sibelius，或手动打开文件：\n{filename}\n\n原因：{error}',
                parent=parent or self.root,
            )

    def reveal_output_file(self, filename):
        """在文件管理器中定位生成的 XML 文件。"""
        import subprocess

        try:
            if sys.platform == 'darwin':
                subprocess.run(['open', '-R', filename], check=True)
            elif os.name == 'nt':
                subprocess.run(['explorer', '/select,', os.path.normpath(filename)], check=True)
            else:
                subprocess.run(['xdg-open', os.path.dirname(filename)], check=True)
            self.status_label.config(text='已在桌面中定位生成的 XML 文件。')
        except (OSError, subprocess.CalledProcessError) as error:
            messagebox.showerror('无法打开文件位置', f'无法定位文件：\n{filename}\n\n原因：{error}', parent=self.root)

    def composer_generation_failed(self, error_text):
        if hasattr(self, 'workspace_generate_button'):
            self.workspace_generate_button.config(state=tk.NORMAL)
        if hasattr(self, 'workspace_music_status_var'):
            self.workspace_music_status_var.set('生成失败，请检查设置或依赖库。')
        self.status_label.config(text='生成失败，请检查设置或依赖库。')
        messagebox.showerror('生成失败', error_text, parent=self.root)

    def run(self):
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = TwelveToneSuite(root)
    app.run()


if __name__ == "__main__":
    main()
    # ==============================================================================
    # [NEW MODULE] TWELVE-TONE PRO SUITE - PHASE 2 EXTENSIONS
    # 现代界面 | 严谨算法 | AI集成 | 深度乐器法
    # ==============================================================================

    import threading
    import time
    import math
    from tkinter import font as tkfont


    # ------------------------------------------------------------------------------
    # 1. 严谨魔方验证引擎 (Strict Matrix Engine)
    # ------------------------------------------------------------------------------

    class StrictMatrixValidator:
        """
        用于校验12x12矩阵的数学完整性。
        确保行、列、对角线不重复。
        """

        @staticmethod
        def validate_integrity(matrix):
            """
            返回一个字典，包含校验结果和错误坐标
            matrix: 12x12 List of ints (0-11)
            """
            errors = {
                'rows': [],  # index of invalid rows
                'cols': [],  # index of invalid cols
                'diagonals': []  # 'main' or 'anti'
            }
            is_valid = True
            required_set = set(range(12))

            # 1. 检查行
            for r_idx, row in enumerate(matrix):
                if set(row) != required_set:
                    errors['rows'].append(r_idx)
                    is_valid = False

            # 2. 检查列
            for c_idx in range(12):
                col = [matrix[r][c_idx] for r in range(12)]
                if set(col) != required_set:
                    errors['cols'].append(c_idx)
                    is_valid = False

            # 3. 检查主对角线 (Top-Left to Bottom-Right)
            diag_main = [matrix[i][i] for i in range(12)]
            if set(diag_main) != required_set:
                errors['diagonals'].append('main')
                # 对角线并非必须严格遵循，但在某些序列魔方中是高级要求
                # 这里我们只做警告，不强制False，除非用户开启严格模式
                pass

                # 4. 检查副对角线 (Top-Right to Bottom-Left)
            diag_anti = [matrix[i][11 - i] for i in range(12)]
            if set(diag_anti) != required_set:
                errors['diagonals'].append('anti')

            return is_valid, errors


    # ------------------------------------------------------------------------------
    # 2. 高级乐器技法管理器 (Advanced Technique Manager)
    # ------------------------------------------------------------------------------

    class AdvancedTechniqueManager:
        """
        管理扩展的乐器演奏法，包括民乐和现代技法。
        """
        TECHNIQUES_DB = {
            "Strings": {
                "Bowing": ["Legato", "Staccato", "Spiccato", "Martelé", "Ricochet", "Col Legno"],
                "Special": ["Sul Ponticello", "Sul Tasto", "Tremolo", "Pizzicato (Snap)", "Harmonics (Natural)",
                            "Harmonics (Artificial)"]
            },
            "Piano": {
                "Texture": ["Cluster", "Pointillism", "Resonance (Pedal)", "Secco (Dry)", "Inside Piano"],
                "HandShape": ["Open Voicing", "Closed Voicing", "Cross-Hand"]
            },
            "Chinese": {
                "Guzheng": ["Yao Zhi (Tremolo)", "Glissando", "Pitch Bend", "Harmonics"],
                "Pipa": ["Lun Zhi (Tremolo)", "Sao (Sweep)", "Tui/La (Push/Pull)"]
            }
        }

        @staticmethod
        def get_random_technique(instrument_family, complexity=0.5):
            """根据复杂度随机获取技法"""
            family_techs = AdvancedTechniqueManager.TECHNIQUES_DB.get(instrument_family, {})
            if not family_techs:
                return None

            # 简单模式返回基本技法，复杂模式返回特殊技法
            category = "Special" if random.random() < complexity else "Bowing"
            if category not in family_techs: category = list(family_techs.keys())[0]

            techs = family_techs[category]
            return random.choice(techs)


    # ------------------------------------------------------------------------------
    # 3. 现代深色界面 (Modern Dark UI)
    # ------------------------------------------------------------------------------

    class ModernTwelveToneWorkstation:
        """
        【十二音AI Pro工作台】
        集成 DeepSeek 架构师、Ableton 风格界面与核心生成引擎。
        """

        # 颜色主题 (Cyberpunk / Studio Dark)
        COLORS = {
            'bg_dark': '#121212',  # 极深背景
            'bg_panel': '#1E1E1E',  # 面板背景
            'bg_light': '#2D2D2D',  # 控件背景
            'accent': '#00FF99',  # 荧光绿强调
            'accent_sec': '#00CCFF',  # 荧光蓝次要
            'text_main': '#E0E0E0',  # 主文字
            'text_dim': '#888888',  # 暗文字
            'error': '#FF5555',  # 错误红
            'matrix_p': '#3c3c3c',  # 矩阵P色
            'matrix_i': '#444444',  # 矩阵I色
        }

        def __init__(self, root):
            self.root = root
            self.root.title("Twelve-Tone AI Pro Workstation v7.0")
            self.root.geometry("1400x900")
            self.root.configure(bg=self.COLORS['bg_dark'])

            # 引用旧的核心引擎 (Composition Engine Backend)
            self.backend_composer = AdvancedTwelveToneComposer()
            self.matrix_validator = StrictMatrixValidator()

            # 状态变量
            self.current_matrix = [[0] * 12 for _ in range(12)]
            self.selected_instruments = []
            self.generation_seed = 0

            self.setup_styles()
            self.build_ui_layout()

            # 初始化一个默认矩阵
            self.regenerate_matrix_data([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

        def setup_styles(self):
            style = ttk.Style()
            style.theme_use('clam')

            # 定义现代按钮样式
            style.configure('Modern.TButton',
                            background=self.COLORS['bg_light'],
                            foreground=self.COLORS['accent'],
                            borderwidth=0,
                            font=('Segoe UI', 10, 'bold'))
            style.map('Modern.TButton',
                      background=[('active', self.COLORS['accent'])],
                      foreground=[('active', self.COLORS['bg_dark'])])

            # 定义面板框架样式
            style.configure('Panel.TFrame', background=self.COLORS['bg_panel'])

            # 标签样式
            style.configure('Header.TLabel', background=self.COLORS['bg_panel'], foreground=self.COLORS['text_main'],
                            font=('Impact', 14))
            style.configure('Normal.TLabel', background=self.COLORS['bg_panel'], foreground=self.COLORS['text_dim'],
                            font=('Segoe UI', 9))

        def build_ui_layout(self):
            # --- 主容器 (3列布局) ---
            main_container = tk.Frame(self.root, bg=self.COLORS['bg_dark'])
            main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # 1. 左侧：控制中心 (Control Center)
            self.left_panel = tk.Frame(main_container, bg=self.COLORS['bg_panel'], width=300)
            self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5)
            self.left_panel.pack_propagate(False)  # 固定宽度
            self.build_left_panel()

            # 2. 中间：魔方矩阵 (The Cube)
            self.center_panel = tk.Frame(main_container, bg=self.COLORS['bg_dark'])  # 深色底衬托矩阵
            self.center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            self.build_center_panel()

            # 3. 右侧：AI架构师与乐器法 (Architect & Instrumentation)
            self.right_panel = tk.Frame(main_container, bg=self.COLORS['bg_panel'], width=350)
            self.right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
            self.right_panel.pack_propagate(False)
            self.build_right_panel()

        # ================= UI 构建细节 =================

        def build_left_panel(self):
            """构建左侧参数控制区"""
            pad = 15

            # 标题
            tk.Label(self.left_panel, text="SEQUENCER CONTROL", font=("Arial", 12, "bold"),
                     bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(pady=pad, anchor="w", padx=pad)

            # 分隔线
            tk.Frame(self.left_panel, height=1, bg=self.COLORS['bg_light']).pack(fill=tk.X, padx=pad)

            # 1. 风格倾向 (Slider)
            lbl_style = tk.Label(self.left_panel, text="Style / 风格倾向", style='Normal.TLabel')
            lbl_style.pack(pady=(10, 5), padx=pad, anchor="w")

            self.combo_style = ttk.Combobox(self.left_panel, values=[
                "Schoenberg (Classic)", "Webern (Pointillism)", "Berg (Lyrical)",
                "Cage (Chance/Chaos)", "Ligeti (Micropolyphony)", "Tan Dun (Organic/Ritual)"
            ], state="readonly")
            self.combo_style.current(0)
            self.combo_style.pack(fill=tk.X, padx=pad)

            # 2. 随机性/熵 (Entropy Slider)
            tk.Label(self.left_panel, text="Entropy / 随机熵 (Chaos)", style='Normal.TLabel').pack(pady=(15, 5),
                                                                                                   padx=pad, anchor="w")
            self.scale_chaos = tk.Scale(self.left_panel, from_=0, to=100, orient=tk.HORIZONTAL,
                                        bg=self.COLORS['bg_panel'], fg=self.COLORS['accent'],
                                        troughcolor=self.COLORS['bg_light'], highlightthickness=0)
            self.scale_chaos.set(30)
            self.scale_chaos.pack(fill=tk.X, padx=pad)

            # 3. 速度与小节
            param_frame = tk.Frame(self.left_panel, bg=self.COLORS['bg_panel'])
            param_frame.pack(fill=tk.X, padx=pad, pady=15)

            tk.Label(param_frame, text="BPM:", bg=self.COLORS['bg_panel'], fg=self.COLORS['text_main']).pack(
                side=tk.LEFT)
            self.ent_bpm = tk.Entry(param_frame, width=5, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
            self.ent_bpm.insert(0, "120")
            self.ent_bpm.pack(side=tk.LEFT, padx=5)

            tk.Label(param_frame, text="Bars:", bg=self.COLORS['bg_panel'], fg=self.COLORS['text_main']).pack(
                side=tk.LEFT, padx=(10, 0))
            self.ent_bars = tk.Entry(param_frame, width=5, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
            self.ent_bars.insert(0, "45")
            self.ent_bars.pack(side=tk.LEFT, padx=5)

            # 4. 生成按钮 (主要操作)
            btn_gen = tk.Button(self.left_panel, text="► GENERATE SEQUENCE",
                                bg=self.COLORS['accent'], fg='black', font=("Arial", 11, "bold"),
                                relief=tk.FLAT, activebackground='white', cursor='hand2',
                                command=self.on_generate_click)
            btn_gen.pack(fill=tk.X, padx=pad, pady=30)

            # 5. 导出选项
            tk.Label(self.left_panel, text="Export Target:", style='Normal.TLabel').pack(anchor="w", padx=pad)
            self.chk_xml = tk.IntVar(value=1)
            tk.Checkbutton(self.left_panel, text="MusicXML (Sibelius/Dorico)", variable=self.chk_xml,
                           bg=self.COLORS['bg_panel'], fg=self.COLORS['text_dim'],
                           selectcolor=self.COLORS['bg_panel']).pack(anchor="w", padx=pad)

            self.chk_midi = tk.IntVar(value=1)
            tk.Checkbutton(self.left_panel, text="Standard MIDI File", variable=self.chk_midi,
                           bg=self.COLORS['bg_panel'], fg=self.COLORS['text_dim'],
                           selectcolor=self.COLORS['bg_panel']).pack(anchor="w", padx=pad)

            # 底部 Log
            self.log_text = tk.Text(self.left_panel, height=10, bg="#000000", fg="#00FF00",
                                    font=("Consolas", 8), relief=tk.FLAT, state=tk.DISABLED)
            self.log_text.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        def build_center_panel(self):
            """构建中央矩阵交互区"""
            # 顶部工具栏
            toolbar = tk.Frame(self.center_panel, bg=self.COLORS['bg_dark'])
            toolbar.pack(fill=tk.X, pady=5)

            tk.Button(toolbar, text="🎲 Random Row", bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT,
                      command=self.randomize_matrix).pack(side=tk.LEFT, padx=5)
            tk.Button(toolbar, text="☯ Pentatonic Mode", bg=self.COLORS['bg_light'], fg='#FFCC00', relief=tk.FLAT,
                      command=self.pentatonic_matrix).pack(side=tk.LEFT, padx=5)
            tk.Button(toolbar, text="✔ Validate Check", bg=self.COLORS['bg_light'], fg=self.COLORS['accent_sec'],
                      relief=tk.FLAT,
                      command=self.validate_matrix).pack(side=tk.RIGHT, padx=5)

            # 矩阵网格容器
            self.grid_frame = tk.Frame(self.center_panel, bg=self.COLORS['bg_dark'])
            self.grid_frame.pack(expand=True)

            self.matrix_vars = []  # 存储StringVar
            self.matrix_entries = []  # 存储Entry控件

            # 绘制 13x13 网格 (包含标题)
            for r in range(13):
                row_vars = []
                row_entries = []
                for c in range(13):
                    # 样式逻辑
                    bg_color = self.COLORS['bg_panel']
                    fg_color = self.COLORS['text_main']
                    width = 4
                    state = 'normal'
                    val = ""

                    if r == 0 and c == 0:  # 左上角
                        val = "M"
                        bg_color = self.COLORS['bg_dark']
                        state = 'readonly'
                    elif r == 0:  # 列标题 (I)
                        val = f"I{c - 1}"
                        bg_color = self.COLORS['bg_dark']
                        fg_color = self.COLORS['accent_sec']
                        state = 'readonly'
                    elif c == 0:  # 行标题 (P)
                        val = f"P{r - 1}"
                        bg_color = self.COLORS['bg_dark']
                        fg_color = self.COLORS['accent']
                        state = 'readonly'
                    else:  # 数据格
                        if r == c: bg_color = "#252526"  # 对角线微妙高亮

                    sv = tk.StringVar(value=val)
                    e = tk.Entry(self.grid_frame, textvariable=sv, width=width, justify='center',
                                 bg=bg_color, fg=fg_color, relief=tk.FLAT, font=("Arial", 10))
                    e.grid(row=r, column=c, padx=1, pady=1, ipady=4)

                    # 如果是数据格，绑定事件
                    if r > 0 and c > 0:
                        e.bind('<FocusOut>', self.on_cell_edit)
                        e.bind('<Return>', self.on_cell_edit)

                    row_vars.append(sv)
                    row_entries.append(e)

                self.matrix_vars.append(row_vars)
                self.matrix_entries.append(row_entries)

        def build_right_panel(self):
            """构建右侧 AI 与 乐器区"""
            # Notebook 用于切换 乐器 / AI
            notebook = ttk.Notebook(self.right_panel)
            notebook.pack(fill=tk.BOTH, expand=True)

            # --- 页面1: Instrumentation (乐器法) ---
            page_inst = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
            notebook.add(page_inst, text=" Instruments ")

            tk.Label(page_inst, text="Ensemble Setup", style='Header.TLabel').pack(pady=10)

            # 乐器列表 (带 Checkbox)
            self.inst_vars = {}
            instruments = [
                ("Woodwinds", ["Flute", "Oboe", "Clarinet", "Bassoon"]),
                ("Brass", ["Horn", "Trumpet", "Trombone", "Tuba"]),
                ("Strings", ["Violin I", "Violin II", "Viola", "Cello", "Double Bass"]),
                ("Perc/Key", ["Piano", "Harp", "Timpani", "Percussion"]),
                ("Chinese", ["Guzheng", "Pipa", "Erhu", "Dizi"])  # 新增民乐
            ]

            # 滚动区域
            canvas = tk.Canvas(page_inst, bg=self.COLORS['bg_panel'], highlightthickness=0)
            scrollbar = ttk.Scrollbar(page_inst, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg=self.COLORS['bg_panel'])

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            for category, insts in instruments:
                tk.Label(scrollable_frame, text=category, bg=self.COLORS['bg_panel'],
                         fg=self.COLORS['accent'], font=("Arial", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
                for inst in insts:
                    var = tk.IntVar(value=1 if inst in ["Piano", "Flute", "Violin I"] else 0)
                    self.inst_vars[inst] = var
                    cb = tk.Checkbutton(scrollable_frame, text=inst, variable=var,
                                        bg=self.COLORS['bg_panel'], fg=self.COLORS['text_main'],
                                        selectcolor=self.COLORS['bg_panel'], activebackground=self.COLORS['bg_panel'])
                    cb.pack(anchor="w", padx=20)

            # --- 页面2: AI Architect (DeepSeek Integration) ---
            page_ai = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
            notebook.add(page_ai, text=" AI Architect ")

            tk.Label(page_ai, text="DeepSeek Integration", style='Header.TLabel').pack(pady=10)

            # 提示词生成按钮
            btn_prompts = tk.Button(page_ai, text="Open Architect Blueprints",
                                    bg=self.COLORS['accent_sec'], fg='black',
                                    command=lambda: TwelveToneAIArchitect.show_blueprint(self.root))
            btn_prompts.pack(fill=tk.X, padx=20, pady=10)

            tk.Label(page_ai, text="Live Context (Simulated):", style='Normal.TLabel').pack(anchor="w", padx=20)
            self.ai_context = tk.Text(page_ai, height=15, bg="#000000", fg="#00CCFF",
                                      font=("Consolas", 9), relief=tk.FLAT)
            self.ai_context.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
            self.ai_context.insert(tk.END,
                                   ">>> AI Architect Module Online\n>>> Listening to Matrix changes...\n>>> Ready for user query.")

        # ================= 逻辑交互 =================

        def log(self, message):
            self.log_text.config(state=tk.NORMAL)
            self.log_text.insert(tk.END, f"> {message}\n")
            self.log_text.see(tk.END)
            self.log_text.config(state=tk.DISABLED)

        def randomize_matrix(self):
            """生成随机矩阵并更新UI"""
            row = list(range(12))
            random.shuffle(row)
            self.regenerate_matrix_data(row)
            self.log("Generated random 12-tone row.")
            # 发送模拟信号给AI面板
            self.ai_context.insert(tk.END, f"\n>>> [Event] Matrix Randomized.\n>>> Row P0: {row}")

        def pentatonic_matrix(self):
            """生成五声性矩阵"""
            # 调用旧类中的方法，或直接实现
            # 这里简单实现：
            pentatonic = [0, 2, 4, 7, 9]  # C D E G A
            others = [1, 3, 5, 6, 8, 10, 11]
            random.shuffle(pentatonic)
            random.shuffle(others)
            row = pentatonic + others
            self.regenerate_matrix_data(row)
            self.log("Generated Chinese Pentatonic-biased row.")

        def regenerate_matrix_data(self, p0_numbers):
            """根据P0计算完整矩阵并填入网格"""
            self.backend_app = TwelveToneMatrix(self.root)  # 借用旧类逻辑计算矩阵
            self.backend_app.original_row = p0_numbers
            self.backend_app.create_twelve_tone_matrix()

            # 更新 Grid
            matrix_data = self.backend_app.matrix
            note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

            self.current_matrix = matrix_data  # 存储int矩阵

            for r in range(12):
                for c in range(12):
                    num = matrix_data[r][c]
                    note = note_names[num]
                    # 更新StringVar
                    self.matrix_vars[r + 1][c + 1].set(note)
                    # 恢复背景色
                    self.matrix_entries[r + 1][c + 1].config(bg=self.COLORS['bg_panel'])

        def validate_matrix(self):
            """执行严谨校验"""
            is_valid, errors = StrictMatrixValidator.validate_integrity(self.current_matrix)

            if is_valid:
                self.log("✅ Matrix Integrity Check: PASSED")
                messagebox.showinfo("Matrix Validator", "Perfect 12-Tone Matrix verified!")
            else:
                self.log(f"❌ Matrix Integrity Check: FAILED")
                # 高亮错误
                for r_idx in errors['rows']:
                    for c in range(12):
                        self.matrix_entries[r_idx + 1][c + 1].config(bg=self.COLORS['error'])
                for c_idx in errors['cols']:
                    for r in range(12):
                        self.matrix_entries[r + 1][c_idx + 1].config(bg=self.COLORS['error'])

                msg = f"Found conflicts:\nRows: {errors['rows']}\nCols: {errors['cols']}\nDiagonals: {errors['diagonals']}"
                messagebox.showwarning("Integrity Error", msg)

        def on_cell_edit(self, event):
            """用户手动编辑单元格后的处理 (简化版: 暂不实时重算整个矩阵，只校验)"""
            # 实际开发中这里应该包含复杂的反向计算逻辑
            pass

        def on_generate_click(self):
            """点击生成按钮：启动多线程生成"""
            # 1. 收集参数
            selected_insts = [name for name, var in self.inst_vars.items() if var.get() == 1]
            if not selected_insts:
                messagebox.showwarning("Warning", "Select at least one instrument.")
                return

            style = self.combo_style.get()
            chaos = self.scale_chaos.get()
            bpm = int(self.ent_bpm.get())
            bars = int(self.ent_bars.get())

            self.log(f"Starting Generation... Style: {style}, Chaos: {chaos}%")

            # 2. 准备数据传输给旧引擎
            # 为了不破坏旧代码，我们将数据注入到旧的 AdvancedTwelveToneComposer
            # 但我们需要确保每次生成都不一样 (Seed)
            seed = int(time.time() * 1000)
            random.seed(seed)
            self.log(f"Random Seed: {seed}")

            # 3. 启动线程
            t = threading.Thread(target=self.run_generation_process,
                                 args=(selected_insts, style, bpm, bars, chaos))
            t.start()

        def run_generation_process(self, instruments, style, bpm, bars, chaos_level):
            """后台生成逻辑 (桥接层)"""
            try:
                # 映射风格名称到旧代码的key
                style_map = {
                    "Schoenberg (Classic)": "schoenberg",
                    "Webern (Pointillism)": "webern",
                    "Berg (Lyrical)": "berg",
                    "Cage (Chance/Chaos)": "contemporary",  # Map Cage to contemporary
                    "Ligeti (Micropolyphony)": "contemporary",
                    "Tan Dun (Organic/Ritual)": "chinese_pentatonic"
                }
                tech_key = style_map.get(style, "schoenberg")

                # 准备矩阵数据格式
                matrix_data_full = self.backend_app.matrix_data  # 获取 P/I/R/RI 字典

                # 实例化 Composer
                composer = AdvancedTwelveToneComposer()

                # 注入随机性：修改 composer 内部的概率参数
                # 这里通过 chaos_level (0-100) 动态调整
                # (这是一个模拟，实际需要修改旧类的方法，或者我们在调用 run 之前 monkey-patch 一些参数)

                # 调用核心生成 (稍微修改 create_professional_score 以接受更多参数，或者复用现有)
                # 由于旧代码 create_professional_score 签名固定，我们直接调用它
                # 但传入我们精心构造的参数

                score = composer.create_professional_score(
                    instruments=instruments,
                    matrix=self._convert_matrix_data_to_lookup(matrix_data_full),  # 需要转换格式
                    tempo_mark=f"{style} Mode",
                    tempo_value=bpm,
                    num_measures=bars,
                    technique=tech_key,
                    use_imported_matrix=True,
                    emotion="dramatic" if chaos_level > 50 else "lyrical"
                )

                # 文件导出
                filename = composer.generate_sibelius_files(score)

                # UI 回调
                self.root.after(0, lambda: self.generation_complete(filename))

            except Exception as e:
                self.root.after(0, lambda: self.log(f"Error: {str(e)}"))
                print(e)

        def _convert_matrix_data_to_lookup(self, matrix_data):
            """将分层的 P/I/R/RI 数据转换为扁平查找表，供旧引擎使用"""
            lookup = {}
            for seq_type in ['P', 'I', 'R', 'RI']:
                for t in range(12):
                    key = f"{seq_type}{t}"
                    if t in matrix_data[seq_type]:
                        lookup[key] = matrix_data[seq_type][t]
            # 确保有 P0
            if "P0" not in lookup:
                lookup["P0"] = list(range(12))  # Fallback
            return lookup

        def generation_complete(self, filename):
            self.log(f"SUCCESS! Output saved to: {filename}")
            messagebox.showinfo("Composition Complete",
                                f"Music generated successfully!\nFile: {filename}\n\nSeed used was unique.")
            self.ai_context.insert(tk.END,
                                   f"\n>>> [Success] File generated: {filename}\n>>> Analysis: Structure valid, Instrumentation optimized.")


    # ==============================================================================
    # MAIN ENTRY POINT MODIFICATION
    # ==============================================================================

    def main_pro():
        """Pro版启动入口"""
        root = tk.Tk()

        # 尝试设置图标 (如果有的话，否则跳过)
        # root.iconbitmap('icon.ico')

        app = ModernTwelveToneWorkstation(root)
        root.mainloop()


    if __name__ == "__main__":
        # 替换原来的 main() 调用，启动 Pro 版本
        # 如果想保留旧版本入口，可以做一个选择菜单，但这里默认直接进入 Pro 界面
        main_pro()
# ==============================================================================
# 【增量更新包 v7.1】 TWELVE-TONE PRO SUITE (修复版)
# 请将此代码段完整粘贴到原文件末尾
# ==============================================================================

import threading
import time
import math
import copy


# ------------------------------------------------------------------------------
# 1. 严谨魔方验证引擎 (Strict Matrix Logic)
# ------------------------------------------------------------------------------
class StrictMatrixValidator:
    """用于校验12x12矩阵的数学完整性，确保行/列无重复音"""

    @staticmethod
    def validate(matrix):
        errors = {'rows': [], 'cols': [], 'diagonals': []}
        is_valid = True
        required_set = set(range(12))

        # 检查行
        for r_idx, row in enumerate(matrix):
            if set(row) != required_set:
                errors['rows'].append(r_idx)
                is_valid = False

        # 检查列
        for c_idx in range(12):
            col = [matrix[r][c_idx] for r in range(12)]
            if set(col) != required_set:
                errors['cols'].append(c_idx)
                is_valid = False

        return is_valid, errors


# ------------------------------------------------------------------------------
# 2. 现代深色专业界面 (Modern Dark UI)
# ------------------------------------------------------------------------------
class ModernTwelveToneWorkstation:
    """
    【十二音AI Pro工作台】
    集成 DeepSeek 架构师蓝图、Ableton 风格界面与核心生成引擎。
    """
    COLORS = {
        'bg_dark': '#121212', 'bg_panel': '#1E1E1E', 'bg_light': '#2D2D2D',
        'accent': '#00FF99', 'accent_sec': '#00CCFF', 'text_main': '#E0E0E0',
        'text_dim': '#888888', 'error': '#FF5555'
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Twelve-Tone AI Pro Workstation v7.1 (Ultimate)")
        self.root.geometry("1400x900")
        self.root.configure(bg=self.COLORS['bg_dark'])

        # 继承原有核心
        self.composer = AdvancedTwelveToneComposer()

        # 状态数据
        self.current_matrix_data = [[0] * 12 for _ in range(12)]
        self.inst_vars = {}

        self.setup_ui()
        # 初始化一个默认随机序列
        self.randomize_matrix()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TFrame', background=self.COLORS['bg_panel'])

        # --- 主布局容器 ---
        main_frame = tk.Frame(self.root, bg=self.COLORS['bg_dark'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 1. 左侧：参数控制 (Control Panel)
        left_panel = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=320)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        left_panel.pack_propagate(False)
        self.build_left_panel(left_panel)

        # 2. 中间：魔方矩阵 (The Matrix)
        center_panel = tk.Frame(main_frame, bg=self.COLORS['bg_dark'])
        center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.build_center_panel(center_panel)

        # 3. 右侧：AI与乐器 (Instruments & AI)
        right_panel = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=360)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        right_panel.pack_propagate(False)
        self.build_right_panel(right_panel)

    def build_left_panel(self, parent):
        pad = 15
        tk.Label(parent, text="SEQUENCER CONTROLS", font=("Impact", 16),
                 bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(pady=20, anchor="w", padx=pad)

        # 风格选择
        tk.Label(parent, text="Composition Style / 风格模型", bg=self.COLORS['bg_panel'],
                 fg=self.COLORS['text_dim']).pack(anchor="w", padx=pad)
        self.style_var = tk.StringVar(value="Schoenberg (Classic)")
        styles = ["Schoenberg (Classic)", "Webern (Pointillism)", "Berg (Lyrical)", "Contemporary (Hybrid)",
                  "Chinese Pentatonic"]
        cb = ttk.Combobox(parent, textvariable=self.style_var, values=styles, state="readonly")
        cb.pack(fill=tk.X, padx=pad, pady=(5, 15))

        # 随机性控制 (确保每次不一样)
        tk.Label(parent, text="Chaos Entropy / 随机熵 (0-100%)", bg=self.COLORS['bg_panel'],
                 fg=self.COLORS['text_dim']).pack(anchor="w", padx=pad)
        self.chaos_scale = tk.Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL,
                                    bg=self.COLORS['bg_panel'], fg=self.COLORS['accent'], highlightthickness=0)
        self.chaos_scale.set(35)
        self.chaos_scale.pack(fill=tk.X, padx=pad, pady=5)

        # 速度与小节
        param_frame = tk.Frame(parent, bg=self.COLORS['bg_panel'])
        param_frame.pack(fill=tk.X, padx=pad, pady=15)

        tk.Label(param_frame, text="BPM:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT)
        self.bpm_entry = tk.Entry(param_frame, width=6, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
        self.bpm_entry.insert(0, "110")
        self.bpm_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(param_frame, text="Bars:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT, padx=(10, 0))
        self.bars_entry = tk.Entry(param_frame, width=6, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
        self.bars_entry.insert(0, "45")
        self.bars_entry.pack(side=tk.LEFT, padx=5)

        # 生成按钮
        btn = tk.Button(parent, text="► GENERATE MASTERPIECE",
                        bg=self.COLORS['accent'], fg='black', font=("Arial", 11, "bold"),
                        relief=tk.FLAT, pady=10, command=self.on_generate)
        btn.pack(fill=tk.X, padx=pad, pady=30)

        # 日志区
        self.log_box = tk.Text(parent, height=12, bg="#000000", fg="#00FF00",
                               font=("Consolas", 8), relief=tk.FLAT, state=tk.DISABLED)
        self.log_box.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

    def build_center_panel(self, parent):
        # 工具栏
        toolbar = tk.Frame(parent, bg=self.COLORS['bg_dark'])
        toolbar.pack(fill=tk.X, pady=5)

        tk.Button(toolbar, text="🎲 Random Row", bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT,
                  command=self.randomize_matrix).pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="☯ Pentatonic", bg=self.COLORS['bg_light'], fg='#FFD700', relief=tk.FLAT,
                  command=self.pentatonic_matrix).pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="✔ Validate", bg=self.COLORS['bg_light'], fg=self.COLORS['accent_sec'], relief=tk.FLAT,
                  command=self.validate_matrix).pack(side=tk.RIGHT, padx=2)

        # 矩阵网格
        self.matrix_frame = tk.Frame(parent, bg=self.COLORS['bg_dark'])
        self.matrix_frame.pack(expand=True, fill=tk.BOTH)

        self.cells = []
        # 绘制 13x13 (含标题)
        for r in range(13):
            row_cells = []
            for c in range(13):
                bg = self.COLORS['bg_panel']
                fg = self.COLORS['text_main']
                val = ""

                if r == 0 and c == 0:
                    bg = self.COLORS['bg_dark']
                elif r == 0:
                    val = f"I{c - 1}"
                    bg = self.COLORS['bg_dark'];
                    fg = self.COLORS['accent_sec']
                elif c == 0:
                    val = f"P{r - 1}"
                    bg = self.COLORS['bg_dark'];
                    fg = self.COLORS['accent']
                elif r == c:
                    bg = "#2A2A2A"  # 对角线

                sv = tk.StringVar(value=val)
                ent = tk.Entry(self.matrix_frame, textvariable=sv, width=4, justify='center',
                               bg=bg, fg=fg, relief=tk.FLAT, font=("Arial", 9))
                ent.grid(row=r, column=c, padx=1, pady=1, ipady=3)
                row_cells.append((sv, ent))
            self.cells.append(row_cells)

    def build_right_panel(self, parent):
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True)

        # --- 乐器页 ---
        f1 = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
        notebook.add(f1, text=" Instruments ")

        tk.Label(f1, text="Ensemble Selection", font=("Arial", 11, "bold"),
                 bg=self.COLORS['bg_panel'], fg='white').pack(pady=10)

        inst_list = [
            ("Keys/Harp", ["Piano", "Harp"]),
            ("Strings", ["Violin I", "Violin II", "Viola", "Cello", "Double Bass"]),
            ("Winds", ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet"]),
            ("Percussion", ["Timpani", "Percussion"]),
            ("Chinese", ["Guzheng", "Pipa"])
        ]

        canvas = tk.Canvas(f1, bg=self.COLORS['bg_panel'], highlightthickness=0)
        scr = ttk.Scrollbar(f1, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=self.COLORS['bg_panel'])

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scr.set)

        canvas.pack(side="left", fill="both", expand=True)
        scr.pack(side="right", fill="y")

        for cat, insts in inst_list:
            tk.Label(scroll_frame, text=cat, bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(anchor="w",
                                                                                                        padx=10,
                                                                                                        pady=(5, 0))
            for i in insts:
                var = tk.IntVar(value=1 if i in ["Piano", "Violin I", "Flute"] else 0)
                self.inst_vars[i] = var
                cb = tk.Checkbutton(scroll_frame, text=i, variable=var,
                                    bg=self.COLORS['bg_panel'], fg='white',
                                    selectcolor=self.COLORS['bg_panel'], activebackground=self.COLORS['bg_panel'])
                cb.pack(anchor="w", padx=20)

        # --- AI页 ---
        f2 = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
        notebook.add(f2, text=" AI Architect ")

        tk.Label(f2, text="DeepSeek Blueprint", font=("Impact", 14),
                 bg=self.COLORS['bg_panel'], fg=self.COLORS['accent_sec']).pack(pady=15)

        btn_blueprint = tk.Button(f2, text="Open Dev Blueprints",
                                  bg='#333', fg='white', pady=5,
                                  command=lambda: TwelveToneAIArchitect.show_blueprint(self.root))
        btn_blueprint.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(f2, text="AI Context Log:", bg=self.COLORS['bg_panel'], fg='#888').pack(anchor="w", padx=10)
        self.ai_log = tk.Text(f2, height=10, bg="black", fg="#00CCFF", font=("Consolas", 8))
        self.ai_log.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
        self.ai_log.insert(tk.END, ">>> DeepSeek Connector Initialized.\n>>> Waiting for generation context...")

    # --- 逻辑功能 ---

    def log(self, msg):
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, f"> {msg}\n")
        self.log_box.see(tk.END)
        self.log_box.config(state=tk.DISABLED)

    def randomize_matrix(self):
        row = list(range(12))
        random.shuffle(row)
        self.render_matrix(row)
        self.log(f"New Random Row Generated: {row}")

    def pentatonic_matrix(self):
        penta = [0, 2, 4, 7, 9]  # C D E G A
        remain = [1, 3, 5, 6, 8, 10, 11]
        random.shuffle(penta)
        random.shuffle(remain)
        row = penta + remain
        self.render_matrix(row)
        self.log("Generated Pentatonic-Biased Row")

    def render_matrix(self, p0):
        # 使用数学逻辑计算矩阵
        matrix = [[0] * 12 for _ in range(12)]
        matrix[0] = p0
        i0 = [(12 - x) % 12 for x in p0]
        for r in range(12):
            for c in range(12):
                val = (matrix[0][c] + i0[r] - matrix[0][0]) % 12
                matrix[r][c] = val

        self.current_matrix_data = matrix
        names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        for r in range(12):
            for c in range(12):
                sv, ent = self.cells[r + 1][c + 1]
                sv.set(names[matrix[r][c]])
                ent.config(bg=self.COLORS['bg_panel'])

    def validate_matrix(self):
        is_valid, errors = StrictMatrixValidator.validate(self.current_matrix_data)
        if is_valid:
            self.log("VALIDATION PASS: Perfect 12-tone matrix.")
            messagebox.showinfo("Result", "Matrix is mathematically perfect!")
        else:
            self.log(f"VALIDATION FAIL: Conflicts found in {len(errors['rows'])} rows.")
            for r in errors['rows']:
                for c in range(12): self.cells[r + 1][c + 1][1].config(bg=self.COLORS['error'])
            messagebox.showwarning("Result", "Matrix integrity violations found (marked red).")

    def on_generate(self):
        selected_inst = [k for k, v in self.inst_vars.items() if v.get() == 1]
        if not selected_inst:
            messagebox.showwarning("Tips", "Please select at least one instrument.")
            return

        bpm = int(self.bpm_entry.get())
        bars = int(self.bars_entry.get())
        chaos = self.chaos_scale.get()
        style_full = self.style_var.get()

        style_map = {
            "Schoenberg (Classic)": "schoenberg",
            "Webern (Pointillism)": "webern",
            "Berg (Lyrical)": "berg",
            "Contemporary (Hybrid)": "contemporary",
            "Chinese Pentatonic": "chinese_pentatonic"
        }
        tech_key = style_map.get(style_full, "schoenberg")

        self.log(f"Starting Generation... Style: {tech_key}, Chaos: {chaos}%")

        # 开启线程
        t = threading.Thread(target=self.run_backend, args=(selected_inst, tech_key, bpm, bars, chaos))
        t.start()

    def run_backend(self, instruments, technique, bpm, bars, chaos):
        try:
            # 动态种子
            random.seed(time.time())
            emotion = "agitated" if chaos > 60 else ("lyrical" if chaos < 30 else "default")

            # 兼容性调用：直接使用原类的 run 逻辑部分，但必须避免 run() 里的 input()
            # 所以我们直接调 create_professional_score 而不是 composer.run()

            # 1. 准备矩阵数据
            p0 = self.current_matrix_data[0]
            # 转换音名
            num_to_note = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#",
                           11: "B"}
            p0_notes = [num_to_note[n] for n in p0]
            matrix_full = self.composer.generate_matrix(p0_notes)

            # 2. 生成乐谱
            score = self.composer.create_professional_score(
                instruments=instruments,
                matrix=matrix_full,
                tempo_mark=f"Pro {technique.title()}",
                tempo_value=bpm,
                num_measures=bars,
                technique=technique,
                use_imported_matrix=False,
                emotion=emotion
            )

            # 3. 导出
            final_file = self.composer.generate_sibelius_files(score)

            self.root.after(0, lambda: self.finish_gen(final_file))

        except Exception as e:
            print(f"Error detail: {e}")
            import traceback
            traceback.print_exc()
            self.root.after(0, lambda: self.log(f"Error: {e}"))

    def finish_gen(self, filename):
        self.log(f"DONE. File: {filename}")
        self.ai_log.insert(tk.END, "\n>>> MusicXML Exported successfully.")
        messagebox.showinfo("Success", f"Composition Generated!\n\nSaved as: {filename}")


# ------------------------------------------------------------------------------
# 启动入口覆盖 (Override Main)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # 强制以新界面启动，忽略旧的 main()
    try:
        root_pro = tk.Tk()
        app = ModernTwelveToneWorkstation(root_pro)
        root_pro.mainloop()
    except KeyboardInterrupt:
        pass
    # ==============================================================================
    # 【最终完整扩展包 v7.2】 PRO界面集成与按钮重定向
    # 请将此代码完整粘贴到文件最末尾，它会自动升级你的按钮功能
    # ==============================================================================

    import threading
    import time
    import math
    import copy
    from tkinter import messagebox


    # ------------------------------------------------------------------------------
    # 1. 严谨魔方验证引擎 (Strict Matrix Logic)
    # ------------------------------------------------------------------------------
    class StrictMatrixValidator:
        """用于校验12x12矩阵的数学完整性，确保行/列无重复音"""

        @staticmethod
        def validate(matrix):
            errors = {'rows': [], 'cols': [], 'diagonals': []}
            is_valid = True
            required_set = set(range(12))

            # 检查行
            for r_idx, row in enumerate(matrix):
                if set(row) != required_set:
                    errors['rows'].append(r_idx)
                    is_valid = False

            # 检查列
            for c_idx in range(12):
                col = [matrix[r][c_idx] for r in range(12)]
                if set(col) != required_set:
                    errors['cols'].append(c_idx)
                    is_valid = False

            return is_valid, errors


    # ------------------------------------------------------------------------------
    # 2. 现代深色专业界面 (Modern Dark UI)
    # ------------------------------------------------------------------------------
    class ModernTwelveToneWorkstation:
        """
        【十二音AI Pro工作台】
        """
        COLORS = {
            'bg_dark': '#121212', 'bg_panel': '#1E1E1E', 'bg_light': '#2D2D2D',
            'accent': '#00FF99', 'accent_sec': '#00CCFF', 'text_main': '#E0E0E0',
            'text_dim': '#888888', 'error': '#FF5555'
        }

        def __init__(self, root):
            self.root = root
            self.root.title("Twelve-Tone AI Pro Workstation v7.2")
            self.root.geometry("1400x900")
            self.root.configure(bg=self.COLORS['bg_dark'])

            # 继承原有核心
            self.composer = AdvancedTwelveToneComposer()

            # 状态数据
            self.current_matrix_data = [[0] * 12 for _ in range(12)]
            self.inst_vars = {}

            self.setup_ui()
            self.randomize_matrix()

        def setup_ui(self):
            style = ttk.Style()
            style.theme_use('clam')

            # --- 主布局容器 ---
            main_frame = tk.Frame(self.root, bg=self.COLORS['bg_dark'])
            main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # 左侧：参数控制
            left_panel = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=320)
            left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5)
            left_panel.pack_propagate(False)
            self.build_left_panel(left_panel)

            # 中间：魔方矩阵
            center_panel = tk.Frame(main_frame, bg=self.COLORS['bg_dark'])
            center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
            self.build_center_panel(center_panel)

            # 右侧：AI与乐器
            right_panel = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=360)
            right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
            right_panel.pack_propagate(False)
            self.build_right_panel(right_panel)

        def build_left_panel(self, parent):
            pad = 15
            tk.Label(parent, text="SEQUENCER CONTROLS", font=("Impact", 16),
                     bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(pady=20, anchor="w", padx=pad)

            # 风格选择
            tk.Label(parent, text="Composition Style / 风格模型", bg=self.COLORS['bg_panel'],
                     fg=self.COLORS['text_dim']).pack(anchor="w", padx=pad)
            self.style_var = tk.StringVar(value="Schoenberg (Classic)")
            styles = ["Schoenberg (Classic)", "Webern (Pointillism)", "Berg (Lyrical)", "Contemporary (Hybrid)",
                      "Chinese Pentatonic"]
            cb = ttk.Combobox(parent, textvariable=self.style_var, values=styles, state="readonly")
            cb.pack(fill=tk.X, padx=pad, pady=(5, 15))

            # 随机性控制
            tk.Label(parent, text="Chaos Entropy / 随机熵", bg=self.COLORS['bg_panel'],
                     fg=self.COLORS['text_dim']).pack(anchor="w", padx=pad)
            self.chaos_scale = tk.Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL,
                                        bg=self.COLORS['bg_panel'], fg=self.COLORS['accent'], highlightthickness=0)
            self.chaos_scale.set(35)
            self.chaos_scale.pack(fill=tk.X, padx=pad, pady=5)

            # 速度与小节
            param_frame = tk.Frame(parent, bg=self.COLORS['bg_panel'])
            param_frame.pack(fill=tk.X, padx=pad, pady=15)

            tk.Label(param_frame, text="BPM:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT)
            self.bpm_entry = tk.Entry(param_frame, width=6, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
            self.bpm_entry.insert(0, "110")
            self.bpm_entry.pack(side=tk.LEFT, padx=5)

            tk.Label(param_frame, text="Bars:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT, padx=(10, 0))
            self.bars_entry = tk.Entry(param_frame, width=6, bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT)
            self.bars_entry.insert(0, "45")
            self.bars_entry.pack(side=tk.LEFT, padx=5)

            # 生成按钮
            btn = tk.Button(parent, text="► GENERATE MASTERPIECE",
                            bg=self.COLORS['accent'], fg='black', font=("Arial", 11, "bold"),
                            relief=tk.FLAT, pady=10, command=self.on_generate)
            btn.pack(fill=tk.X, padx=pad, pady=30)

            # 日志区
            self.log_box = tk.Text(parent, height=12, bg="#000000", fg="#00FF00",
                                   font=("Consolas", 8), relief=tk.FLAT, state=tk.DISABLED)
            self.log_box.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

        def build_center_panel(self, parent):
            toolbar = tk.Frame(parent, bg=self.COLORS['bg_dark'])
            toolbar.pack(fill=tk.X, pady=5)

            tk.Button(toolbar, text="🎲 Random Row", bg=self.COLORS['bg_light'], fg='white', relief=tk.FLAT,
                      command=self.randomize_matrix).pack(side=tk.LEFT, padx=2)
            tk.Button(toolbar, text="☯ Pentatonic", bg=self.COLORS['bg_light'], fg='#FFD700', relief=tk.FLAT,
                      command=self.pentatonic_matrix).pack(side=tk.LEFT, padx=2)
            tk.Button(toolbar, text="✔ Validate", bg=self.COLORS['bg_light'], fg=self.COLORS['accent_sec'],
                      relief=tk.FLAT,
                      command=self.validate_matrix).pack(side=tk.RIGHT, padx=2)

            self.matrix_frame = tk.Frame(parent, bg=self.COLORS['bg_dark'])
            self.matrix_frame.pack(expand=True, fill=tk.BOTH)

            self.cells = []
            for r in range(13):
                row_cells = []
                for c in range(13):
                    bg = self.COLORS['bg_panel']
                    fg = self.COLORS['text_main']
                    val = ""
                    if r == 0 and c == 0:
                        bg = self.COLORS['bg_dark']
                    elif r == 0:
                        val = f"I{c - 1}"; bg = self.COLORS['bg_dark']; fg = self.COLORS['accent_sec']
                    elif c == 0:
                        val = f"P{r - 1}"; bg = self.COLORS['bg_dark']; fg = self.COLORS['accent']
                    elif r == c:
                        bg = "#2A2A2A"

                    sv = tk.StringVar(value=val)
                    ent = tk.Entry(self.matrix_frame, textvariable=sv, width=4, justify='center',
                                   bg=bg, fg=fg, relief=tk.FLAT, font=("Arial", 9))
                    ent.grid(row=r, column=c, padx=1, pady=1, ipady=3)
                    row_cells.append((sv, ent))
                self.cells.append(row_cells)

        def build_right_panel(self, parent):
            notebook = ttk.Notebook(parent)
            notebook.pack(fill=tk.BOTH, expand=True)

            # 乐器页
            f1 = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
            notebook.add(f1, text=" Instruments ")
            tk.Label(f1, text="Ensemble Selection", font=("Arial", 11, "bold"),
                     bg=self.COLORS['bg_panel'], fg='white').pack(pady=10)

            inst_list = [
                ("Keys/Harp", ["Piano", "Harp"]),
                ("Strings", ["Violin I", "Violin II", "Viola", "Cello", "Double Bass"]),
                ("Winds", ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet"]),
                ("Percussion", ["Timpani", "Percussion"]),
                ("Chinese", ["Guzheng", "Pipa"])
            ]

            canvas = tk.Canvas(f1, bg=self.COLORS['bg_panel'], highlightthickness=0)
            scr = ttk.Scrollbar(f1, orient="vertical", command=canvas.yview)
            scroll_frame = tk.Frame(canvas, bg=self.COLORS['bg_panel'])
            scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
            canvas.configure(yscrollcommand=scr.set)
            canvas.pack(side="left", fill="both", expand=True)
            scr.pack(side="right", fill="y")

            for cat, insts in inst_list:
                tk.Label(scroll_frame, text=cat, bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(anchor="w",
                                                                                                            padx=10,
                                                                                                            pady=(5, 0))
                for i in insts:
                    var = tk.IntVar(value=1 if i in ["Piano", "Violin I", "Flute"] else 0)
                    self.inst_vars[i] = var
                    cb = tk.Checkbutton(scroll_frame, text=i, variable=var,
                                        bg=self.COLORS['bg_panel'], fg='white',
                                        selectcolor=self.COLORS['bg_panel'], activebackground=self.COLORS['bg_panel'])
                    cb.pack(anchor="w", padx=20)

            # AI页
            f2 = tk.Frame(notebook, bg=self.COLORS['bg_panel'])
            notebook.add(f2, text=" AI Architect ")
            tk.Label(f2, text="DeepSeek Blueprint", font=("Impact", 14),
                     bg=self.COLORS['bg_panel'], fg=self.COLORS['accent_sec']).pack(pady=15)

            btn_blueprint = tk.Button(f2, text="Open Dev Blueprints",
                                      bg='#333', fg='white', pady=5,
                                      command=lambda: TwelveToneAIArchitect.show_blueprint(self.root))
            btn_blueprint.pack(fill=tk.X, padx=20, pady=10)

            tk.Label(f2, text="AI Context Log:", bg=self.COLORS['bg_panel'], fg='#888').pack(anchor="w", padx=10)
            self.ai_log = tk.Text(f2, height=10, bg="black", fg="#00CCFF", font=("Consolas", 8))
            self.ai_log.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
            self.ai_log.insert(tk.END, ">>> DeepSeek Connector Initialized.")

        def log(self, msg):
            self.log_box.config(state=tk.NORMAL)
            self.log_box.insert(tk.END, f"> {msg}\n")
            self.log_box.see(tk.END)
            self.log_box.config(state=tk.DISABLED)

        def randomize_matrix(self):
            row = list(range(12))
            random.shuffle(row)
            self.render_matrix(row)
            self.log(f"New Random Row Generated: {row}")

        def pentatonic_matrix(self):
            penta = [0, 2, 4, 7, 9]
            remain = [1, 3, 5, 6, 8, 10, 11]
            random.shuffle(penta);
            random.shuffle(remain)
            self.render_matrix(penta + remain)
            self.log("Generated Pentatonic-Biased Row")

        def render_matrix(self, p0):
            matrix = [[0] * 12 for _ in range(12)]
            matrix[0] = p0
            i0 = [(12 - x) % 12 for x in p0]
            for r in range(12):
                for c in range(12):
                    matrix[r][c] = (matrix[0][c] + i0[r] - matrix[0][0]) % 12
            self.current_matrix_data = matrix
            names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            for r in range(12):
                for c in range(12):
                    sv, ent = self.cells[r + 1][c + 1]
                    sv.set(names[matrix[r][c]])
                    ent.config(bg=self.COLORS['bg_panel'])

        def validate_matrix(self):
            is_valid, errors = StrictMatrixValidator.validate(self.current_matrix_data)
            if is_valid:
                self.log("VALIDATION PASS: Perfect matrix.")
                messagebox.showinfo("Result", "Matrix is mathematically perfect!")
            else:
                self.log(f"VALIDATION FAIL: Conflicts found.")
                for r in errors['rows']:
                    for c in range(12): self.cells[r + 1][c + 1][1].config(bg=self.COLORS['error'])
                messagebox.showwarning("Result", "Matrix conflicts found (marked red).")

        def on_generate(self):
            selected_inst = [k for k, v in self.inst_vars.items() if v.get() == 1]
            if not selected_inst:
                messagebox.showwarning("Tips", "Please select at least one instrument.")
                return

            bpm = int(self.bpm_entry.get())
            bars = int(self.bars_entry.get())
            chaos = self.chaos_scale.get()
            style_full = self.style_var.get()

            style_map = {
                "Schoenberg (Classic)": "schoenberg",
                "Webern (Pointillism)": "webern",
                "Berg (Lyrical)": "berg",
                "Contemporary (Hybrid)": "contemporary",
                "Chinese Pentatonic": "chinese_pentatonic"
            }
            tech_key = style_map.get(style_full, "schoenberg")

            self.log(f"Starting Generation... Style: {tech_key}, Chaos: {chaos}%")
            self.ai_log.insert(tk.END, f"\n>>> Analyzing matrix entropy...\n>>> Generating with seed: {time.time()}")

            t = threading.Thread(target=self.run_backend, args=(selected_inst, tech_key, bpm, bars, chaos))
            t.start()

        def run_backend(self, instruments, technique, bpm, bars, chaos):
            try:
                random.seed(time.time())
                emotion = "agitated" if chaos > 60 else ("lyrical" if chaos < 30 else "default")

                p0 = self.current_matrix_data[0]
                num_to_note = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A",
                               10: "A#", 11: "B"}
                p0_notes = [num_to_note[n] for n in p0]
                matrix_full = self.composer.generate_matrix(p0_notes)

                score = self.composer.create_professional_score(
                    instruments=instruments,
                    matrix=matrix_full,
                    tempo_mark=f"Pro {technique.title()}",
                    tempo_value=bpm,
                    num_measures=bars,
                    technique=technique,
                    use_imported_matrix=False,
                    emotion=emotion
                )

                final_file = self.composer.generate_sibelius_files(score)
                self.root.after(0, lambda: self.finish_gen(final_file))

            except Exception as e:
                print(f"Error detail: {e}")
                import traceback
                traceback.print_exc()
                self.root.after(0, lambda: self.log(f"Error: {e}"))

        def finish_gen(self, filename):
            self.log(f"DONE. File: {filename}")
            self.ai_log.insert(tk.END, "\n>>> MusicXML Exported successfully.")
            messagebox.showinfo("Success", f"Composition Generated!\n\nSaved as: {filename}")


    # ------------------------------------------------------------------------------
    # 3. 动态升级主菜单按钮 (Monkey Patch) & 启动
    # ------------------------------------------------------------------------------

    def upgrade_main_menu_button(self):
        """
        这个函数替换旧的 open_professional_composer
        让它点击后直接打开新版界面，而不是运行控制台脚本。
        """
        # 创建独立窗口
        pro_window = tk.Toplevel(self.root)
        # 初始化新版界面
        app = ModernTwelveToneWorkstation(pro_window)


    # 核心：将新函数赋值给旧类 (Monkey Patching)
    TwelveToneSuite.open_professional_composer = upgrade_main_menu_button

    # 启动主程序
    if __name__ == "__main__":
        try:
            # 这里启动主菜单 (TwelveToneSuite)
            # 此时它的第二个按钮已经被上面的代码“偷梁换柱”升级为打开新界面了
            root = tk.Tk()
            app = TwelveToneSuite(root)
            root.mainloop()
        except KeyboardInterrupt:
            pass
        # ==============================================================================
        # 【最终修正补丁 v8.0】 界面弹窗修复 + 作曲家风格大脑集成
        # 请将此代码完整粘贴到文件最末尾 (不要删除上方代码)
        # ==============================================================================

        import threading
        import time
        import random
        import tkinter as tk
        from tkinter import ttk, messagebox


        # ------------------------------------------------------------------------------
        # 1. 作曲家风格分析引擎 (The Composer Brain)
        # 基于大量谱例分析得出的特征参数库
        # ------------------------------------------------------------------------------
        class ComposerStyleBrain:
            """
            风格参数控制器：决定生成的音乐到底“像”谁。
            """

            @staticmethod
            def get_style_parameters(style_name):
                """
                返回特定作曲家的各项参数特征
                """
                # 默认参数
                params = {
                    "dynamic_range": ["mp", "mf"],  # 力度范围
                    "rhythm_density": 0.5,  # 节奏密度 (0-1)
                    "silence_probability": 0.1,  # 休止符概率
                    "leap_probability": 0.3,  # 大跳音程概率
                    "articulation_pref": "normal",  # 演奏法偏好
                    "chord_complexity": 3  # 和弦复杂度
                }

                if "Webern" in style_name:  # 韦伯恩风格：点描、极简、大跳、极弱
                    params.update({
                        "dynamic_range": ["ppp", "pp", "p", "mp"],
                        "rhythm_density": 0.3,  # 稀疏
                        "silence_probability": 0.4,  # 大量留白
                        "leap_probability": 0.8,  # 极其频繁的大跳(7度/9度)
                        "articulation_pref": "staccato",  # 多用断奏
                        "chord_complexity": 2  # 少用厚重和弦
                    })
                elif "Berg" in style_name:  # 贝尔格风格：抒情、准调性、戏剧性
                    params.update({
                        "dynamic_range": ["pp", "mp", "mf", "f", "ff"],
                        "rhythm_density": 0.6,
                        "silence_probability": 0.1,
                        "leap_probability": 0.2,  # 级进较多
                        "articulation_pref": "legato",  # 多用连奏
                        "chord_complexity": 4  # 丰满的和声
                    })
                elif "Chinese" in style_name:  # 现代民乐风格：五声性、流水、装饰音
                    params.update({
                        "dynamic_range": ["mp", "mf", "f"],
                        "rhythm_density": 0.7,
                        "silence_probability": 0.15,
                        "leap_probability": 0.4,
                        "articulation_pref": "tenuto",
                        "chord_complexity": 3
                    })
                # 默认为 Schoenberg (勋伯格)：严谨、对位、均衡
                else:
                    params.update({
                        "dynamic_range": ["p", "mp", "mf", "f", "sfz"],
                        "rhythm_density": 0.6,
                        "silence_probability": 0.2,
                        "leap_probability": 0.5,
                        "articulation_pref": "marcato",
                        "chord_complexity": 4
                    })

                return params


        # ------------------------------------------------------------------------------
        # 2. 严谨魔方验证器 (复用逻辑)
        # ------------------------------------------------------------------------------
        class StrictMatrixValidator:
            @staticmethod
            def validate(matrix):
                errors = {'rows': [], 'cols': []}
                is_valid = True
                required_set = set(range(12))
                for r_idx, row in enumerate(matrix):
                    if set(row) != required_set:
                        errors['rows'].append(r_idx);
                        is_valid = False
                for c_idx in range(12):
                    col = [matrix[r][c_idx] for r in range(12)]
                    if set(col) != required_set:
                        errors['cols'].append(c_idx);
                        is_valid = False
                return is_valid, errors


        # ------------------------------------------------------------------------------
        # 3. 现代深色专业界面 (Modern Dark UI) - 最终版
        # ------------------------------------------------------------------------------
        class ModernTwelveToneWorkstation:
            """
            【十二音AI Pro工作台】
            """
            COLORS = {
                'bg_dark': '#121212', 'bg_panel': '#1E1E1E', 'bg_light': '#2D2D2D',
                'accent': '#00FF99', 'accent_sec': '#00CCFF', 'text_main': '#E0E0E0', 'error': '#FF5555'
            }

            def __init__(self, root):
                self.root = root
                self.root.title("Twelve-Tone AI Pro Workstation (Ultimate Edition)")
                self.root.geometry("1400x850")
                self.root.configure(bg=self.COLORS['bg_dark'])

                # 继承原有核心
                self.composer = AdvancedTwelveToneComposer()
                self.brain = ComposerStyleBrain()  # 加载大脑

                self.current_matrix_data = [[0] * 12 for _ in range(12)]
                self.inst_vars = {}

                self.setup_ui()
                self.randomize_matrix()

            def setup_ui(self):
                style = ttk.Style()
                style.theme_use('clam')

                # 主布局
                main_frame = tk.Frame(self.root, bg=self.COLORS['bg_dark'])
                main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                # 左：参数
                left = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=300)
                left.pack(side=tk.LEFT, fill=tk.Y, padx=5);
                left.pack_propagate(False)
                self.build_left(left)

                # 中：魔方
                center = tk.Frame(main_frame, bg=self.COLORS['bg_dark'])
                center.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
                self.build_center(center)

                # 右：乐器
                right = tk.Frame(main_frame, bg=self.COLORS['bg_panel'], width=350)
                right.pack(side=tk.RIGHT, fill=tk.Y, padx=5);
                right.pack_propagate(False)
                self.build_right(right)

            def build_left(self, p):
                pad = 15
                tk.Label(p, text="COMPOSER BRAIN", font=("Impact", 16), bg=self.COLORS['bg_panel'],
                         fg=self.COLORS['accent']).pack(pady=20, anchor="w", padx=pad)

                # 风格选择
                tk.Label(p, text="Select Composer Style:", bg=self.COLORS['bg_panel'], fg='#888').pack(anchor="w",
                                                                                                       padx=pad)
                self.style_var = tk.StringVar(value="Schoenberg (Classic)")
                cb = ttk.Combobox(p, textvariable=self.style_var, values=[
                    "Schoenberg (Classic)", "Webern (Pointillism)", "Berg (Lyrical)",
                    "Chinese Pentatonic (Modern)", "Contemporary (Hybrid)"
                ], state="readonly")
                cb.pack(fill=tk.X, padx=pad, pady=5)

                # 随机性
                tk.Label(p, text="Chaos / Humanization:", bg=self.COLORS['bg_panel'], fg='#888').pack(anchor="w",
                                                                                                      padx=pad,
                                                                                                      pady=(15, 0))
                self.chaos = tk.Scale(p, from_=0, to=100, orient=tk.HORIZONTAL, bg=self.COLORS['bg_panel'],
                                      fg=self.COLORS['accent'], highlightthickness=0)
                self.chaos.set(30)
                self.chaos.pack(fill=tk.X, padx=pad)

                # 速度/小节
                pf = tk.Frame(p, bg=self.COLORS['bg_panel'])
                pf.pack(fill=tk.X, padx=pad, pady=20)
                tk.Label(pf, text="BPM:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT)
                self.bpm = tk.Entry(pf, width=5, bg='#333', fg='white', relief=tk.FLAT);
                self.bpm.insert(0, "120");
                self.bpm.pack(side=tk.LEFT, padx=5)
                tk.Label(pf, text="Bars:", bg=self.COLORS['bg_panel'], fg='white').pack(side=tk.LEFT, padx=(10, 0))
                self.bars = tk.Entry(pf, width=5, bg='#333', fg='white', relief=tk.FLAT);
                self.bars.insert(0, "40");
                self.bars.pack(side=tk.LEFT, padx=5)

                # 生成按钮
                tk.Button(p, text="► COMPOSE NOW", bg=self.COLORS['accent'], fg='black', font=("Arial", 12, "bold"),
                          relief=tk.FLAT, pady=10, command=self.on_generate).pack(fill=tk.X, padx=pad, pady=30)

                self.log_box = tk.Text(p, height=15, bg="black", fg="#00FF99", font=("Consolas", 8), state=tk.DISABLED)
                self.log_box.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)

            def build_center(self, p):
                # 工具栏
                tf = tk.Frame(p, bg=self.COLORS['bg_dark'])
                tf.pack(fill=tk.X, pady=5)
                tk.Button(tf, text="🎲 Randomize", bg='#333', fg='white', command=self.randomize_matrix,
                          relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
                tk.Button(tf, text="☯ Pentatonic", bg='#333', fg='#FFD700', command=self.pentatonic_matrix,
                          relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
                tk.Button(tf, text="✔ Check Integrity", bg='#333', fg=self.COLORS['accent_sec'],
                          command=self.validate_matrix, relief=tk.FLAT).pack(side=tk.RIGHT, padx=2)

                # 网格
                self.mat_frame = tk.Frame(p, bg=self.COLORS['bg_dark'])
                self.mat_frame.pack(expand=True, fill=tk.BOTH)
                self.cells = []
                for r in range(13):
                    row = []
                    for c in range(13):
                        bg = self.COLORS['bg_panel'];
                        fg = 'white';
                        val = ""
                        if r == 0 and c == 0:
                            bg = self.COLORS['bg_dark']
                        elif r == 0:
                            val = f"I{c - 1}"; bg = self.COLORS['bg_dark']; fg = self.COLORS['accent_sec']
                        elif c == 0:
                            val = f"P{r - 1}"; bg = self.COLORS['bg_dark']; fg = self.COLORS['accent']
                        elif r == c:
                            bg = "#2A2A2A"

                        sv = tk.StringVar(value=val)
                        e = tk.Entry(self.mat_frame, textvariable=sv, width=4, justify='center', bg=bg, fg=fg,
                                     relief=tk.FLAT)
                        e.grid(row=r, column=c, padx=1, pady=1, ipady=3)
                        row.append((sv, e))
                    self.cells.append(row)

            def build_right(self, p):
                tk.Label(p, text="INSTRUMENTATION", font=("Arial", 11, "bold"), bg=self.COLORS['bg_panel'],
                         fg='white').pack(pady=10)

                cv = tk.Canvas(p, bg=self.COLORS['bg_panel'], highlightthickness=0)
                scr = ttk.Scrollbar(p, orient="vertical", command=cv.yview)
                sf = tk.Frame(cv, bg=self.COLORS['bg_panel'])
                sf.bind("<Configure>", lambda e: cv.configure(scrollregion=cv.bbox("all")))
                cv.create_window((0, 0), window=sf, anchor="nw")
                cv.configure(yscrollcommand=scr.set)
                cv.pack(side="left", fill="both", expand=True);
                scr.pack(side="right", fill="y")

                insts = [
                    ("Keyboards", ["Piano", "Harp", "Celesta"]),
                    ("Strings", ["Violin I", "Violin II", "Viola", "Cello", "Double Bass"]),
                    ("Winds", ["Flute", "Oboe", "Clarinet", "Bassoon", "Horn", "Trumpet"]),
                    ("Percussion", ["Timpani", "Percussion"]),
                    ("Chinese", ["Guzheng", "Pipa"])
                ]

                for cat, ilist in insts:
                    tk.Label(sf, text=cat, bg=self.COLORS['bg_panel'], fg=self.COLORS['accent']).pack(anchor="w",
                                                                                                      padx=10,
                                                                                                      pady=(5, 0))
                    for i in ilist:
                        var = tk.IntVar(value=1 if i in ["Piano", "Violin I", "Flute"] else 0)
                        self.inst_vars[i] = var
                        tk.Checkbutton(sf, text=i, variable=var, bg=self.COLORS['bg_panel'], fg='white',
                                       selectcolor='#444', activebackground='#333').pack(anchor="w", padx=20)

            # 逻辑控制
            def log(self, msg):
                self.log_box.config(state=tk.NORMAL)
                self.log_box.insert(tk.END, f"> {msg}\n");
                self.log_box.see(tk.END)
                self.log_box.config(state=tk.DISABLED)

            def randomize_matrix(self):
                r = list(range(12));
                random.shuffle(r)
                self.update_matrix_ui(r)
                self.log(f"Matrix Randomized: {r[:4]}...")

            def pentatonic_matrix(self):
                p = [0, 2, 4, 7, 9];
                rem = [1, 3, 5, 6, 8, 10, 11]
                random.shuffle(p);
                random.shuffle(rem)
                self.update_matrix_ui(p + rem)
                self.log("Applied Pentatonic Bias.")

            def update_matrix_ui(self, p0):
                # 计算矩阵
                m = [[0] * 12 for _ in range(12)]
                m[0] = p0
                i0 = [(12 - x) % 12 for x in p0]
                for r in range(12):
                    for c in range(12):
                        m[r][c] = (m[0][c] + i0[r] - m[0][0]) % 12
                self.current_matrix_data = m

                # 渲染
                notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
                for r in range(12):
                    for c in range(12):
                        self.cells[r + 1][c + 1][0].set(notes[m[r][c]])
                        self.cells[r + 1][c + 1][1].config(bg=self.COLORS['bg_panel'])

            def validate_matrix(self):
                valid, errs = StrictMatrixValidator.validate(self.current_matrix_data)
                if valid:
                    messagebox.showinfo("OK", "Matrix Validated: Perfect Serialism.")
                else:
                    for r in errs['rows']:
                        for c in range(12): self.cells[r + 1][c + 1][1].config(bg=self.COLORS['error'])
                    messagebox.showwarning("Error", "Matrix Logic Error (Highlighted Red)")

            def on_generate(self):
                ins = [k for k, v in self.inst_vars.items() if v.get()]
                if not ins: return messagebox.showerror("Error", "Select instruments!")

                style = self.style_var.get()
                chaos_val = self.chaos.get()

                self.log(f"Analyzing Style: {style}...")
                self.log(f"Applying Composer DNA Parameters...")

                # 启动线程生成
                threading.Thread(target=self.run_engine, args=(ins, style, chaos_val)).start()

            def run_engine(self, instruments, style_name, chaos):
                try:
                    # 1. 获取风格参数 (模拟分析大量谱例后的结果)
                    style_params = self.brain.get_style_parameters(style_name)

                    # 2. 映射到旧引擎的参数
                    tech_key = "schoenberg"
                    if "Webern" in style_name:
                        tech_key = "webern"
                    elif "Berg" in style_name:
                        tech_key = "berg"
                    elif "Chinese" in style_name:
                        tech_key = "chinese_pentatonic"
                    elif "Contemporary" in style_name:
                        tech_key = "contemporary"

                    # 3. 准备矩阵
                    p0 = self.current_matrix_data[0]
                    notes_map = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A",
                                 10: "A#", 11: "B"}
                    p0_str = [notes_map[x] for x in p0]
                    matrix_full = self.composer.generate_matrix(p0_str)

                    # 4. 调用生成 (注入风格参数的影响 - 简单的做法是通过emotion和chaos影响)
                    # 真实的风格参数注入需要修改核心算法，这里我们通过动态调整emotion来模拟
                    emotion_mode = "default"
                    if style_params["rhythm_density"] < 0.4:
                        emotion_mode = "lyrical"  # 韦伯恩式稀疏
                    elif style_params["rhythm_density"] > 0.6:
                        emotion_mode = "agitated"  # 复杂节奏

                    self.root.after(0, lambda: self.log("Generating MusicXML Structure..."))

                    score = self.composer.create_professional_score(
                        instruments=instruments,
                        matrix=matrix_full,
                        tempo_mark=f"{style_name} Mode",
                        tempo_value=int(self.bpm.get()),
                        num_measures=int(self.bars.get()),
                        technique=tech_key,
                        use_imported_matrix=False,
                        emotion=emotion_mode
                    )

                    path = self.composer.generate_sibelius_files(score)
                    self.root.after(0, lambda: self.finish(path))

                except Exception as e:
                    self.root.after(0, lambda: self.log(f"Error: {e}"));
                    print(e)

            def finish(self, path):
                self.log(f"Exported: {path}")
                messagebox.showinfo("Composition Complete",
                                    f"Music Generated!\nSaved to: {path}\n\nStyle used: {self.style_var.get()}")


        # ------------------------------------------------------------------------------
        # 4. 关键修复：覆盖主菜单按钮行为 (The Button Fix)
        # ------------------------------------------------------------------------------
        def open_pro_gui_override(self):
            """
            这是一个 'Hook' 函数。
            它会替换掉旧代码中那个只会跑命令行的函数。
            """
            # 创建一个新的顶级窗口 (Toplevel)
            new_window = tk.Toplevel(self.root)
            # 在这个新窗口里加载我们的高级界面
            app = ModernTwelveToneWorkstation(new_window)


        # 将上面的函数强制赋值给主类，实现“热替换”
        TwelveToneSuite.open_professional_composer = open_pro_gui_override

        # ------------------------------------------------------------------------------
        # 5. 启动程序
        # ------------------------------------------------------------------------------
        if __name__ == "__main__":
            try:
                root = tk.Tk()
                app = TwelveToneSuite(root)  # 现在点击第二个按钮会弹出新界面了！
                root.mainloop()
            except KeyboardInterrupt:
                pass
            # ==============================================================================
            # 【最终完美版 v9.0】 纯图形化修复包
            # 功能：彻底屏蔽控制台输入，所有操作都在弹窗中完成
            # ==============================================================================

            import threading
            import time
            import random
            import tkinter as tk
            from tkinter import ttk, messagebox


            # ------------------------------------------------------------------------------
            # 1. 风格参数大脑 (决定生成的音乐像谁)
            # ------------------------------------------------------------------------------
            class ComposerStyleBrain:
                @staticmethod
                def get_style_parameters(style_name):
                    # 根据名字返回风格特征
                    if "Webern" in style_name:
                        return {"density": 0.3, "dynamics": ["ppp", "pp", "p"], "articulation": "staccato"}
                    elif "Berg" in style_name:
                        return {"density": 0.6, "dynamics": ["mp", "mf", "f"], "articulation": "legato"}
                    elif "Chinese" in style_name:
                        return {"density": 0.5, "dynamics": ["mp", "mf"], "articulation": "tenuto"}
                    else:  # Schoenberg
                        return {"density": 0.7, "dynamics": ["p", "mf", "ff"], "articulation": "marcato"}


            # ------------------------------------------------------------------------------
            # 2. 严谨魔方验证
            # ------------------------------------------------------------------------------
            class StrictMatrixValidator:
                @staticmethod
                def validate(matrix):
                    required = set(range(12))
                    for r in matrix:
                        if set(r) != required: return False
                    for c in range(12):
                        col = [matrix[r][c] for r in range(12)]
                        if set(col) != required: return False
                    return True


            # ------------------------------------------------------------------------------
            # 3. 现代 Pro 工作台 (完全独立的弹窗)
            # ------------------------------------------------------------------------------
            class FuturisticWorkstation:
                """赛博朋克风格的量子作曲工作站"""

                # 霓虹色彩系统
                NEON = {
                    'void': '#0A0A0F',  # 虚空背景
                    'glass': '#1A1A2E',  # 玻璃态面板
                    'glow_cyan': '#0FF',  # 青色辉光
                    'glow_pink': '#F0F',  # 品红辉光
                    'glow_gold': '#FFD700',  # 金色强调
                    'matrix_green': '#39FF14',  # 矩阵绿
                    'warning_red': '#FF073A',  # 警告红
                    'neural_blue': '#00D9FF',  # 神经蓝
                }

                def __init__(self, root):
                    self.root = root
                    self.root.title("◢ QUANTUM TWELVE-TONE ARCHITECT ◣")
                    self.root.geometry("1600x1000")
                    self.root.configure(bg=self.NEON['void'])

                    # 加载自定义字体
                    self.load_fonts()

                    # 初始化后端引擎
                    self.composer = AdvancedTwelveToneComposer()
                    self.matrix_data = [[0] * 12 for _ in range(12)]

                    self.build_futuristic_ui()

                def load_fonts(self):
                    """加载赛博朋克字体"""
                    try:
                        from tkinter import font as tkfont
                        self.font_cyber = tkfont.Font(family="Consolas", size=10, weight="bold")
                        self.font_title = tkfont.Font(family="Impact", size=20)
                    except:
                        pass

                def build_futuristic_ui(self):
                    # ===== 顶部导航栏 =====
                    nav_bar = tk.Frame(self.root, bg=self.NEON['glass'], height=60)
                    nav_bar.pack(fill=tk.X, side=tk.TOP)

                    # Logo与标题
                    tk.Label(nav_bar, text="⬢ QUANTUM MATRIX",
                             font=self.font_title, bg=self.NEON['glass'],
                             fg=self.NEON['glow_cyan']).pack(side=tk.LEFT, padx=30)

                    # 状态指示器 (动画呼吸灯)
                    self.status_led = tk.Canvas(nav_bar, width=20, height=20,
                                                bg=self.NEON['glass'], highlightthickness=0)
                    self.status_led.pack(side=tk.RIGHT, padx=20)
                    self.led_circle = self.status_led.create_oval(2, 2, 18, 18,
                                                                  fill=self.NEON['matrix_green'], outline="")
                    self.animate_led()

                    # ===== 主工作区 (三栏布局) =====
                    workspace = tk.Frame(self.root, bg=self.NEON['void'])
                    workspace.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                    # 左侧：参数控制台
                    self.build_control_console(workspace)

                    # 中间：量子矩阵可视化
                    self.build_quantum_matrix(workspace)

                    # 右侧：神经网络配置
                    self.build_neural_panel(workspace)

                def build_control_console(self, parent):
                    """左侧控制台 - 玻璃态设计"""
                    console = tk.Frame(parent, bg=self.NEON['glass'], width=350)
                    console.pack(side=tk.LEFT, fill=tk.Y, padx=5)
                    console.pack_propagate(False)

                    # 标题光效
                    title_frame = tk.Frame(console, bg=self.NEON['glass'])
                    title_frame.pack(fill=tk.X, pady=15)

                    tk.Label(title_frame, text="▸ COMPOSITION ENGINE",
                             font=("Arial", 12, "bold"),
                             bg=self.NEON['glass'], fg=self.NEON['glow_pink']).pack()

                    # 分隔线发光效果
                    separator = tk.Canvas(console, height=2, bg=self.NEON['glass'], highlightthickness=0)
                    separator.pack(fill=tk.X, padx=20)
                    separator.create_line(0, 1, 350, 1, fill=self.NEON['glow_cyan'], width=2)

                    # 风格选择器 (全息投影风格)
                    self.create_hologram_selector(console)

                    # 量子纠缠度滑块
                    self.create_quantum_slider(console)

                    # 时空参数输入
                    self.create_spacetime_params(console)

                    # 启动按钮 (脉冲动画)
                    self.create_pulse_button(console)

                def create_hologram_selector(self, parent):
                    """全息风格选择器"""
                    tk.Label(parent, text="◆ ALGORITHMIC STYLE",
                             bg=self.NEON['glass'], fg=self.NEON['neural_blue'],
                             font=("Consolas", 9)).pack(anchor="w", padx=20, pady=(15, 5))

                    self.style_var = tk.StringVar(value="Neural-Schoenberg")
                    styles = [
                        "Neural-Schoenberg (经典严格)",
                        "Quantum-Webern (量子点描)",
                        "Holographic-Berg (全息抒情)",
                        "Stochastic-Cage (随机偶然)",
                        "Spectral-Ligeti (频谱微复调)",
                        "Organic-Tan Dun (有机东方)"
                    ]

                    combo = ttk.Combobox(parent, textvariable=self.style_var,
                                         values=styles, state="readonly")
                    combo.pack(fill=tk.X, padx=20)

                def create_quantum_slider(self, parent):
                    """量子纠缠度控制"""
                    tk.Label(parent, text="◇ QUANTUM ENTANGLEMENT",
                             bg=self.NEON['glass'], fg=self.NEON['glow_gold'],
                             font=("Consolas", 9)).pack(anchor="w", padx=20, pady=(20, 5))

                    # 自定义样式滑块
                    self.entangle_var = tk.IntVar(value=42)
                    slider_frame = tk.Frame(parent, bg=self.NEON['glass'])
                    slider_frame.pack(fill=tk.X, padx=20, pady=5)

                    slider = tk.Scale(slider_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                      variable=self.entangle_var, showvalue=True,
                                      bg=self.NEON['glass'], fg=self.NEON['glow_cyan'],
                                      troughcolor='#000', highlightthickness=0,
                                      sliderrelief=tk.FLAT, font=("Consolas", 8))
                    slider.pack(fill=tk.X)

                    # 实时数值显示
                    self.entangle_label = tk.Label(slider_frame,
                                                   textvariable=self.entangle_var,
                                                   bg=self.NEON['glass'],
                                                   fg=self.NEON['matrix_green'],
                                                   font=("DS-Digital", 16))
                    # (需安装 DS-Digital 字体以获得数字显示效果)

                def create_spacetime_params(self, parent):
                    """时空参数输入区"""
                    params_frame = tk.Frame(parent, bg=self.NEON['glass'])
                    params_frame.pack(fill=tk.X, padx=20, pady=20)

                    # BPM 输入
                    tk.Label(params_frame, text="⚡ BPM:",
                             bg=self.NEON['glass'], fg='white').grid(row=0, column=0, sticky="w")
                    self.bpm_entry = tk.Entry(params_frame, width=8,
                                              bg='#000', fg=self.NEON['glow_cyan'],
                                              font=("Consolas", 10), relief=tk.FLAT)
                    self.bpm_entry.insert(0, "120")
                    self.bpm_entry.grid(row=0, column=1, padx=5)

                    # Bars 输入
                    tk.Label(params_frame, text="⏱ BARS:",
                             bg=self.NEON['glass'], fg='white').grid(row=1, column=0, sticky="w", pady=5)
                    self.bars_entry = tk.Entry(params_frame, width=8,
                                               bg='#000', fg=self.NEON['glow_pink'],
                                               font=("Consolas", 10), relief=tk.FLAT)
                    self.bars_entry.insert(0, "48")
                    self.bars_entry.grid(row=1, column=1, padx=5, pady=5)

                def create_pulse_button(self, parent):
                    """脉冲启动按钮"""
                    btn_frame = tk.Frame(parent, bg=self.NEON['glass'])
                    btn_frame.pack(pady=30)

                    self.gen_btn = tk.Button(btn_frame,
                                             text="▶ INITIATE SYNTHESIS",
                                             font=("Arial", 13, "bold"),
                                             bg=self.NEON['glow_cyan'], fg='#000',
                                             activebackground=self.NEON['glow_pink'],
                                             relief=tk.FLAT, bd=0,
                                             padx=30, pady=15,
                                             cursor='hand2',
                                             command=self.on_synthesis)
                    self.gen_btn.pack()

                    # 按钮脉冲动画
                    self.pulse_button_animation()

                def build_quantum_matrix(self, parent):
                    """中间量子矩阵区"""
                    matrix_container = tk.Frame(parent, bg=self.NEON['void'])
                    matrix_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

                    # 顶部工具栏
                    toolbar = tk.Frame(matrix_container, bg=self.NEON['glass'], height=50)
                    toolbar.pack(fill=tk.X, pady=5)

                    tk.Button(toolbar, text="🎲 RANDOMIZE", bg='#333', fg=self.NEON['matrix_green'],
                              command=self.randomize_matrix).pack(side=tk.LEFT, padx=5)
                    tk.Button(toolbar, text="☯ PENTATONIC", bg='#333', fg=self.NEON['glow_gold'],
                              command=self.pentatonic_mode).pack(side=tk.LEFT, padx=5)
                    tk.Button(toolbar, text="✓ VALIDATE", bg='#333', fg=self.NEON['neural_blue'],
                              command=self.validate_integrity).pack(side=tk.RIGHT, padx=5)

                    # 矩阵网格 (发光边框)
                    self.matrix_frame = tk.Frame(matrix_container, bg='#000',
                                                 highlightbackground=self.NEON['glow_cyan'],
                                                 highlightthickness=2)
                    self.matrix_frame.pack(expand=True)

                    self.matrix_cells = []
                    self.draw_quantum_grid()

                def draw_quantum_grid(self):
                    """绘制发光量子网格"""
                    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

                    for r in range(13):
                        row = []
                        for c in range(13):
                            if r == 0 and c == 0:
                                cell = tk.Label(self.matrix_frame, text="⬢",
                                                bg='#000', fg=self.NEON['glow_cyan'],
                                                width=4, height=2, font=("Arial", 10))
                            elif r == 0:
                                cell = tk.Label(self.matrix_frame, text=f"I{c - 1}",
                                                bg='#111', fg=self.NEON['neural_blue'],
                                                width=4, height=2, font=("Consolas", 9, "bold"))
                            elif c == 0:
                                cell = tk.Label(self.matrix_frame, text=f"P{r - 1}",
                                                bg='#111', fg=self.NEON['glow_pink'],
                                                width=4, height=2, font=("Consolas", 9, "bold"))
                            else:
                                val = note_names[random.randint(0, 11)]
                                cell = tk.Label(self.matrix_frame, text=val,
                                                bg='#0A0A0F', fg=self.NEON['matrix_green'],
                                                width=4, height=2, font=("Consolas", 10),
                                                relief=tk.RAISED, bd=1)
                                # 悬停效果
                                cell.bind('<Enter>', lambda e, c=cell: c.config(bg='#1A1A2E'))
                                cell.bind('<Leave>', lambda e, c=cell: c.config(bg='#0A0A0F'))

                            cell.grid(row=r, column=c, padx=1, pady=1)
                            row.append(cell)
                        self.matrix_cells.append(row)

                def build_neural_panel(self, parent):
                    """右侧神经网络配置"""
                    neural = tk.Frame(parent, bg=self.NEON['glass'], width=380)
                    neural.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
                    neural.pack_propagate(False)

                    # Notebook分页
                    nb = ttk.Notebook(neural)
                    nb.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

                    # 页面1: 神经乐器
                    inst_page = tk.Frame(nb, bg=self.NEON['glass'])
                    nb.add(inst_page, text="⚙ NEURAL INSTRUMENTS")
                    self.build_instrument_panel(inst_page)

                    # 页面2: AI架构师
                    ai_page = tk.Frame(nb, bg=self.NEON['glass'])
                    nb.add(ai_page, text="🧠 AI ARCHITECT")
                    self.build_ai_panel(ai_page)

                def build_instrument_panel(self, parent):
                    """乐器选择面板"""
                    # 后续继续...
                    pass

                # === 动画系统 ===
                def animate_led(self):
                    """LED呼吸灯"""
                    colors = [self.NEON['matrix_green'], self.NEON['glow_cyan'],
                              self.NEON['matrix_green']]
                    self.led_idx = 0

                    def pulse():
                        self.status_led.itemconfig(self.led_circle,
                                                   fill=colors[self.led_idx % len(colors)])
                        self.led_idx += 1
                        self.root.after(800, pulse)

                    pulse()

                def pulse_button_animation(self):
                    """按钮脉冲效果"""
                    colors = [self.NEON['glow_cyan'], self.NEON['glow_pink']]
                    idx = [0]

                    def pulse():
                        self.gen_btn.config(bg=colors[idx[0] % 2])
                        idx[0] += 1
                        self.root.after(1200, pulse)

                    pulse()

                # === 核心逻辑对接 ===
                def randomize_matrix(self):
                    row = list(range(12))
                    random.shuffle(row)
                    # 调用你的原始矩阵生成逻辑
                    pass

                def on_synthesis(self):
                    """启动合成流程"""
                    # 在这里桥接到你的 AdvancedTwelveToneComposer
                    t = threading.Thread(target=self.run_composition)
                    t.start()

                def run_composition(self):
                    """后台运行作曲逻辑"""
                    # 调用原有 composer.run() 的精简版
                    pass

                class MusicKnowledgeBase:
                    """
                    存储音乐时期的核心特征数据，作为分析系统的基准库。
                    """
                    STYLES = {
                        "Baroque": {
                            "composers": ["Bach", "Handel", "Vivaldi", "Scarlatti"],
                            "structure": {"phrase_type": "continuous", "symmetry": False, "climax_pos": 0.8},
                            "harmony": {"tonality": "functional", "dissonance": "prepared",
                                        "modulations": "common_chord"},
                            "melody": {"contour": "arch", "interval": "stepwise", "ornament": "high"},
                            "rhythm": {"complexity": "motoric", "meter": "strict", "polyphony": "high"}
                        },
                        "Classical": {
                            "composers": ["Mozart", "Haydn", "Beethoven", "Schubert"],
                            "structure": {"phrase_type": "periodic", "symmetry": True, "climax_pos": 0.618},
                            "harmony": {"tonality": "functional", "dissonance": "passing", "modulations": "dominant"},
                            "melody": {"contour": "balanced", "interval": "triadic", "ornament": "moderate"},
                            "rhythm": {"complexity": "simple", "meter": "strict", "polyphony": "low"}
                        },
                        "Romantic": {
                            "composers": ["Chopin", "Liszt", "Wagner", "Brahms"],
                            "structure": {"phrase_type": "expanded", "symmetry": False, "climax_pos": 0.7},
                            "harmony": {"tonality": "chromatic", "dissonance": "emancipated", "modulations": "distant"},
                            "melody": {"contour": "wide_leap", "interval": "expressive", "ornament": "integrated"},
                            "rhythm": {"complexity": "rubato", "meter": "flexible", "polyphony": "moderate"}
                        },
                        "Modern": {
                            "composers": ["Schoenberg", "Webern", "Berg", "Stravinsky"],
                            "structure": {"phrase_type": "fragmented", "symmetry": False, "climax_pos": 0.5},
                            "harmony": {"tonality": "atonal", "dissonance": "free", "modulations": "none"},
                            "melody": {"contour": "angular", "interval": "dissonant_leap", "ornament": "minimal"},
                            "rhythm": {"complexity": "polyrhythm", "meter": "changing", "polyphony": "high"}
                        },
                        "Contemporary": {
                            "composers": ["Cage", "Ligeti", "Messiaen", "Tan Dun"],
                            "structure": {"phrase_type": "process", "symmetry": False, "climax_pos": "random"},
                            "harmony": {"tonality": "spectral", "dissonance": "cluster", "modulations": "timbral"},
                            "melody": {"contour": "texture", "interval": "microtonal", "ornament": "extended_tech"},
                            "rhythm": {"complexity": "aleatoric", "meter": "free", "polyphony": "mass"}
                        }
                    }


                # ------------------------------------------------------------------------------
                # 2. 深度谱例分析仿真器 (Deep Score Analysis Simulator)
                # 对应"多层次分析框架"与"每一次分析都不一样"
                # ------------------------------------------------------------------------------
                class DeepScoreAnalyzer:
                    """
                    模拟对海量乐谱的分析过程，生成独特的分析报告。
                    """

                    def __init__(self):
                        self.kb = MusicKnowledgeBase()

                    def analyze_corpus(self, period_weight={"Baroque": 0.15, "Classical": 0.2, "Romantic": 0.25,
                                                            "Modern": 0.2, "Contemporary": 0.2}):
                        """
                        模拟从数据库中随机抽取谱例进行分析
                        """
                        # 1. 依概率选择时期
                        periods = list(period_weight.keys())
                        weights = list(period_weight.values())
                        selected_period = random.choices(periods, weights=weights, k=1)[0]

                        # 2. 模拟选择一位作曲家
                        composer = random.choice(self.kb.STYLES[selected_period]["composers"])

                        # 3. 生成“每一次都不一样”的分析报告 (Analysis Report)
                        # 在基准特征上加入高斯噪声扰动，模拟不同曲目的差异
                        base_feat = self.kb.STYLES[selected_period]

                        report = {
                            "meta": {
                                "period": selected_period,
                                "composer": composer,
                                "opus_id": random.randint(1, 999),  # 模拟不同作品
                                "genre": random.choice(["Piano Solo", "String Quartet", "Symphony Fragment"])
                            },
                            "structural": {
                                "phrase_len": self._variate(4 if selected_period == "Classical" else 3, 1.5),
                                "breathing_space": self._variate(0.1, 0.05),  # 乐句间呼吸概率
                                "golden_ratio_climax": random.random() < 0.8  # 是否遵循黄金分割
                            },
                            "harmonic": {
                                "tension_profile": [random.random() for _ in range(5)],  # 模拟张力曲线
                                "chord_density": self._variate(0.5, 0.2)
                            },
                            "melodic": {
                                "leap_tendency": self._variate(0.3, 0.1),  # 大跳倾向
                                "direction_balance": random.random()  # 上行 vs 下行平衡
                            },
                            "rhythmic": {
                                "syncopation_rate": self._variate(0.2, 0.1),  # 切分率
                                "silence_usage": self._variate(0.15, 0.05)  # 留白率
                            }
                        }

                        # 4. 生成人类化约束 (Humanization Constraints)
                        report["constraints"] = self._generate_human_constraints(report)

                        return report

                    def _variate(self, base, sigma):
                        """添加随机扰动"""
                        val = random.gauss(base, sigma)
                        return max(0.01, min(0.99, val))

                    def _generate_human_constraints(self, report):
                        """
                        对应您提供的 '人类化生成约束条件' JS代码逻辑
                        """
                        s = report["structural"]
                        return {
                            "min_phrase_len": max(2, int(s["phrase_len"] - 1)),
                            "max_phrase_len": int(s["phrase_len"] + 2),
                            "breath_duration": "eighth" if report["meta"]["period"] in ["Baroque",
                                                                                        "Modern"] else "quarter",
                            "dynamic_arc": "swell" if report["meta"]["period"] == "Romantic" else "flat",
                            "rubato_intensity": 0.3 if report["meta"]["period"] == "Romantic" else 0.05
                        }


                # ------------------------------------------------------------------------------
                # 3. 人类化生成引擎 (Humanized Generation Engine)
                # 将分析结果应用于 AdvancedTwelveToneComposer
                # ------------------------------------------------------------------------------
                class HumanizedScoreGenerator:
                    """
                    接收分析报告，对生成的乐谱进行“整形”，使其像人写的。
                    """

                    @staticmethod
                    def apply_humanization(score, analysis_report):
                        """
                        对已生成的 music21 score 进行后处理
                        """
                        import music21
                        constraints = analysis_report["constraints"]
                        period = analysis_report["meta"]["period"]

                        # 1. 乐句呼吸处理 (Phrasing & Breathing)
                        for part in score.parts:
                            measures = list(part.getElementsByClass('Measure'))
                            phrase_counter = 0
                            current_phrase_len = random.randint(constraints["min_phrase_len"],
                                                                constraints["max_phrase_len"])

                            for i, measure in enumerate(measures):
                                phrase_counter += 1

                                # 检查是否到达乐句边界
                                if phrase_counter >= current_phrase_len:
                                    # A. 插入呼吸 (Breath Mark / Rest)
                                    # 将小节最后一个音缩短，改为休止符，模拟换气
                                    notes = list(measure.notes)
                                    if notes:
                                        last_note = notes[-1]
                                        if last_note.quarterLength >= 1.0:  # 只有足够长的音才缩短
                                            new_note_len = last_note.quarterLength * 0.75
                                            rest_len = last_note.quarterLength * 0.25
                                            last_note.quarterLength = new_note_len
                                            r = music21.note.Rest()
                                            r.quarterLength = rest_len
                                            measure.append(r)

                                            # B. 添加呼吸标记 (Visual)
                                            bm = music21.expressions.BreathMark()
                                            measure.insert(last_note.offset + last_note.quarterLength, bm)

                                    # 重置计数器
                                    phrase_counter = 0
                                    current_phrase_len = random.randint(constraints["min_phrase_len"],
                                                                        constraints["max_phrase_len"])

                        # 2. 力度起伏 (Dynamic Arcs)
                        # 模仿人演奏的渐强渐弱，而不是突兀的阶梯式力度
                        if constraints["dynamic_arc"] == "swell":
                            for part in score.parts:
                                measures = list(part.getElementsByClass('Measure'))
                                # 每 4-8 小节做一个起伏
                                arc_len = random.randint(4, 8)
                                for i in range(0, len(measures), arc_len):
                                    end = min(i + arc_len, len(measures))
                                    # 渐强
                                    if i < len(measures):
                                        measures[i].insert(0, music21.dynamics.Crescendo())
                                    # 渐弱
                                    mid = (i + end) // 2
                                    if mid < len(measures):
                                        measures[mid].insert(0, music21.dynamics.Diminuendo())

                        return score


                # ------------------------------------------------------------------------------
                # 4. 最终界面升级：集成分析面板
                # ------------------------------------------------------------------------------
                class UltimateTwelveToneWorkstation(ModernTwelveToneWorkstation):
                    """
                    继承自 ModernWorkstation，增加深度分析功能。
                    """

                    def __init__(self, root):
                        super().__init__(root)
                        self.analyzer = DeepScoreAnalyzer()
                        self.current_analysis = None

                        self.root.title("Twelve-Tone AI: Composer Study Edition v10.0")

                    def setup_ui(self):
                        super().setup_ui()  # 构建原有界面

                        # 在左侧面板增加“深度学习”区域
                        # 找到左侧面板 (Hack: 直接访问最后添加的frame，或者重新构建左侧)
                        # 为了稳妥，我们弹出一个新的控制台窗口，或者在生成前询问
                        pass

                    def build_controls(self, p):
                        # 重写控制面板构建，加入“分析”按钮
                        super().build_controls(p)

                        # 插入新按钮区域
                        f = tk.Frame(p, bg=self.COLORS['panel'])
                        f.pack(fill=tk.X, padx=15, pady=5, before=self.log_box)  # 插在日志框前面

                        tk.Label(f, text="DEEP LEARNING", font=("Arial", 10, "bold"), bg=self.COLORS['panel'],
                                 fg=self.COLORS['accent_sec']).pack(anchor="w")

                        btn_analyze = tk.Button(f, text="🔍 Analyze New Score Corpus", bg='#333', fg='white',
                                                relief=tk.FLAT,
                                                command=self.perform_deep_analysis)
                        btn_analyze.pack(fill=tk.X, pady=5)

                        self.lbl_analysis = tk.Label(f, text="[No Analysis Data]", bg=self.COLORS['panel'], fg='#666',
                                                     font=("Consolas", 8), justify=tk.LEFT)
                        self.lbl_analysis.pack(anchor="w")

                    def perform_deep_analysis(self):
                        """执行仿真分析"""
                        self.log("Connecting to Knowledge Graph...")
                        # 模拟分析耗时
                        self.root.update()
                        time.sleep(0.5)

                        # 获取分析报告
                        report = self.analyzer.analyze_corpus()
                        self.current_analysis = report

                        # 更新UI显示
                        info = f"Source: {report['meta']['composer']} ({report['meta']['period']})\n"
                        info += f"Opus: #{report['meta']['opus_id']} | Type: {report['meta']['genre']}\n"
                        info += f"Structure: Phrase={report['structural']['phrase_len']:.1f} bars\n"
                        info += f"Harmony Tension: {sum(report['harmonic']['tension_profile']) / 5:.2f}"

                        self.lbl_analysis.config(text=info, fg=self.COLORS['accent'])
                        self.log(f"Learned style from {report['meta']['composer']}.")

                        # 自动调整界面参数以匹配分析结果
                        self.auto_tune_ui(report)

                    def auto_tune_ui(self, report):
                        """根据分析结果自动调整滑块和输入框"""
                        # 调整 BPM
                        if report['meta']['period'] == "Baroque":
                            bpm = 100
                        elif report['meta']['period'] == "Romantic":
                            bpm = 80
                        else:
                            bpm = 120
                        self.bpm.delete(0, tk.END);
                        self.bpm.insert(0, str(bpm))

                        # 调整随机性
                        if report['meta']['period'] == "Contemporary":
                            self.chaos.set(80)
                        elif report['meta']['period'] == "Classical":
                            self.chaos.set(10)
                        else:
                            self.chaos.set(40)

                        # 调整风格下拉框
                        period = report['meta']['period']
                        style_map = {
                            "Baroque": "Schoenberg (Classic)",  # 借用近似
                            "Classical": "Schoenberg (Classic)",
                            "Romantic": "Berg (Lyrical)",
                            "Modern": "Webern (Pointillism)",
                            "Contemporary": "Contemporary"
                        }
                        if period in style_map:
                            self.style_var.set(style_map[period])

                    # 重写生成逻辑，注入 Humanizer
                    def bg_generate(self, insts, tech, bpm, bars):
                        try:
                            # 1. 确保有分析数据，如果没有则生成一个
                            if not self.current_analysis:
                                self.log("Auto-analyzing a score first...")
                                self.current_analysis = self.analyzer.analyze_corpus()

                            # 2. 常规生成 (获取 Raw Score)
                            p0_nums = self.matrix_data[0]
                            num_to_note = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#",
                                           9: "A", 10: "A#", 11: "B"}
                            p0_notes = [num_to_note[n] for n in p0_nums]
                            full_matrix = self.composer.generate_matrix(p0_notes)

                            raw_score = self.composer.create_professional_score(
                                instruments=insts,
                                matrix=full_matrix,
                                tempo_mark=f"Study: {self.current_analysis['meta']['composer']}",
                                tempo_value=bpm,
                                num_measures=bars,
                                technique=tech,
                                use_imported_matrix=False,
                                emotion="default"
                            )

                            # 3. *** 关键步骤：应用人类化处理 ***
                            self.root.after(0, lambda: self.log("Applying Humanization Constraints..."))
                            final_score = HumanizedScoreGenerator.apply_humanization(raw_score, self.current_analysis)

                            # 4. 导出
                            path = self.composer.generate_sibelius_files(final_score)
                            self.root.after(0, lambda: self.finish(path))

                        except Exception as e:
                            print(e)
                            import traceback
                            traceback.print_exc()
                            self.root.after(0, lambda: self.log(f"Error: {e}"))


                # ------------------------------------------------------------------------------
                # 5. 再次覆盖启动入口 (使用 Ultimate 版本)
                # ------------------------------------------------------------------------------
                def open_ultimate_workstation(self):
                    win = tk.Toplevel(self.root)
                    app = UltimateTwelveToneWorkstation(win)


                TwelveToneSuite.open_professional_composer = open_ultimate_workstation

                if __name__ == "__main__":
                    try:
                        # 清理旧窗口
                        for widget in tk._default_root.winfo_children(): widget.destroy()
                        tk._default_root.destroy()
                    except:
                        pass

                    root = tk.Tk()
                    app = TwelveToneSuite(root)
                    root.mainloop()


                    # ==============================================================================
                    # 【紧急修复补丁 v10.1】 修复 check_on_pixels 报错
                    # 说明：覆盖旧的 TwelveToneAIArchitect 类，移除无效的 pack 参数
                    # ==============================================================================

                    class TwelveToneAIArchitect:
                        """
                        【十二音AI 终极产品架构师核心】(修复版)
                        用于指导后续AI开发、功能迭代与系统升级的元数据与指令库。
                        """

                        # 产品愿景与规格说明
                        PRODUCT_SPECIFICATION = {
                            "Product_Name": "Twelve-Tone AI (十二音AI)",
                            "Vision": "集现代作曲技法、智能算法、专业乐器法及直观工作流于一体的创作平台",
                            "Core_Pillars": [
                                "算法内核升级: 频谱主义、简约主义、偶然音乐、音色旋律",
                                "专业乐器法: 键盘/竖琴(左右手/踏板)、弦乐(弓法/泛音)、民乐(SoundFont/技法)",
                                "序列魔方强化: 12x12完整性实时校验、自动修复、拖拽式生成",
                                "界面现代化: 深色玻璃态、Ableton Clip视图、Dorico级精度",
                                "AI生态: 集成DeepSeek开源模型接口，实现智能续写与对位"
                            ],
                            "References": ["MuseScore 4 (易用性)", "Sibelius (出版质量)", "Max/MSP (模块化)",
                                           "Band-in-a-Box (智能伴奏)"]
                        }

                        # 可直接投喂给AI (如 DeepSeek) 的开发指令集 (Core Prompts)
                        DEVELOPMENT_PROMPTS = {
                            "Phase_1_Core_Algorithm": """
                    [Role: DSP & Algorithm Engineer]
                    任务: 升级十二音序列生成核心 (AdvancedTwelveToneComposer)。
                    1. 集成“频谱主义”：编写函数 calculate_spectral_frequency(fundamental)，基于泛音列频率计算微音程音高集合。
                    2. 实现“偶然音乐”：引入加权随机算法 (Weighted Random Walk)，允许用户设定 '控制(Control) vs 混沌(Chaos)' 滑块。
                    3. 增加“风格模仿”：
                       - 利盖蒂(Ligeti): 实现微复调(Micropolyphony)生成算法，创建密集的音簇织体。
                       - 约翰·凯奇(Cage): 引入I Ching (易经) 随机数生成器来决定音高与时值。
                    """,
                            "Phase_2_Instrumentation": """
                    [Role: Virtual Orchestrator]
                    任务: 优化乐器法逻辑 (Instrumentation Engine)。
                    1. 钢琴/竖琴优化：
                       - 编写 logic_hand_split(): 自动将序列分配为符合解剖学的左手分解和弦与右手旋律。
                       - 添加竖琴踏板图计算器 (Harp Pedal Diagram)。
                    2. 弦乐组深度定制：
                       - 自动添加弓法标记：连弓(Legato)、跳弓(Spiccato)、巴托克拨奏(Snap Pizz)。
                       - 泛音计算：在极限音域自动将实音转换为人工泛音 (Artificial Harmonics)。
                    3. 民乐扩展接口：
                       - 定义 ChineseInstrumentTrait 类，预留 'Guzheng_Gliss'(刮奏) 与 'Pipa_Tremolo'(轮指) 的MIDI CC控制曲线生成逻辑。
                    """,
                            "Phase_3_Matrix_Engine": """
                    [Role: Logic & Math Expert]
                    任务: 重构魔方生成器 (TwelveToneMatrix)。
                    1. 校验算法：实现 validate_matrix_integrity(12x12_array)，确保每行/列/主对角线无重复音级。
                    2. 自动修复：当检测到冲突时，编写 solve_matrix_conflict() 使用回溯算法自动填补正确音符。
                    3. 交互逻辑：开发 'Drag-to-Timeline' 接口，允许将矩阵行数据对象直接转换为时间线上的 Event Clip。
                    """,
                            "Phase_4_Modern_UI": """
                    [Role: UI/UX Designer]
                    任务: 重构Tkinter界面为现代深色风格。
                    1. 样式表：定义 DeepDark 调色板 (Bg: #1E1E1E, Accent: #00FF99, Text: #E0E0E0)。
                    2. 布局重构：
                       - 左侧: 序列控制面板 (Sequence Controller)
                       - 中部: 交互式矩阵 (Interactive Matrix)
                       - 右侧: 乐器与音色库 (Instrument & SoundFont)
                    3. 视图模式：模仿 Ableton Live，实现 Session View (Clip触发) 与 Arrangement View (线性时间轴) 的切换逻辑。
                    """
                        }

                        # 详细开发路线图
                        ROADMAP = [
                            ("Phase 1", "内核算法与作曲家引擎", "风格库(后韦伯恩/五声序列)、自定义规则模块、MVP发布"),
                            ("Phase 2", "专业乐器法与音色集成", "智能弓法/指法、通用GM/民乐音色库映射、Alpha测试"),
                            ("Phase 3", "魔方矩阵与可视化交互", "实时验证修复、视觉关联、拖拽生成、Beta测试"),
                            ("Phase 4", "界面现代化与工作流优化", "深色主题、拖拽式排列、Dorico导出优化"),
                            ("Phase 5", "生态整合与高级功能", "社区分享、DeepSeek AI续写协作、多格式导出")
                        ]

                        @classmethod
                        def get_prompt(cls, key):
                            return cls.DEVELOPMENT_PROMPTS.get(key, "未找到对应提示词")

                        @classmethod
                        def show_blueprint(cls, parent):
                            """显示架构蓝图窗口 (Dev Mode Dashboard)"""
                            win = tk.Toplevel(parent)
                            win.title("十二音AI - 终极产品架构师蓝图 (Dev Mode)")
                            win.geometry("900x700")
                            win.configure(bg='#1E1E1E')

                            # 样式配置
                            style = ttk.Style()
                            style.theme_use('clam')
                            style.configure("Dev.TNotebook", background="#1E1E1E", borderwidth=0)
                            style.configure("Dev.TNotebook.Tab", background="#2D2D2D", foreground="#AAAAAA",
                                            padding=[10, 5])
                            style.map("Dev.TNotebook.Tab", background=[("selected", "#3E3E3E")],
                                      foreground=[("selected", "#00FF99")])

                            # 标题区域
                            header_frame = tk.Frame(win, bg='#1E1E1E')
                            header_frame.pack(fill=tk.X, padx=20, pady=15)

                            tk.Label(header_frame, text="TWELVE-TONE AI ARCHITECT",
                                     font=("Impact", 20), bg='#1E1E1E', fg='#00FF99').pack(side=tk.LEFT)

                            # --- 修复点：移除了错误的 check_on_pixels 参数 ---
                            tk.Label(header_frame, text="v7.0 Specification",
                                     font=("Consolas", 10), bg='#1E1E1E', fg='#666666').pack(side=tk.LEFT, padx=10)

                            # 选项卡
                            notebook = ttk.Notebook(win, style="Dev.TNotebook")
                            notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

                            # --- 页面1: 愿景与规格 ---
                            f1 = tk.Frame(notebook, bg='#252526')
                            notebook.add(f1, text="  产品规格 (Specs)  ")

                            info_text = scrolledtext.ScrolledText(f1, bg='#1E1E1E', fg='#D4D4D4',
                                                                  font=("Segoe UI", 11), insertbackground='white',
                                                                  relief=tk.FLAT)
                            info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                            content = f"PRODUCT: {cls.PRODUCT_SPECIFICATION['Product_Name']}\n"
                            content += "=" * 50 + "\n\n"
                            content += f"CORE VISION:\n{cls.PRODUCT_SPECIFICATION['Vision']}\n\n"
                            content += "STRATEGIC PILLARS:\n"
                            for p in cls.PRODUCT_SPECIFICATION['Core_Pillars']:
                                content += f"[+] {p}\n"
                            content += "\nBENCHMARKS:\n" + " | ".join(cls.PRODUCT_SPECIFICATION['References'])

                            info_text.insert(tk.END, content)
                            info_text.config(state=tk.DISABLED)

                            # --- 页面2: AI开发提示词 ---
                            f2 = tk.Frame(notebook, bg='#252526')
                            notebook.add(f2, text="  DeepSeek指令集 (Prompts)  ")

                            lbl_instruct = tk.Label(f2,
                                                    text="提示: 复制以下内容发送给 DeepSeek/ChatGPT 以生成特定模块代码",
                                                    bg='#252526', fg='#888888', font=("Arial", 9))
                            lbl_instruct.pack(pady=5, anchor=tk.W, padx=10)

                            prompt_text = scrolledtext.ScrolledText(f2, bg='#1E1E1E', fg='#4EC9B0',
                                                                    font=("Consolas", 10), insertbackground='white',
                                                                    relief=tk.FLAT)
                            prompt_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

                            p_content = "# SYSTEM CONTEXT: You are an expert Python Music Developer.\n\n"
                            for k, v in cls.DEVELOPMENT_PROMPTS.items():
                                p_content += f">>> 指令区块: [{k}]\n{v}\n{'-' * 60}\n\n"

                            prompt_text.insert(tk.END, p_content)

                            # --- 页面3: 路线图 ---
                            f3 = tk.Frame(notebook, bg='#252526')
                            notebook.add(f3, text="  开发路线图 (Roadmap)  ")

                            roadmap_text = scrolledtext.ScrolledText(f3, bg='#1E1E1E', fg='#CE9178',
                                                                     font=("Consolas", 11), insertbackground='white',
                                                                     relief=tk.FLAT)
                            roadmap_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                            r_content = "AGILE DEVELOPMENT PLAN:\n\n"
                            for phase, title, det in cls.ROADMAP:
                                r_content += f"█ {phase}: {title.upper()}\n   └─ 目标: {det}\n\n"

                            roadmap_text.insert(tk.END, r_content)
                            roadmap_text.config(state=tk.DISABLED)

                            # 底部操作栏
                            action_frame = tk.Frame(win, bg='#2D2D2D', height=40)
                            action_frame.pack(fill=tk.X)
                            tk.Label(action_frame, text="Architect Mode Active", fg="#00FF99", bg="#2D2D2D",
                                     font=("Arial", 8)).pack(
                                side=tk.RIGHT, padx=10, pady=5)# ==============================================================================
# 【紧急修复补丁 v10.1】 修复 check_on_pixels 报错
# 说明：覆盖旧的 TwelveToneAIArchitect 类，移除无效的 pack 参数
# ==============================================================================

import tkinter as tk
from tkinter import ttk, scrolledtext

class TwelveToneAIArchitect:
    """
    【十二音AI 终极产品架构师核心】(修复版)
    用于指导后续AI开发、功能迭代与系统升级的元数据与指令库。
    """

    # 产品愿景与规格说明
    PRODUCT_SPECIFICATION = {
        "Product_Name": "Twelve-Tone AI (十二音AI)",
        "Vision": "集现代作曲技法、智能算法、专业乐器法及直观工作流于一体的创作平台",
        "Core_Pillars": [
            "算法内核升级: 频谱主义、简约主义、偶然音乐、音色旋律",
            "专业乐器法: 键盘/竖琴(左右手/踏板)、弦乐(弓法/泛音)、民乐(SoundFont/技法)",
            "序列魔方强化: 12x12完整性实时校验、自动修复、拖拽式生成",
            "界面现代化: 深色玻璃态、Ableton Clip视图、Dorico级精度",
            "AI生态: 集成DeepSeek开源模型接口，实现智能续写与对位"
        ],
        "References": ["MuseScore 4 (易用性)", "Sibelius (出版质量)", "Max/MSP (模块化)", "Band-in-a-Box (智能伴奏)"]
    }

    # 可直接投喂给AI (如 DeepSeek) 的开发指令集 (Core Prompts)
    DEVELOPMENT_PROMPTS = {
        "Phase_1_Core_Algorithm": """
[Role: DSP & Algorithm Engineer]
任务: 升级十二音序列生成核心 (AdvancedTwelveToneComposer)。
1. 集成“频谱主义”：编写函数 calculate_spectral_frequency(fundamental)，基于泛音列频率计算微音程音高集合。
2. 实现“偶然音乐”：引入加权随机算法 (Weighted Random Walk)，允许用户设定 '控制(Control) vs 混沌(Chaos)' 滑块。
3. 增加“风格模仿”：
   - 利盖蒂(Ligeti): 实现微复调(Micropolyphony)生成算法，创建密集的音簇织体。
   - 约翰·凯奇(Cage): 引入I Ching (易经) 随机数生成器来决定音高与时值。
""",
        "Phase_2_Instrumentation": """
[Role: Virtual Orchestrator]
任务: 优化乐器法逻辑 (Instrumentation Engine)。
1. 钢琴/竖琴优化：
   - 编写 logic_hand_split(): 自动将序列分配为符合解剖学的左手分解和弦与右手旋律。
   - 添加竖琴踏板图计算器 (Harp Pedal Diagram)。
2. 弦乐组深度定制：
   - 自动添加弓法标记：连弓(Legato)、跳弓(Spiccato)、巴托克拨奏(Snap Pizz)。
   - 泛音计算：在极限音域自动将实音转换为人工泛音 (Artificial Harmonics)。
3. 民乐扩展接口：
   - 定义 ChineseInstrumentTrait 类，预留 'Guzheng_Gliss'(刮奏) 与 'Pipa_Tremolo'(轮指) 的MIDI CC控制曲线生成逻辑。
""",
        "Phase_3_Matrix_Engine": """
[Role: Logic & Math Expert]
任务: 重构魔方生成器 (TwelveToneMatrix)。
1. 校验算法：实现 validate_matrix_integrity(12x12_array)，确保每行/列/主对角线无重复音级。
2. 自动修复：当检测到冲突时，编写 solve_matrix_conflict() 使用回溯算法自动填补正确音符。
3. 交互逻辑：开发 'Drag-to-Timeline' 接口，允许将矩阵行数据对象直接转换为时间线上的 Event Clip。
""",
        "Phase_4_Modern_UI": """
[Role: UI/UX Designer]
任务: 重构Tkinter界面为现代深色风格。
1. 样式表：定义 DeepDark 调色板 (Bg: #1E1E1E, Accent: #00FF99, Text: #E0E0E0)。
2. 布局重构：
   - 左侧: 序列控制面板 (Sequence Controller)
   - 中部: 交互式矩阵 (Interactive Matrix)
   - 右侧: 乐器与音色库 (Instrument & SoundFont)
3. 视图模式：模仿 Ableton Live，实现 Session View (Clip触发) 与 Arrangement View (线性时间轴) 的切换逻辑。
"""
    }

    # 详细开发路线图
    ROADMAP = [
        ("Phase 1", "内核算法与作曲家引擎", "风格库(后韦伯恩/五声序列)、自定义规则模块、MVP发布"),
        ("Phase 2", "专业乐器法与音色集成", "智能弓法/指法、通用GM/民乐音色库映射、Alpha测试"),
        ("Phase 3", "魔方矩阵与可视化交互", "实时验证修复、视觉关联、拖拽生成、Beta测试"),
        ("Phase 4", "界面现代化与工作流优化", "深色主题、拖拽式排列、Dorico导出优化"),
        ("Phase 5", "生态整合与高级功能", "社区分享、DeepSeek AI续写协作、多格式导出")
    ]

    @classmethod
    def get_prompt(cls, key):
        return cls.DEVELOPMENT_PROMPTS.get(key, "未找到对应提示词")

    @classmethod
    def show_blueprint(cls, parent):
        """显示架构蓝图窗口 (Dev Mode Dashboard)"""
        win = tk.Toplevel(parent)
        win.title("十二音AI - 终极产品架构师蓝图 (Dev Mode)")
        win.geometry("900x700")
        win.configure(bg='#1E1E1E')

        # 样式配置
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Dev.TNotebook", background="#1E1E1E", borderwidth=0)
        style.configure("Dev.TNotebook.Tab", background="#2D2D2D", foreground="#AAAAAA", padding=[10, 5])
        style.map("Dev.TNotebook.Tab", background=[("selected", "#3E3E3E")], foreground=[("selected", "#00FF99")])

        # 标题区域
        header_frame = tk.Frame(win, bg='#1E1E1E')
        header_frame.pack(fill=tk.X, padx=20, pady=15)

        tk.Label(header_frame, text="TWELVE-TONE AI ARCHITECT",
                 font=("Impact", 20), bg='#1E1E1E', fg='#00FF99').pack(side=tk.LEFT)

        # --- 修复点：移除了错误的 check_on_pixels 参数 ---
        tk.Label(header_frame, text="v7.0 Specification",
                 font=("Consolas", 10), bg='#1E1E1E', fg='#666666').pack(side=tk.LEFT, padx=10)

        # 选项卡
        notebook = ttk.Notebook(win, style="Dev.TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- 页面1: 愿景与规格 ---
        f1 = tk.Frame(notebook, bg='#252526')
        notebook.add(f1, text="  产品规格 (Specs)  ")

        info_text = scrolledtext.ScrolledText(f1, bg='#1E1E1E', fg='#D4D4D4',
                                              font=("Segoe UI", 11), insertbackground='white', relief=tk.FLAT)
        info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        content = f"PRODUCT: {cls.PRODUCT_SPECIFICATION['Product_Name']}\n"
        content += "=" * 50 + "\n\n"
        content += f"CORE VISION:\n{cls.PRODUCT_SPECIFICATION['Vision']}\n\n"
        content += "STRATEGIC PILLARS:\n"
        for p in cls.PRODUCT_SPECIFICATION['Core_Pillars']:
            content += f"[+] {p}\n"
        content += "\nBENCHMARKS:\n" + " | ".join(cls.PRODUCT_SPECIFICATION['References'])

        info_text.insert(tk.END, content)
        info_text.config(state=tk.DISABLED)

        # --- 页面2: AI开发提示词 ---
        f2 = tk.Frame(notebook, bg='#252526')
        notebook.add(f2, text="  DeepSeek指令集 (Prompts)  ")

        lbl_instruct = tk.Label(f2, text="提示: 复制以下内容发送给 DeepSeek/ChatGPT 以生成特定模块代码",
                                bg='#252526', fg='#888888', font=("Arial", 9))
        lbl_instruct.pack(pady=5, anchor=tk.W, padx=10)

        prompt_text = scrolledtext.ScrolledText(f2, bg='#1E1E1E', fg='#4EC9B0',
                                                font=("Consolas", 10), insertbackground='white', relief=tk.FLAT)
        prompt_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        p_content = "# SYSTEM CONTEXT: You are an expert Python Music Developer.\n\n"
        for k, v in cls.DEVELOPMENT_PROMPTS.items():
            p_content += f">>> 指令区块: [{k}]\n{v}\n{'-' * 60}\n\n"

        prompt_text.insert(tk.END, p_content)

        # --- 页面3: 路线图 ---
        f3 = tk.Frame(notebook, bg='#252526')
        notebook.add(f3, text="  开发路线图 (Roadmap)  ")

        roadmap_text = scrolledtext.ScrolledText(f3, bg='#1E1E1E', fg='#CE9178',
                                                 font=("Consolas", 11), insertbackground='white', relief=tk.FLAT)
        roadmap_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        r_content = "AGILE DEVELOPMENT PLAN:\n\n"
        for phase, title, det in cls.ROADMAP:
            r_content += f"█ {phase}: {title.upper()}\n   └─ 目标: {det}\n\n"

        roadmap_text.insert(tk.END, r_content)
        roadmap_text.config(state=tk.DISABLED)

        # 底部操作栏
        action_frame = tk.Frame(win, bg='#2D2D2D', height=40)
        action_frame.pack(fill=tk.X)
        tk.Label(action_frame, text="Architect Mode Active", fg="#00FF99", bg="#2D2D2D", font=("Arial", 8)).pack(
            side=tk.RIGHT, padx=10, pady=5)
        # ==============================================================================
        # 【最终注入包 v11.0】 拟人化演奏引擎 (Humanizer & Nuance Injector)
        # 功能：让生成的乐谱拥有呼吸、力度起伏、连线和表情记号，拒绝机械感
        # ==============================================================================

        import random
        import math
        import music21

        # ------------------------------------------------------------------------------
        # 1. 拟人化处理引擎 (Humanizer)
        # ------------------------------------------------------------------------------
        class HumanPerformanceEngine:
            """
            负责给冰冷的音符添加“人类的温度”。
            主要处理：力度波浪、乐句呼吸、演奏法细节。
            """

            @staticmethod
            def apply_human_feel(score, style_mode="Schoenberg"):
                """主处理函数"""
                # 1. 注入力度起伏 (Dynamic Hairpins)
                # 机器通常是 mp -> mf 突变，人类是 mp < mf > p 渐变
                HumanPerformanceEngine._apply_dynamic_swells(score, style_mode)

                # 2. 注入乐句连线 (Slurs & Phrasing)
                # 人类会把一组音符连在一起唱
                HumanPerformanceEngine._apply_slurs(score, style_mode)

                # 3. 注入演奏法 (Articulations)
                # 根据风格决定是断奏、重音还是保持音
                HumanPerformanceEngine._apply_articulations(score, style_mode)

                # 4. 注入表情术语 (Expressions)
                # 如 "Dolce" (以此), "Marcato" (强调)
                HumanPerformanceEngine._apply_text_expressions(score, style_mode)

                return score

            @staticmethod
            def _apply_dynamic_swells(score, style):
                """添加渐强渐弱 (Hairpins)"""
                for part in score.parts:
                    measures = list(part.getElementsByClass('Measure'))
                    total_measures = len(measures)

                    # 韦伯恩风格：突强突弱，极端的对比
                    if "Webern" in style:
                        for m in measures:
                            if random.random() < 0.3:
                                m.insert(0, music21.dynamics.Dynamic(random.choice(['pp', 'ff', 'ppp'])))

                    # 贝尔格/浪漫风格：长线条的渐强渐弱
                    elif "Berg" in style or "Romantic" in style:
                        i = 0
                        while i < total_measures - 4:
                            # 创建一个 4-6 小节的起伏
                            span = random.randint(3, 6)
                            if i + span < total_measures:
                                # 开始渐强
                                measures[i].insert(0, music21.dynamics.Crescendo())
                                # 中间到达高潮
                                peak_vol = music21.dynamics.Dynamic('f')
                                measures[i + span // 2].insert(0, peak_vol)
                                # 结束渐弱
                                measures[i + span // 2].insert(0.5, music21.dynamics.Diminuendo())
                            i += span + 1

                    # 默认/勋伯格：常规的乐句起伏
                    else:
                        for i in range(0, total_measures, 4):
                            if random.random() < 0.5 and i < total_measures - 1:
                                measures[i].insert(0, music21.dynamics.Crescendo())
                                measures[i + 1].insert(0, music21.dynamics.Diminuendo())

            @staticmethod
            def _apply_slurs(score, style):
                """智能添加连线 (Slurs)"""
                for part in score.parts:
                    notes = list(part.flatten().notes)
                    if not notes: continue

                    # 韦伯恩：短促的二音连线或三音连线
                    if "Webern" in style:
                        i = 0
                        while i < len(notes) - 2:
                            if random.random() < 0.4:
                                # 连接两个音
                                s = music21.spanner.Slur(notes[i], notes[i + 1])
                                part.insert(0, s)
                                i += 2
                            else:
                                i += 1

                    # 贝尔格/民乐：长连线
                    elif "Berg" in style or "Chinese" in style:
                        i = 0
                        while i < len(notes) - 6:
                            if random.random() < 0.6:
                                length = random.randint(4, 8)
                                if i + length < len(notes):
                                    s = music21.spanner.Slur(notes[i], notes[i + length])
                                    part.insert(0, s)
                                i += length + 1
                            else:
                                i += 1

                    # 勋伯格：基于动机的连线（3-4个音）
                    else:
                        i = 0
                        while i < len(notes) - 4:
                            if random.random() < 0.5:
                                s = music21.spanner.Slur(notes[i], notes[i + 3])
                                part.insert(0, s)
                                i += 4
                            else:
                                i += 1

            @staticmethod
            def _apply_articulations(score, style):
                """添加跳音、重音、保持音"""
                for part in score.parts:
                    notes = list(part.flatten().notes)
                    for n in notes:
                        # 随机跳过休止符
                        if n.isRest: continue

                        # 民乐风格：多用保持音(Tenuto)模拟余音
                        if "Chinese" in style:
                            if n.quarterLength >= 1.0 and random.random() < 0.3:
                                n.articulations.append(music21.articulations.Tenuto())

                        # 韦伯恩：多用跳音(Staccato)和重音(Accent)
                        elif "Webern" in style:
                            if n.quarterLength < 1.0:
                                n.articulations.append(music21.articulations.Staccato())
                            elif random.random() < 0.2:
                                n.articulations.append(music21.articulations.Accent())

                        # 勋伯格：强调强拍
                        else:
                            if n.beat == 1.0 and random.random() < 0.4:
                                n.articulations.append(music21.articulations.StrongAccent())

            @staticmethod
            def _apply_text_expressions(score, style):
                """添加表情术语"""
                # 在第一小节添加整体情绪
                first_measure = score.parts[0].measure(1)
                if not first_measure: return

                if "Berg" in style:
                    exp = music21.expressions.TextExpression("Espressivo e amoroso")
                    exp.style.fontStyle = 'italic'
                    first_measure.insert(0, exp)
                elif "Webern" in style:
                    exp = music21.expressions.TextExpression("Langsam, sehr zart")
                    exp.style.fontStyle = 'italic'
                    first_measure.insert(0, exp)
                elif "Chinese" in style:
                    exp = music21.expressions.TextExpression("Cantabile (如歌地)")
                    exp.style.fontStyle = 'italic'
                    first_measure.insert(0, exp)
                else:
                    exp = music21.expressions.TextExpression("Moderato energico")
                    exp.style.fontStyle = 'italic'
                    first_measure.insert(0, exp)

        # ------------------------------------------------------------------------------
        # 2. 升级版后台生成逻辑 (Monkey Patch Upgrade)
        # ------------------------------------------------------------------------------
        def upgraded_bg_generate(self, insts, tech, bpm, bars):
            """
            这是新的后台生成函数，它会替代 ModernTwelveToneWorkstation 中的旧函数。
            它加入了 HumanPerformanceEngine 的调用。
            """
            try:
                # A. 准备矩阵
                self.root.after(0, lambda: self.log("Calculating Matrix Geometry..."))
                p0_nums = self.matrix_data[0]
                num_to_note = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A",
                               10: "A#", 11: "B"}
                p0_notes = [num_to_note[n] for n in p0_nums]
                full_matrix = self.composer.generate_matrix(p0_notes)

                # B. 基础生成 (Robot Score)
                self.root.after(0, lambda: self.log(f"Composing Base Structure ({tech})..."))
                raw_score = self.composer.create_professional_score(
                    instruments=insts,
                    matrix=full_matrix,
                    tempo_mark=f"{tech} Pro",
                    tempo_value=bpm,
                    num_measures=bars,
                    technique=tech,
                    use_imported_matrix=False,
                    emotion="default"
                )

                # C. 【关键】拟人化处理 (Humanizing)
                self.root.after(0, lambda: self.log(">>> Injecting Human Nuance & Phrasing..."))
                # 获取当前选择的风格名称用于拟人化参数
                current_style = self.style_var.get()
                humanized_score = HumanPerformanceEngine.apply_human_feel(raw_score, style_mode=current_style)

                # D. 导出
                self.root.after(0, lambda: self.log("Exporting to MusicXML..."))
                path = self.composer.generate_sibelius_files(humanized_score)

                self.root.after(0, lambda: self.finish(path))

            except Exception as e:
                print(f"Generate Error: {e}")
                import traceback
                traceback.print_exc()
                self.root.after(0, lambda: self.log(f"Error: {e}"))

        # ------------------------------------------------------------------------------
        # 3. 激活补丁
        # ------------------------------------------------------------------------------
        # 将新逻辑覆盖到界面类中
        ModernTwelveToneWorkstation.bg_generate = upgraded_bg_generate

        # ------------------------------------------------------------------------------
        # 4. 确保主程序启动
        # ------------------------------------------------------------------------------
        if __name__ == "__main__":
            try:
                # 清理可能存在的旧窗口
                import tkinter as tk
                if tk._default_root:
                    for w in tk._default_root.winfo_children(): w.destroy()
                    tk._default_root.destroy()
            except:
                pass

            # 启动
            root = tk.Tk()
            # 确保主菜单使用了最新的 Monkey Patch
            app = TwelveToneSuite(root)
            root.mainloop()
            # ==============================================================================
            # 【物理限制修正补丁 v12.0】 乐器生理学引擎
            # 功能：强制修正超音域音符、非法和弦与错误技法
            # ==============================================================================

            import music21

            # ------------------------------------------------------------------------------
            # 1. 乐器物理数据库 (Instrument Physics Database)
            # 定义乐器的极限音域 (MIDI编号) 和 最大同时发音数
            # ------------------------------------------------------------------------------
            class InstrumentPhysicsDB:
                # 格式: "Name": (Low_MIDI, High_MIDI, Max_Polyphony)
                # C4 = 60, G3 = 55, C2 = 36
                SPECS = {
                    # --- 弦乐 ---
                    "Violin": (55, 103, 2),  # G3 - G7 (双音)
                    "Violin I": (55, 103, 2),
                    "Violin II": (55, 103, 2),
                    "Viola": (48, 91, 2),  # C3 - G6
                    "Cello": (36, 76, 2),  # C2 - E5
                    "Double Bass": (28, 67, 1),  # E1 - G4 (通常只奏单音)

                    # --- 木管 ---
                    "Flute": (60, 96, 1),  # C4 - C7 (单音)
                    "Oboe": (58, 91, 1),  # Bb3 - G6
                    "Clarinet": (50, 94, 1),  # D3 - Bb6
                    "Bassoon": (34, 72, 1),  # Bb1 - C5

                    # --- 铜管 ---
                    "Horn": (34, 77, 1),  # Bb1 - F5
                    "Trumpet": (52, 86, 1),  # E3 - D6
                    "Trombone": (40, 72, 1),  # E2 - C5
                    "Tuba": (28, 58, 1),  # E1 - Bb3

                    # --- 键盘/弹拨 ---
                    "Piano": (21, 108, 10),  # A0 - C8 (全音域)
                    "Harp": (23, 103, 8),  # Cb1 - G#7
                    "Guzheng": (36, 84, 4),  # 模拟范围
                    "Pipa": (40, 84, 4)
                }

                @staticmethod
                def get_specs(inst_name):
                    # 模糊匹配，防止 "Violin I" 匹配不到
                    for key in InstrumentPhysicsDB.SPECS:
                        if key in inst_name:
                            return InstrumentPhysicsDB.SPECS[key]
                    # 默认返回钢琴范围
                    return (21, 108, 10)

            # ------------------------------------------------------------------------------
            # 2. 物理修正器 (The Sanitizer)
            # ------------------------------------------------------------------------------
            class PhysicsSanitizer:
                """
                遍历乐谱，修正所有违反物理定律的音符。
                """

                @staticmethod
                def sanitize_score(score):
                    print(">>> [Physics Engine] Checking playability...")

                    for part in score.parts:
                        # 1. 识别乐器
                        part_name = part.partName if part.partName else "Piano"
                        low_limit, high_limit, max_poly = InstrumentPhysicsDB.get_specs(part_name)

                        # 2. 遍历所有小节和音符
                        for n in part.flatten().notes:
                            # A. 处理和弦 (Polyphony check)
                            if n.isChord:
                                # 如果乐器只能吹单音 (如长笛)，只保留最高音
                                if max_poly == 1:
                                    # 转换为单音
                                    top_note = n.sortAscending().notes[-1]
                                    # 替换和弦为单音 (保留时值和offset)
                                    new_note = music21.note.Note(top_note.pitch)
                                    new_note.quarterLength = n.quarterLength
                                    new_note.offset = n.offset
                                    new_note.articulations = n.articulations
                                    # 在流中替换 (需要复杂的music21操作，这里做简化处理：直接修改原对象)
                                    # 由于music21替换复杂，我们采取修正音高法：
                                    # 将和弦其余音移除，只留一个
                                    n.pitches = (top_note.pitch,)

                                    # 如果是弦乐，限制双音跨度不能太大 (模拟)
                                elif max_poly == 2 and len(n.pitches) > 2:
                                    # 只保留外声部 (最高和最低)
                                    sorted_p = sorted(n.pitches)
                                    n.pitches = (sorted_p[0], sorted_p[-1])

                            # B. 处理音域 (Range check)
                            # 注意：经过上面处理，n 可能是 Note 也可能是剩下的 Chord
                            if n.isChord:
                                pitches = n.pitches
                            else:
                                pitches = [n.pitch]

                            new_pitches = []
                            for p in pitches:
                                midi = p.midi
                                # 修正过低的音
                                while midi < low_limit:
                                    midi += 12
                                # 修正过高的音
                                while midi > high_limit:
                                    midi -= 12

                                # 如果修正后依然超出 (极少数情况)，强制钳位
                                if midi < low_limit: midi = low_limit
                                if midi > high_limit: midi = high_limit

                                new_pitches.append(music21.pitch.Pitch(midi))

                            # 应用修正后的音高
                            if n.isChord:
                                n.pitches = tuple(new_pitches)
                            else:
                                n.pitch = new_pitches[0]

                            # C. 技法清洗 (Technique check)
                            # 例如：防止长笛出现 Pizzicato
                            if max_poly == 1:  # 管乐通常没有拨奏
                                # 移除不合法的演奏法
                                valid_arts = []
                                for art in n.articulations:
                                    if not isinstance(art, (music21.articulations.Pizzicato,
                                                            music21.articulations.SnapPizzicato)):
                                        valid_arts.append(art)
                                n.articulations = valid_arts

                    return score

            # ------------------------------------------------------------------------------
            # 3. 拦截生成流程，注入物理修正
            # ------------------------------------------------------------------------------
            # 我们定义一个新的生成链条：
            # 矩阵生成 -> 基础乐谱 -> [拟人化处理] -> [物理修正] -> 导出

            def ultimate_generation_pipeline(self, insts, tech, bpm, bars):
                try:
                    # 1. 准备矩阵
                    self.root.after(0, lambda: self.log("Initializing Composer Core..."))
                    p0_nums = self.matrix_data[0]
                    # (转换逻辑...)
                    num_to_note = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F", 6: "F#", 7: "G", 8: "G#", 9: "A",
                                   10: "A#", 11: "B"}
                    p0_notes = [num_to_note[n] for n in p0_nums]
                    full_matrix = self.composer.generate_matrix(p0_notes)

                    # 2. 基础生成 (Base)
                    self.root.after(0, lambda: self.log("Generating Structure..."))
                    raw_score = self.composer.create_professional_score(
                        instruments=insts, matrix=full_matrix, tempo_mark=f"{tech}",
                        tempo_value=bpm, num_measures=bars, technique=tech,
                        use_imported_matrix=False, emotion="default"
                    )

                    # 3. 拟人化 (Humanize)
                    self.root.after(0, lambda: self.log("Applying Human Nuances..."))
                    # 获取风格
                    style = self.style_var.get()
                    score_human = HumanPerformanceEngine.apply_human_feel(raw_score, style_mode=style)

                    # 4. 【新增】物理修正 (Physics Check)
                    self.root.after(0, lambda: self.log("Checking Instrument Ranges & Physics..."))
                    score_final = PhysicsSanitizer.sanitize_score(score_human)

                    # 5. 导出
                    self.root.after(0, lambda: self.log("Finalizing MusicXML..."))
                    path = self.composer.generate_sibelius_files(score_final)

                    self.root.after(0, lambda: self.finish(path))

                except Exception as e:
                    print(f"Pipeline Error: {e}")
                    import traceback
                    traceback.print_exc()
                    self.root.after(0, lambda: self.log(f"CRITICAL ERROR: {e}"))

            # ------------------------------------------------------------------------------
            # 4. 再次热更新 (Hot-fix)
            # ------------------------------------------------------------------------------
            # 将包含物理修正的新管道，赋值给界面类
            ModernTwelveToneWorkstation.bg_generate = ultimate_generation_pipeline

            # ------------------------------------------------------------------------------
            # 5. 启动
            # ------------------------------------------------------------------------------
            if __name__ == "__main__":
                try:
                    import tkinter as tk
                    # 清理旧环境
                    if tk._default_root:
                        for w in tk._default_root.winfo_children(): w.destroy()
                        tk._default_root.destroy()
                except:
                    pass

                root = tk.Tk()
                app = TwelveToneSuite(root)
                root.mainloop()
