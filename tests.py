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
                
    def test_rook(self):
        response = get_potential_moves('rook', 'd5')
        response = [each.strip() for each in response.split(',')]

        for each in ['a5', 'b5', 'c5', 'e5', 'f5', 'g5', 'h5',
                     'd1', 'd2', 'd3', 'd4', 'd6', 'd7', 'd8']:
            self.assertTrue(each in response)

    def test_queen(self):
        response = get_potential_moves('queen', 'd4')
        response = [each.strip() for each in response.split(',')]
        
        for each in ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4',
                     'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8',
                     'a7', 'b6', 'c5', 'e3', 'f2', 'g1',
                     'a1', 'b2', 'c3', 'e5', 'f6', 'g7', 'h8']:
            self.assertTrue(each in response)
