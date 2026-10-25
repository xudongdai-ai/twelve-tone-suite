"""Coordinate matrix generation, score construction and MusicXML export."""

from ..dependencies import require_music21
from ..i18n import MultilingualSystem
from ..matrix import parse_tone_row, build_variants, flatten_variants
from ..export.musicxml import MusicXMLExporter
from .settings import CompositionSettings
from .techniques import TechniqueEngine
from .rhythm import RhythmGenerator
from .instrumentation import Instrumentation
from .builder import ScoreBuilder


class AdvancedTwelveToneComposer:
    def __init__(self, output_dir=None):
        self.settings = CompositionSettings()
        self.lang_system = MultilingualSystem()
        self.techniques = TechniqueEngine(self.settings)
        self.rhythm = RhythmGenerator(self.settings)
        self.instrumentation = Instrumentation(self.settings)
        self.builder = ScoreBuilder(self.settings, self.techniques, self.rhythm, self.instrumentation)
        self.exporter = MusicXMLExporter(output_dir)

    def generate_chinese_pentatonic_row(self):
        return self.techniques.generate_chinese_pentatonic_row()

    def generate_matrix(self, row):
        return flatten_variants(build_variants(parse_tone_row(row)))

    def create_professional_score(self, instruments, matrix, tempo_mark, tempo_value,
                                  num_measures=45, technique='schoenberg',
                                  use_imported_matrix=False, emotion='default'):
        require_music21()
        if not instruments:
            raise ValueError('请至少选择一种乐器。')
        if num_measures <= 0 or tempo_value <= 0:
            raise ValueError('小节数和 BPM 必须大于 0。')
        if technique not in self.settings.composition_techniques:
            raise ValueError(f'未知作曲技法：{technique}')
        self.builder.lang_system = self.lang_system
        return self.builder.create_professional_score(
            instruments, matrix, tempo_mark, tempo_value, num_measures,
            technique, use_imported_matrix, emotion
        )

    def generate_sibelius_files(self, score):
        print(self.lang_system.get_text('processing_xml'))
        filename = self.exporter.export(score)
        print(f"✓ {self.lang_system.get_text('complete')} -> {filename}")
        return filename

    def run(self, imported_sequence=None, matrix_data=None):
        """Optional interactive console workflow; never invoked by package import."""
        require_music21()
        inputs = self.get_user_input(imported_sequence, matrix_data)
        return self.run_with_inputs(inputs)

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

        for i, (tech_id, tech_info) in enumerate(self.settings.composition_techniques.items()):
            print(f"{i + 1:2d}. {tech_info['name']:20} - {tech_info['description']}")

        try:
            tech_choice = int(input(f"\nSelect (1-{len(self.settings.composition_techniques)}): ") or "1")
            selected_technique = list(self.settings.composition_techniques.keys())[tech_choice - 1]
        except (ValueError, IndexError):
            selected_technique = "schoenberg"
            print("Using default: Schoenberg")

        print(f"{self.lang_system.get_text('using_tech')} {self.settings.composition_techniques[selected_technique]['name']}")

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

        for i, (tempo_name, bpm) in enumerate(self.settings.tempo_options.items()):
            print(f"{i + 1:2d}. {tempo_name:12} (approx {bpm} BPM)")

        print(f"{len(self.settings.tempo_options) + 1:2d}. Custom Tempo")

        tempo_choice = input(f"\nSelect (1-{len(self.settings.tempo_options) + 1}, default 5): ").strip()

        if tempo_choice == str(len(self.settings.tempo_options) + 1):
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
                if 0 <= choice_idx < len(self.settings.tempo_options):
                    tempo_mark = list(self.settings.tempo_options.keys())[choice_idx]
                    tempo_value = list(self.settings.tempo_options.values())[choice_idx]
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

    def run_with_inputs(self, inputs):
        """使用图形界面已收集的参数生成作品，不再调用 input()。"""
        require_music21()

        (P0, instruments, tempo_mark, tempo_value, num_measures,
         technique, use_imported, matrix_data, emotion) = inputs

        print("\n" + "=" * 50)
        print(self.lang_system.get_text('generating'))
        print("=" * 50)

        print(self.lang_system.get_text('matrix_gen'))
        if use_imported and matrix_data:
            matrix = flatten_variants(matrix_data)
            print("   使用导入的完整魔方矩阵")
        else:
            matrix = self.generate_matrix(P0)
            print("   生成新的音列矩阵")

        if technique not in self.settings.composition_techniques:
            raise ValueError(f'未知作曲技法：{technique}')

        print(self.lang_system.get_text('apply_tech'))
        print(f"   使用技法: {self.settings.composition_techniques[technique]['name']}")
        print(f"   技法特点: {self.settings.composition_techniques[technique]['description']}")
        print(f"   发展手法: {', '.join(self.settings.composition_techniques[technique]['techniques'])}")

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
