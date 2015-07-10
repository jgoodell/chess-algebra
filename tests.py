from unittest import TestCase

from chess import get_potential_moves

class ChessTestCase(TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_knight(self):
        response = get_potential_moves('knight', 'd2')
        self.assertEqual(response,
                         'b1, f1, b3, f3, c4, e4')
