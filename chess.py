X_MAPPING = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
REVERSE_X_MAPPING = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

KNIGHT_UNIT_VECTORS = (
    (2,1,),(1,2,),(-1,2,),(-2,1,),(-2,-1,),(-1,-2,),(1,-2,),(2,-1,),)
KNIGHT_RANGE = 1
QUEEN_UNIT_VECTORS = (
    (1,0,),(1,1,),(0,1),(-1,1,),(-1,0,),(-1,-1,),(0,-1,),(-1,1,),)
QUEEN_RANGE = 8
ROOK_UNIT_VECTORS = ((1,0,),(1,1,),(-1,0,),(-1,-1,),)
ROOK_RANGE = 8


def find_knight_moves(x_axis, y_axis):
    #import pdb; pdb.set_trace()
    move_multiplier = 1
    moves = []
    for unit_vector in KNIGHT_UNIT_VECTORS:
        for each in range(KNIGHT_RANGE):
            x_value = unit_vector[0]*move_multiplier
            y_value = unit_vector[1]*move_multiplier
            x_value += x_axis
            y_value += y_axis
            moves.append([x_value, y_value])
    return moves 


def find_rook_moves(x_axis, y_axis):
    return ''


def find_queen_moves(x_axis, y_axis):
    return ''


def convert_chess_position(position):
    '''
    Takes a chess position as a chess algebra string and
    returns separate x and y values as integers.
    '''
    
    x_axis = X_MAPPING[position[0]]
    y_axis = int(position[1])
    return x_axis, y_axis


def revert_chess_position(x_axis, y_axis):
    '''
    Takes a chess position as separate x and y integers
    and returns a string in chess algebra notation.
    '''
    return ''.join([REVERSE_X_MAPPING.get(x_axis,'x'), str(y_axis)])


def convert_and_validate_moves(moves):
    '''
    Takes a collection of chess moves as collections of
    separate x and y intgers and returns a comma
    separated string of moves. Also validates that the
    move is within the bounds of the board.
    '''
    tmp = list()
    for move in moves:
        x_value = move[0]
        y_value = move[1]

        #make sure move is on the board
        if x_value != 'x' and y_value > 0 and y_value < 9:
            tmp.append(revert_chess_position(x_value, y_value))
            
    #import pdb; pdb.set_trace()
    return ', '.join(tmp)

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

    moves = convert_and_validate_moves((moves))
    return moves
