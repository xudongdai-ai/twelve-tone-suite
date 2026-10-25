"""Optional music21 dependency; absence must not prevent matrix use."""

try:
    import music21
except ImportError:
    music21 = None


def require_music21():
    if music21 is None:
        raise RuntimeError('未安装 music21，无法生成乐谱。请运行：python -m pip install music21')
    return music21
