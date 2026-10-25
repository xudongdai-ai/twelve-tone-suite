"""Rhythm, texture and dynamics plans."""

import random


class RhythmGenerator:
    def __init__(self, settings):
        self.settings = settings

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
            dynamic_index = self.settings.dynamics_options.index(base_dynamic) if base_dynamic in self.settings.dynamics_options else 4
            new_index = max(0, min(len(self.settings.dynamics_options) - 1, dynamic_index + variation))

            dynamics_plan.append(self.settings.dynamics_options[new_index])

        return dynamics_plan

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
