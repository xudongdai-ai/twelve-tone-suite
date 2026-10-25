"""Build music21 scores using the composition services."""

import random
from ..dependencies import music21
import datetime

from ..notation import EmotionExpressionSystem, PhrasingIntelligence
from ..i18n import MultilingualSystem


class ScoreBuilder:
    def __init__(self, settings, techniques, rhythm, instrumentation, language='zh-CN'):
        self.settings = settings
        self.techniques = techniques
        self.rhythm = rhythm
        self.instrumentation = instrumentation
        self.lang_system = MultilingualSystem(language)
        self.emotion_system = EmotionExpressionSystem()
        self.phrasing_system = PhrasingIntelligence()

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
            current_sequence = self.techniques.apply_composition_technique(
                technique, matrix, measure_num - 1, 0)

            # 确定钢琴织体类型
            texture_type = self.rhythm.generate_piano_texture_type(measure_num - 1, technique)

            # 生成钢琴特定节奏模式
            if part_type == "treble":
                rhythm_pattern = self.rhythm.generate_piano_treble_rhythm(technique, measure_num - 1, texture_type)
            else:  # bass
                rhythm_pattern = self.rhythm.generate_piano_bass_rhythm(technique, measure_num - 1, texture_type)

            note_index = 0
            rhythm_index = 0

            # 添加表情记号
            if measure_num % 4 == 1 and random.random() < 0.7:
                expression = random.choice([e for e in self.settings.expression_options if e])
                self.instrumentation.add_expression_marking(measure, expression)

            # 添加力度变化
            if measure_num % 2 == 1 or random.random() < 0.5:
                dynamic = dynamics_plan[measure_num - 1]
                self.instrumentation.add_dynamic_marking(measure, dynamic)

            # 填充小节
            while current_duration < 4.0 and rhythm_index < len(rhythm_pattern):
                if note_index >= len(current_sequence):
                    note_index = 0

                rhythm = rhythm_pattern[rhythm_index]
                rhythm_duration = self.rhythm.get_quarter_length(rhythm)

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
                    octave = self.instrumentation.generate_registral_contrast(
                        current_sequence[note_index], instrument_name, measure_num, technique)

                    # 根据声部类型调整音区
                    if part_type == "treble":
                        octave = max(4, octave + 1)  # 高音部使用较高音区
                    else:  # bass
                        octave = min(4, octave - 1)  # 低音部使用较低音区

                    # 为钢琴创建音符或和弦
                    if texture_type in ["chordal", "cluster"] and rhythm_duration >= 0.5:
                        # 对于较长的时值，使用和弦
                        chord_notes = self.instrumentation.create_piano_chord(
                            current_sequence[note_index:min(note_index + 4, len(current_sequence))],
                            texture_type, octave, part_type
                        )

                        if len(chord_notes) > 1:
                            # 创建和弦
                            chord = music21.chord.Chord(chord_notes)
                            chord.quarterLength = rhythm_duration

                            # 添加演奏法
                            if random.random() < 0.6:
                                articulation = random.choice(self.settings.articulations_options)
                                if articulation:
                                    self.instrumentation.apply_articulation(chord, articulation)

                            measure.append(chord)
                            note_index += len(chord_notes)
                        else:
                            # 单音
                            note_obj = music21.note.Note(chord_notes[0])
                            note_obj.quarterLength = rhythm_duration

                            # 添加演奏法
                            if random.random() < 0.8:
                                articulation = random.choice(self.settings.articulations_options)
                                if articulation:
                                    self.instrumentation.apply_articulation(note_obj, articulation)

                            measure.append(note_obj)
                            note_index += 1
                    else:
                        # 单音
                        note_name = self.settings.num_to_note[current_sequence[note_index]]
                        full_note_name = self.instrumentation.get_note_in_range(note_name, instrument_name, octave)
                        note_obj = music21.note.Note(full_note_name)

                        # 添加演奏法
                        if random.random() < 0.8:
                            articulation = random.choice(self.settings.articulations_options)
                            if articulation:
                                self.instrumentation.apply_articulation(note_obj, articulation)

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
        score.metadata.title = f"十二音序列作品 - {self.settings.composition_techniques[technique]['name']}"
        score.metadata.composer = "Algorithmic Composition System - Professional Edition"
        score.metadata.date = datetime.datetime.now().strftime("%Y/%m/%d")

        # 生成结构化的音乐元素
        dynamics_plan = self.rhythm.generate_dynamics_with_structure(num_measures, technique)

        # 创建曲式结构
        structure = self.create_complex_score_structure(num_measures, technique)

        # 创建乐器部分
        parts = []
        for i_idx, instrument_name in enumerate(instruments):
            # 对于需要大谱表的乐器，创建两个部分（高音和低音）
            if instrument_name in self.settings.grand_staff_instruments:
                # 高音部分
                treble_part = music21.stream.Part()
                try:
                    instr = music21.instrument.fromString(instrument_name)
                    treble_part.append(instr)
                    treble_part.partName = f"{instrument_name} (Treble)"
                    treble_part.partAbbreviation = self.instrumentation.get_instrument_abbreviation(instrument_name)
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
                    bass_part.partAbbreviation = self.instrumentation.get_instrument_abbreviation(instrument_name)
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
                    part.partAbbreviation = self.instrumentation.get_instrument_abbreviation(instrument_name)

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
                    current_sequence = self.techniques.apply_composition_technique(
                        technique, matrix, measure_num - 1, i_idx)

                    # 生成复杂的节奏模式
                    rhythm_pattern = self.rhythm.generate_rhythm_pattern(technique, measure_num - 1, i_idx)

                    note_index = 0
                    rhythm_index = 0

                    # 添加表情记号
                    if measure_num % 3 == 1 and random.random() < 0.6:
                        expression = random.choice([e for e in self.settings.expression_options if e])
                        self.instrumentation.add_expression_marking(measure, expression)

                    # 添加力度变化
                    if measure_num % 2 == 1 or random.random() < 0.4:
                        dynamic = dynamics_plan[measure_num - 1]
                        self.instrumentation.add_dynamic_marking(measure, dynamic)

                    # 填充小节
                    while current_duration < 4.0 and rhythm_index < len(rhythm_pattern):
                        if note_index >= len(current_sequence):
                            note_index = 0

                        rhythm = rhythm_pattern[rhythm_index]
                        rhythm_duration = self.rhythm.get_quarter_length(rhythm)

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
                            note_name = self.settings.num_to_note[note_num]

                            # 生成音区对比
                            octave = self.instrumentation.generate_registral_contrast(note_num, instrument_name, measure_num, technique)

                            full_note_name = self.instrumentation.get_note_in_range(note_name, instrument_name, octave)
                            note_obj = music21.note.Note(full_note_name)

                            # 添加演奏法
                            if random.random() < 0.8:
                                articulation = random.choice(self.settings.articulations_options)
                                if articulation:
                                    self.instrumentation.apply_articulation(note_obj, articulation)

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


        return score
