"""Expressive articulations and phrase slurs for generated scores."""

import random

from .dependencies import music21


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
                    breath = music21.articulations.BreathMark()
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
