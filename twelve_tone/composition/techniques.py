"""Tone-row selection and development strategies."""

import random


class TechniqueEngine:
    def __init__(self, settings):
        self.settings = settings

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
        pentatonic_row = [self.settings.num_to_note[note] for note in all_notes]
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
