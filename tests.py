from unittest import TestCase

from chess import get_potential_moves

class ChessTestCase(TestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_knight(self):
        response = get_potential_moves('knight', 'd2')
        response = [each.strip() for each in response.split(',')]

        for each in ['b1', 'f1', 'b3', 'f3', 'c4', 'e4']:
            self.assertTrue(each in response)
                
