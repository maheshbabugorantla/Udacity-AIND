from copy import deepcopy

xdim, ydim = 3, 2 # Board Dimensions

class GameState:

    def __init__(self):

        # Set up the axes for the board
        self._board = [[0] * ydim for val in range(xdim)]

        # Open and Closed Sets of cells (0 -> open and 1 -> closed)
        # Block off the lower Right Corner of the Board
        self._board[-1][-1] = 1 # Blocking the Lower Right Cell of the Board

        # Current Player (Player One is represented as 0 and Player 2 is represented as 1)
        # Used to indicate current player self._current ^= 1 (flips the players turn between 0 and 1)
        # Default: Player 1 takes the First Turn
        self._player = 0

        # X and O current position on the board
        self._current = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if type(move) is not tuple:
            raise TypeError("Parameter 'move' should be of type tuple")

        legal_moves = set(self.get_legal_moves())

        if move not in legal_moves: # If the player has made a move that is invalid
            raise RunTimeError("Move {} is not a legal move".format(move))


        newBoard = deepcopy(self)
        current_position = newBoard._current[self._player] # Getting the Current Player's Current Position

        newBoard._board[move[0]][move[1]] = 1
        newBoard._current[self._player] = move # Updating the Current Position
        newBoard._player ^= 1 # Flips the Players turn

        return newBoard

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """

        # Returning all the available empty spaces for the player if it is their first turn
        if self._current[0] is None or self._current[1] is None:
            return self._get_all_blank_spaces()

        # Returning available Legal Moves
        legal_moves = list()

        '''
            (0, 1) => Move forward along the same column
            (0, -1) => Move backward along the same column
            (1, 0) => Move right along the same row
            (-1, 0) => Move left along the same row
            (1, 1) => Move Diagonally towards the bottom-right corner
            (1, -1) => Move Diagonally towards the top-right corner
            (-1, 1) => Move Diagonally towards the bottom-left corner
            (-1, -1) => Move Diagonally towards the top-left corner
        '''
        unit_paths = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for _path_x, _path_y in unit_paths:

            _x, _y = self._current[self._player] # Getting the Current Players Current Position

            while 0 <= _x + _path_x < xdim and 0 <= _y + _path_y < ydim:
                _x += _path_x
                _y += _path_y

                if self._board[_x][_y]: # Checking to see if the cell is already closed
                    break

                legal_moves.append((_x, _y)) #

        return legal_moves

    def _get_all_blank_spaces(self):
        return [(col, row) for row in range(ydim) for col in range(xdim) if self._board[col][row] == 0]
