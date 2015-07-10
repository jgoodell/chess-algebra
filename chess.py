X_MAPPING = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
REVERSE_X_MAPPING = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

KNIGHT_UNIT_VECTORS = (
    (2,1,),(1,2,),(-1,2,),(-2,1,),(-2,-1,),(-1,-2,),(1,-2,),(2,-1,),)
KNIGHT_VECTOR_MULTIPLIER = 1
QUEEN_UNIT_VECTORS = (
    (1,0,),(1,1,),(0,1),(-1,1,),(-1,0,),(-1,-1,),(0,-1,),(-1,1,),)
QUEEN_VECTOR_MULTIPLIER = 8
ROOK_UNIT_VECTORS = ((1,0,),(1,1,),(-1,0,),(-1,-1,),)
ROOK_VECTOR_MULTIPLIER = 8


def find_knight_moves(x_axis, y_axis):
    return ''


def find_rook_moves(x_axis, y_axis):
    return ''


def find_queen_moves(x_axis, y_axis):
    return ''


def convert_chess_position(position):
    x_axis = X_MAPPING[position[0]]
    y_axis = position[1]
    return x_axis, y_axis


def revert_chess_position(x_axis, y_axis):
    position = ''
    return position


def convert_moves(moves):
    tmp = list()
    for move in moves:
        tmp.append(revert_chess_position(move[0], move[1]))
    return ','.join(tmp)

def get_potential_moves(piece, position):
    x_axis, y_axis = convert_chess_position(position)
    
    if piece.lower() == 'knight':
        moves = find_knight_moves(x_axis, y_axis)
    elif piece.lower() == 'rook':
        moves = find_rook_moves(x_axis, y_axis)
    elif piece.lower() == 'queen':
        moves = find_queen_moves(x_axis, y_axis)
    else:
        return ''

    moves = convert_moves((moves))
    return moves
