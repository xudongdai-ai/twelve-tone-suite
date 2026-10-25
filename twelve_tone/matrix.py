"""Pure pitch-class operations shared by the desktop and composition engine.

Variant suffixes are semitone transpositions of the input row (P0 is unchanged).
I0 is inversion about pitch class 0, matching the original composition API.
The display matrix is anchored to the first input pitch, preserving its top row.
"""

NOTE_NAMES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
NOTE_TO_NUM = {name: index for index, name in enumerate(NOTE_NAMES)}
NOTE_ALIASES = {'DB': 'C#', 'EB': 'D#', 'GB': 'F#', 'AB': 'G#', 'BB': 'A#'}


def validate_tone_row(numbers):
    row = list(numbers)
    if len(row) != 12:
        raise ValueError('请输入正好12个数字或音名。')
    if any(type(value) is not int or not 0 <= value <= 11 for value in row):
        raise ValueError('每个音级必须是0到11之间的整数。')
    if len(set(row)) != 12:
        raise ValueError('音级不能重复，必须包含12个不同的音级。')
    return row


def parse_tone_row(value):
    """Accept a space/comma-separated string or a sequence of notes/integers."""
    tokens = value.replace(',', ' ').split() if isinstance(value, str) else list(value)
    numbers = []
    for token in tokens:
        if type(token) is int:
            numbers.append(token)
            continue
        if not isinstance(token, str):
            raise ValueError(f'无法识别音级：{token}')
        name = token.strip().upper().replace('♯', '#').replace('♭', 'B')
        if name.lstrip('-').isdigit():
            numbers.append(int(name))
        else:
            name = NOTE_ALIASES.get(name, name)
            if name not in NOTE_TO_NUM:
                raise ValueError(f'无法识别音名：{token}')
            numbers.append(NOTE_TO_NUM[name])
    return validate_tone_row(numbers)


def build_matrix(numbers):
    """Return a 12×12 matrix whose rows and columns each contain all pitches."""
    row = validate_tone_row(numbers)
    return [[(pitch + row[0] - anchor) % 12 for pitch in row] for anchor in row]


def build_variants(numbers):
    row = validate_tone_row(numbers)
    bases = {'P': row, 'I': [(-pitch) % 12 for pitch in row],
             'R': row[::-1], 'RI': [(-pitch) % 12 for pitch in row[::-1]]}
    return {
        kind: {shift: [(pitch + shift) % 12 for pitch in base] for shift in range(12)}
        for kind, base in bases.items()
    }


def flatten_variants(variants):
    """Validate and flatten GUI data to the composer's P0 … RI11 keys."""
    result = {}
    for kind in ('P', 'I', 'R', 'RI'):
        for shift in range(12):
            try:
                row = variants[kind][shift]
            except (KeyError, TypeError) as error:
                raise ValueError(f'导入矩阵缺少序列：{kind}{shift}') from error
            result[f'{kind}{shift}'] = validate_tone_row(row)
    return result
