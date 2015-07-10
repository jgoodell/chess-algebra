import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open('chess.cfg'))

ITEM_DELIMITER = config.get('general', 'item_delimiter')
MAPPING_DELIMITER = config.get('general', 'mapping_delimiter')
VECTOR_DELIMITER = config.get('general', 'vector_delimiter')

PIECES = [each.strip() for each in config.get('general', 'pieces').split(',')]

def _parse_mappings(string):
    '''Converts mappings from cfg to python dict.'''
    items = string.split(ITEM_DELIMITER)
    mapping_dict = dict()

    for item in items:
        key, value = item.split(MAPPING_DELIMITER)
        try:
            mapping_dict[key.strip()] = int(value)
        except ValueError:
            mapping_dict[int(key)] = value.strip()
    return mapping_dict

def _parse_vectors(string):
    '''Converst vector from cfg to python tuple.'''
    items = string.split(ITEM_DELIMITER)
    tuple_list = list()

    for item in items:
        try:
            x_value, y_value = item.split(VECTOR_DELIMITER)
        except Exception, e:
            import pdb; pdb.set_trace()
        tuple_list.append(tuple([int(x_value), int(y_value)]))
    return tuple(tuple_list)
        
X_MAPPING = _parse_mappings(config.get('x_mapping', 'forward'))
REVERSE_X_MAPPING = _parse_mappings(config.get('x_mapping', 'reverse'))

KNIGHT_UNIT_VECTORS = _parse_vectors(config.get('knight', 'unit_vectors'))
KNIGHT_RANGE = int(config.get('knight', 'range'))
ROOK_UNIT_VECTORS = _parse_vectors(config.get('rook', 'unit_vectors'))
ROOK_RANGE = int(config.get('rook', 'range'))
QUEEN_UNIT_VECTORS = _parse_vectors(config.get('queen', 'unit_vectors'))
QUEEN_RANGE = int(config.get('queen', 'range'))


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
    '''Calculates the potential moves for the defined pieces
    based on the pieces current position.
    '''
    x_axis, y_axis = convert_chess_position(position)

    if piece in PIECES:
        UNIT_VECTORS = eval("%s_UNIT_VECTORS" % piece.upper())
        RANGE = eval("%s_RANGE" % piece.upper())
        moves = calculate_moves(x_axis, y_axis, UNIT_VECTORS,
                                RANGE)
    else:
        return ''

    moves = convert_and_validate_moves((moves))
    return moves
