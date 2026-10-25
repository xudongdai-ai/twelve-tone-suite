"""MusicXML serialization and export destination handling."""

import datetime
from pathlib import Path

from ..dependencies import music21, require_music21


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


class MusicXMLExporter:
    def __init__(self, output_dir=None):
        self.output_dir = Path(output_dir).expanduser() if output_dir is not None else None
        self.optimizer = XMLOptimizer()

    def export(self, score):
        require_music21()
        directory = self.output_dir if self.output_dir is not None else Path.home() / 'Desktop'
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError:
            if self.output_dir is not None:
                raise
            directory = Path.cwd()
        timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S-%f')
        filename = directory / f'professional_score_{timestamp}.xml'
        return str(self.optimizer.optimize_and_save(score, str(filename)))
