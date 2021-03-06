"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

def improved_score_heuristic(game, player):
    """
        Outputs a score that is a difference between player's moves and opponent moves

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        player : hashable
            One of the objects registered by the game object as a valid player.
            (i.e., `player` should be either game.__player_1__ or
            game.__player_2__).

        Returns
        ----------
        float
            The heuristic value of the current game state
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(my_moves - opponent_moves)

def improved_score_heuristic(game, player, alpha):
    """
        Outputs a score that is a difference between player's moves and opponent moves

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        player : hashable
            One of the objects registered by the game object as a valid player.
            (i.e., `player` should be either game.__player_1__ or
            game.__player_2__).

        Returns
        ----------
        float
            The heuristic value of the current game state
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(my_moves - alpha * opponent_moves)

def improved_score_2_heuristic(game, player):
    """
        Outputs a score that is a difference between player's moves and opponent moves

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        player : hashable
            One of the objects registered by the game object as a valid player.
            (i.e., `player` should be either game.__player_1__ or
            game.__player_2__).

        Returns
        ----------
        float
            The heuristic value of the current game state
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(my_moves - 1.5 * opponent_moves)

def improved_score_3_heuristic(game, player):
    """
        Outputs a score that is a weighted difference of player's moves and opponent moves (weighted more)

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        player : hashable
            One of the objects registered by the game object as a valid player.
            (i.e., `player` should be either game.__player_1__ or
            game.__player_2__).

        Returns
        ----------
        float
            The heuristic value of the current game state
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(my_moves - 2 * opponent_moves)

def distance_from_center(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    width, height = game.width/2., game.height/2.
    y, x = game.get_player_location(player)

    return float((height - y)**2 + (width - x)**2)

def moves_ratio(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))

    if my_moves == 0: # Opponent Wins
        return -8

    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    if opponent_moves == 0: # Current Player Wins
        return 8

    ratio = float(my_moves/opponent_moves)

    if ratio == 1:
        return 0
    elif ratio <= 0.5:
        return -6
    elif ratio <= 0.75:
        return -4
    elif ratio < 1:
        return -2
    elif ratio <= 1.25:
        return 2
    elif ratio <= 1.75:
        return 4
    elif ratio <= 2:
        return 6
    else:
        return 8

def weighted_center_board_moves(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    center_dis_c = distance_from_center(game, player)
    center_dis_o = distance_from_center(game, game.get_opponent(player))

    # TODO: Need to think of a logic to give more weightage for the moves at the center

    # Variable to store the Weighted Current Player's and Opponent's score based on their distance from the center of Isolation Board
    w_player_score = 0
    w_opponent_score = 0

    if center_dis_c == 0: # The current player is at the center of the board
        w_player_score = 8
    elif center_dis_c <= 1:
        w_player_score = 5
    elif center_dis_c <= 2:
        w_player_score = 2
    elif center_dis_c <= 3:
        w_player_score = 1

    if center_dis_o == 0: # The opponent player is at the center of the board
        w_opponent_score = 8 # 4
    elif center_dis_o <= 1:
        w_opponent_score = 5 # 3
    elif center_dis_o <= 2:
        w_opponent_score = 2
    elif center_dis_o <= 3:
        w_opponent_score = 1

    return float(w_player_score - w_opponent_score)

def weighted_available_moves(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = game.get_legal_moves(player)
    opponent_moves = game.get_legal_moves(game.get_opponent(player))

    width, height = game.width/2., game.height/2.

    my_score = 0
    opponent_score = 0

    for move in my_moves:
        center_distance = float(((width - move[1])**2 + (height - move[0])**2)**0.5)

        # Giving more weightage for the available moves near to the center
        my_score += my_score * (game.width - center_distance)

    for move in opponent_moves:
        center_distance = float(((width - move[1])**2 + (height - move[0])**2)**0.5)

        # Giving more weightage for the available moves near to the center
        opponent_score += opponent_score * (game.width - center_distance)

    return my_score - opponent_score

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    return float(moves_ratio(game=game, player=player))
    # return improved_score_heuristic(game=game, player=player, alpha=1.5)

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!
    # return weighted_available_moves(game=game, player=player)
    # return improved_score_heuristic(game=game, player=player, alpha=2.0)
    return improved_score_3_heuristic(game=game, player=player)

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    return float(weighted_center_board_moves(game=game, player=player))
    # return improved_score_heuristic(game=game, player=player, alpha=2.5)

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        legal_moves = game.get_legal_moves()

        if not legal_moves: # If there are no more legal moves then return (-1, -1)
            return (-1, -1)

        bestMove = None

        # If we started the game then take the center position
        if game.move_count == 0:
            return (game.height//2, game.width//2)
        else:
            bestMove = legal_moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return bestMove

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        return self._helper_minimax(game=game, depth=depth) # Returning the best legal move

    # Copied from AIMA Pseudocode
    def terminal_test(self, game, depth): # Either the depth is Zero(node is terminal node) OR there are no legal moves
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        return depth == 0 or len(legal_moves) == 0

    def min_value(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(game, depth):
            return self.score(game, self)

        bestScore = float("inf")

        for move in game.get_legal_moves():
            bestScore = min(bestScore, self.max_value(game.forecast_move(move), depth - 1)) # Get the bestScore

        return bestScore

    def max_value(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(game, depth):
            return self.score(game, self)

        bestScore = float("-inf")

        for move in game.get_legal_moves():
            bestScore = max(bestScore, self.min_value(game.forecast_move(move), depth - 1)) # Get the bestScore

        return bestScore

    def _helper_minimax(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        bestMove = None # Assuming first legal move as the best move

        legal_moves = game.get_legal_moves()

        if not legal_moves: # If there are no more legal moves then return (-1, -1)
            return (-1, -1)

        # If we started the game then take the center position
        if game.move_count == 0:
            return (game.height//2, game.width//2)
        else:
            bestMove = legal_moves[0]

        # bestMove = legal_moves[0] # Assuming first legal move as the best move
        bestScore = float("-inf")

        for move in legal_moves:
            nextMove = game.forecast_move(move)
            bestMove, bestScore = max([(bestMove, bestScore), (move, self.min_value(nextMove, depth - 1))] , key=lambda item: item[1]) # Get the move that has the bestScore

        return bestMove

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        bestMove = None # Assuming first legal move as the best move

        legal_moves = game.get_legal_moves()

        if not legal_moves: # If there are no more legal moves then return (-1, -1)
            return (-1, -1)

        # If we started the game then take the center position
        if game.move_count == 0:
            return (game.height//2, game.width//2)
        else:
            bestMove = legal_moves[0]

        try:

            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            _depth = 1
            while True:
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()

                best_move = self.alphabeta(game=game, depth=_depth)
                _depth += 1

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def terminal_test(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        return depth == 0 or not legal_moves

    def min_value(self, game, depth, alpha, beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(game=game, depth=depth):
            return self.score(game, self)

        bestScore = float("inf")

        legal_moves = game.get_legal_moves()

        for move in legal_moves:
            bestScore = min(bestScore, self.max_value(game=game.forecast_move(move), depth=depth-1, alpha=alpha, beta=beta))

            if bestScore <= alpha:
                return bestScore

            beta = min(beta, bestScore)

        return bestScore

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(game=game, depth=depth):
            return self.score(game, self)

        bestScore = float("-inf")

        legal_moves = game.get_legal_moves()

        for move in legal_moves:
            bestScore = max(bestScore, self.min_value(game=game.forecast_move(move), depth=depth-1, alpha=alpha, beta=beta))

            if bestScore >= beta:
                return bestScore

            alpha = max(alpha, bestScore)

        return bestScore

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!

        bestScore = float("-inf")

        legal_moves = game.get_legal_moves()

        if not legal_moves: # If there are no more legal moves then return (-1, -1)
            return (-1, -1)

        # If we started the game then take the center position
        if game.move_count == 0:
            return (game.height//2, game.width//2)
        else:
            bestMove = legal_moves[0]

        for move in legal_moves:
            _score = self.min_value(game=game.forecast_move(move), depth=depth-1, alpha=alpha, beta=beta)
            alpha = max(_score, alpha) # Updating the alpha
            bestMove, bestScore = max([(bestMove, bestScore), (move, _score)], key=lambda item: item[1])

        return bestMove
