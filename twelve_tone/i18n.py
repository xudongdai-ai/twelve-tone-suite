"""Chinese and English messages for score generation."""


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
