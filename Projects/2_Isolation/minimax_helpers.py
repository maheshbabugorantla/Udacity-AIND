
def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    if gameState.get_legal_moves(): # If there are legal moves left then return False
        return False

    return True

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1

    legal_moves = gameState.get_legal_moves()
    minValue = float("inf") # Positive infinity

    for move in legal_moves:
        minValue = min(minValue, max_value(gameState.forecast_move(move)))

    return minValue

def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1

    maxValue = float("-inf") # Negative infinity
    legal_moves = gameState.get_legal_moves()

    for move in legal_moves:
        maxValue = max(maxValue, min_value(gameState.forecast_move(move)))

    return maxValue
