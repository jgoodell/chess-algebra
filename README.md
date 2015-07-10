# chess-algebra
Coding Challenge

# instructions
In any language, and given standard algebraic notation of a chess board (see below),
write code that will:
 
1. Accept 2 parameters:
   1. Type of chess piece (Queen, Rook, Knight)
   2. Current position on a chess board (for example: d2)
2.Return
   1. A list of all the potential board positions that piece could advance to,
      with one move, from the given position, with the assumption there are no
      other pieces on the board.
 
The only piece types that will be used (passed to) the code will be Queen, Rook and Knight.
 
Example:
 
If the code is passed:  “knight, d2”
The response should be:  “b1, f1, b3, f3,c4, e4"

#USAGE:

To use this code either run

   $ nosetests

from the repository root, or start a python shell in the root
of the repository.

     >>> from chess import get_potential_moves
     >>> get_potential_moves('rook', 'a3')
     'b3, c3, d3, e3, f3, g3, h3, a4, a5, a6, a7, a8, a2, a1'
     >>> 