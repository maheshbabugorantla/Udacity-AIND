
from utils import *


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# Diagonals
diagonal_unit_1 = [[rs+cs for rs, cs in zip(rows, cols)]] # Top-Left to Bottom-Right
diagonal_unit_2 = [[rs+cs for rs, cs in zip(rows, cols[::-1])]] # Bottom-Left to Top-Right

# diagonal_units = [diagonal_unit_1, diagonal_unit_2]

unitlist = row_units + column_units + square_units + diagonal_unit_1 + diagonal_unit_2

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).
    """
    # Obtaining all the boxes where there are only two possibilities
    twin_boxes = [box for box in boxes if len(values[box]) == 2]

    naked_twins = []

    for box in twin_boxes:
        value = values[box]
        for peer in peers[box]:
            if values[peer] == value: # and (peer, box) not in naked_twins: # (peer, box) not in naked_twins removes the duplicate pairs
                naked_twins.append((box, peer))

    for twin1, twin2 in naked_twins:
        peer1 = peers[twin1]
        peer2 = peers[twin2]
        value = values[twin1]
        peers_common = set(peer1) & set(peer2)
        for peer in peers_common:
            if len(values[peer]) > 1:
                for val in value:
                    values = assign_value(values, peer, values[peer].replace(val, ''))

    return values

def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    solved = [key for key in values.keys() if len(values[key]) == 1]

    for s in solved:
        digit = values[s]
        peerSet = peers[s]
        for peer in peerSet:
            values[peer] = values[peer].replace(digit, "")
    return values

def only_choice(grid):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """
    for unit in unitlist:
        for digit in '123456789':
            box_n = [box for box in unit if digit in grid[box]]
            if len(box_n) == 1:
                grid[box_n[0]] = digit

    return grid

def reduce_puzzle(grid):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable
    """
    done = False

    while not done:
        # Counting the no. of determined cases
        puzzle_before = len([box for box in grid.keys() if len(grid[box]) == 1])
        grid = eliminate(grid)
        grid = only_choice(grid)
        grid = naked_twins(grid)

        puzzle_after = len([box for box in grid.keys() if len(grid[box]) == 1])
        done = puzzle_before == puzzle_after

        # Sanity Check, return False if there is a box with zero available values
        if len([box for box in grid.keys() if len(grid[box]) == 0]):
            return False

    return grid

def search(grid):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """
    # First Reduce the grid values
    grid = reduce_puzzle(grid)

    # BASE Cases for Recursion
    # Check if we already have a solution or failed initially
    if grid is False:
        return False # Failed Earlier

    # Checking to see if already have a solution
    if all([len(grid[box]) == 1 for box in boxes]):
        return grid

    # Check for the box that least no.of possibilities
    box, n = min([(box, len(grid[box])) for box in boxes if len(grid[box]) > 1])

    # Choosing one possibility at a time
    for val in grid[box]:
        new_grid = grid.copy()
        new_grid[box] = val
        trial = search(new_grid)

        if trial: # This is only true if there is a solution else the 'trial' == false and we will chose the next possibility
            return trial

def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values

if __name__ == "__main__":
    diag_sudoku_grid = '........4......1.....6......7....2.8...372.4.......3.7......4......5.6....4....2.'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
