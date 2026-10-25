import random
import unittest

from twelve_tone.matrix import (
    build_matrix, build_variants, flatten_variants, parse_tone_row, validate_tone_row,
)


class MatrixTests(unittest.TestCase):
    def test_note_aliases_and_numbers(self):
        expected = list(range(12))
        for value in ('C Db D Eb E F Gb G Ab A Bb B',
                      'C C♯ D D♯ E F F♯ G G♯ A A♯ B',
                      '0,1,2,3,4,5,6,7,8,9,10,11', expected):
            with self.subTest(value=value):
                self.assertEqual(parse_tone_row(value), expected)

    def test_rejects_invalid_rows(self):
        for row in ('', '0 1 2', 'C C D D# E F F# G G# A A# B',
                    'C Db D Eb E F Gb G Ab A Bb H', list(range(1, 13)),
                    [-1] + list(range(1, 12)), [True] + list(range(1, 12))):
            with self.subTest(row=row), self.assertRaises(ValueError):
                parse_tone_row(row)

    def test_rows_columns_and_anchor_for_random_rows(self):
        rng = random.Random(7401)
        for _ in range(100):
            row = rng.sample(range(12), 12)
            original = row.copy()
            matrix = build_matrix(row)
            self.assertEqual(matrix[0], row)
            self.assertEqual(row, original)
            self.assertEqual(len(matrix), 12)
            for line in matrix + list(zip(*matrix)):
                self.assertEqual(set(line), set(range(12)))
            self.assertEqual([matrix[i][i] for i in range(12)], [row[0]] * 12)

    def test_all_variants_and_transpositions(self):
        row = [7, 0, 4, 1, 9, 2, 10, 3, 11, 5, 8, 6]
        variants = build_variants(row)
        flat = flatten_variants(variants)
        self.assertEqual(len(flat), 48)
        self.assertEqual(variants['P'][0], row)
        self.assertEqual(variants['R'][0], row[::-1])
        self.assertEqual(variants['I'][0], [(-n) % 12 for n in row])
        self.assertEqual(variants['RI'][0], variants['I'][0][::-1])
        for key, sequence in flat.items():
            self.assertEqual(set(sequence), set(range(12)), key)
        self.assertEqual(variants['P'][5], [(n + 5) % 12 for n in row])

    def test_rejects_incomplete_imported_variants(self):
        variants = build_variants(range(12))
        del variants['RI'][11]
        with self.assertRaisesRegex(ValueError, 'RI11'):
            flatten_variants(variants)

    def test_rejects_invalid_imported_sequence(self):
        variants = build_variants(range(12))
        variants['P'][2] = [0] * 12
        with self.assertRaises(ValueError):
            flatten_variants(variants)

    def test_generated_lists_are_independent(self):
        row = list(range(12))
        variants = build_variants(row)
        flat = flatten_variants(variants)
        flat['P0'][0] = 99
        self.assertEqual(variants['P'][0], row)
        self.assertEqual(validate_tone_row(row), row)
