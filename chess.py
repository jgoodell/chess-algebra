X_MAPPING = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
REVERSE_X_MAPPING = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

KNIGHT_UNIT_VECTORS = (
    (2,1,),(1,2,),(-1,2,),(-2,1,),(-2,-1,),(-1,-2,),(1,-2,),(2,-1,),)
KNIGHT_RANGE = 1
QUEEN_UNIT_VECTORS = (
    (1,0,),(1,1,),(0,1),(-1,1,),(-1,0,),(-1,-1,),(0,-1,),(1,-1,),)
QUEEN_RANGE = 8
ROOK_UNIT_VECTORS = ((1,0,),(0,1,),(-1,0,),(0,-1,),)
ROOK_RANGE = 8


def calculate_moves(x_axis, y_axis, unit_vectors, piece_range):
    '''Uses vector algebra to calculate the move options based
    on the current position if the piece, the posible movement
    unit vectors, and the pieces range for a single. move.
    Returns a separate x and y values for the move.
    '''
    moves = []

    for unit_vector in unit_vectors:
        move_multiplier = 1

        for each in range(piece_range):
            x_vector = unit_vector[0]*move_multiplier
            y_vector = unit_vector[1]*move_multiplier
            x_value = x_vector + x_axis
            y_value = y_vector + y_axis
            moves.append([x_value, y_value])
            move_multiplier += 1
    return moves 


def convert_chess_position(position):
    '''Takes a chess position as a chess algebra string and
    returns separate x and y values as integers.
    '''
    
    x_axis = X_MAPPING[position[0]]
    y_axis = int(position[1])
    return x_axis, y_axis


def revert_chess_position(x_axis, y_axis):
    '''Takes a chess position as separate x and y integers
    and returns a string in chess algebra notation.
    '''
    return ''.join([REVERSE_X_MAPPING.get(x_axis,'x'), str(y_axis)])


def convert_and_validate_moves(moves):
    '''Takes a collection of chess moves as collections of
    separate x and y intgers and returns a comma
    separated string of moves. Also validates that the
    move is within the bounds of the board.
    '''
    tmp = list()
    for move in moves:
        x_value = move[0]
        y_value = move[1]

        position = revert_chess_position(x_value, y_value)
        #make sure move is on the board
        if position[0] != 'x' and int(position[1:]) > 0 and int(position[1:]) < 9:
            tmp.append(position)
    return ', '.join(tmp)

def get_potential_moves(piece, position):
    '''Calculates the potential moves for the "knight", "rook" and "queen"
    based on the pieces current position.
    '''
    x_axis, y_axis = convert_chess_position(position)
    
    if piece.lower() == 'knight':
        moves = calculate_moves(x_axis, y_axis, KNIGHT_UNIT_VECTORS,
                                KNIGHT_RANGE)
    elif piece.lower() == 'rook':
        moves = calculate_moves(x_axis, y_axis, ROOK_UNIT_VECTORS,
                                ROOK_RANGE)
    elif piece.lower() == 'queen':
        moves = calculate_moves(x_axis, y_axis, QUEEN_UNIT_VECTORS,
                                QUEEN_RANGE)
    else:
        return ''

    moves = convert_and_validate_moves((moves))
    return moves
