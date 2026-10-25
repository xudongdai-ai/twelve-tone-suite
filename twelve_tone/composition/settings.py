"""Composition presets and instrument ranges; no GUI or score dependencies."""


class CompositionSettings:
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
