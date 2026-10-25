"""Instrument registers, voicings and notation markings."""

import random
from ..dependencies import music21


class Instrumentation:
    def __init__(self, settings):
        self.settings = settings

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

    def get_note_in_range(self, note_name, instrument_name, octave):
        """确保音符在乐器音域内"""
        if instrument_name not in self.settings.instrument_ranges:
            return note_name + str(octave)

        low_midi, high_midi = self.settings.instrument_ranges[instrument_name]

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
                    note_name = self.settings.num_to_note[note_num]
                    full_note = self.get_note_in_range(note_name, "Piano", octaves[i])
                    chords.append(full_note)
            else:
                # 如果音符不足，使用单音
                note_name = self.settings.num_to_note[note_nums[0]]
                full_note = self.get_note_in_range(note_name, "Piano", octave_base)
                chords.append(full_note)

        elif texture_type == "cluster":
            # 音簇式织体：密集的音符组合
            if len(note_nums) >= 4:
                cluster_notes = note_nums[:4]
                octave_offset = 1 if hand_type == "treble" else -1
                for note_num in cluster_notes:
                    note_name = self.settings.num_to_note[note_num]
                    full_note = self.get_note_in_range(note_name, "Piano", octave_base + octave_offset)
                    chords.append(full_note)
            else:
                note_name = self.settings.num_to_note[note_nums[0]]
                full_note = self.get_note_in_range(note_name, "Piano", octave_base)
                chords.append(full_note)

        else:
            # 其他织体类型：单音
            note_name = self.settings.num_to_note[note_nums[0]]
            full_note = self.get_note_in_range(note_name, "Piano", octave_base)
            chords.append(full_note)

        return chords

    def get_articulation_object(self, name):
        """Create a supported articulation; ornaments belong to expressions."""
        classes = {
            'staccato': 'Staccato', 'tenuto': 'Tenuto', 'accent': 'Accent',
            'staccatissimo': 'Staccatissimo', 'marcato': 'StrongAccent',
            'portato': 'Tenuto', 'spiccato': 'Spiccato', 'sforzando': 'Stress',
            'harmonics': 'Harmonic', 'pizzicato': 'Pizzicato',
        }
        class_name = classes.get(name)
        return getattr(music21.articulations, class_name)() if class_name else None

    def apply_articulation(self, note, name):
        articulation = self.get_articulation_object(name)
        if articulation is not None:
            note.articulations.append(articulation)
            return
        expressions = {'fermata': 'Fermata', 'trill': 'Trill', 'turn': 'Turn',
                       'mordent': 'Mordent', 'tremolo': 'Tremolo'}
        class_name = expressions.get(name)
        if class_name:
            note.expressions.append(getattr(music21.expressions, class_name)())
        elif name:
            # Techniques requiring multi-note spanners are retained as text.
            note.expressions.append(music21.expressions.TextExpression(name))

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
