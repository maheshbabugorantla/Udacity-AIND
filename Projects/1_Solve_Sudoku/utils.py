from collections import Counter

rows = 'ABCDEFGHI'
cols = '123456789'

'''
    The below functions are copied from Udacity helper code
'''
# cross('abc', 'def') will return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
def cross(a, b):
    return [s + t for s in a for t in b]

boxes = cross(rows, cols)

# Element example:
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# This is the top most row
row_units = [cross(r, cols) for r in rows]

# Element example:
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# This is the left most column.
column_units = [cross(rows, c) for c in cols]

# Element example:
# square_units[0] = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
# This is the top left square.
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


'''
    The below function code is written by @MaheshBabuGorantla
'''
# This is used to convert the string form of sudoku representation
# into a dictionary form where each box is represented as a key such A1 (means Row A , Column 1)
# My Solution
def grid_values(grid_str):
    return {box:( '123456789' if val == '.' else val) for box, val in zip(boxes, grid_str)}

def eliminate(grid):
    solved = [key for key in grid.keys() if len(grid[key]) == 1]

    for val in solved:
        digit = grid[val]
        for peer in peers[val]:
            grid[peer] = grid[peer].replace(digit, "")

    return grid

def only_choice(grid):
    for unit in unitlist:
        for digit in '123456789':
            box_n = [box for box in unit if digit in grid[box]]
            if len(box_n) == 1:
                grid[box_n[0]] = digit

    return grid

# def only_choice_1(grid):
#
#     solved = [key for key in grid.keys() if len(grid[key]) == 1]
#     solved_cells = set(solved)
#
#     for square in square_units:
#         search_units = set(square) - solved_cells
#         counter = Counter()
#         for unit in search_units:
#             counter.update(list(grid[unit]))
#
#         only_choice = [key for key in counter.keys() if counter[key] == 1]
#
#         for choice in only_choice:
#             for unit in search_units:
#                 if choice in grid[unit]:
#                     grid[unit] = choice
#
#     display(grid)
#     #
#     # return grid

def reduce_puzzle(grid):

    done = False

    while not done:
        # Counting the no. of determined cases
        puzzle_before = len([box for box in grid.keys() if len(grid[box]) == 1])
        grid = eliminate(grid)
        grid = only_choice(grid)
        puzzle_after = len([box for box in grid.keys() if len(grid[box]) == 1])
        done = puzzle_before == puzzle_after

        # Sanity Check, return False if there is a box with zero available values
        if len([box for box in grid.keys() if len(grid[box]) == 0]):
            return False

    return grid

def search(grid):

    # First Reduce the grid values
    grid = reduce_puzzle(grid)

    # BASE Case for Recursion
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
