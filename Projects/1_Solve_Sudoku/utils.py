import re

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

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

# def eliminate(grid):
#
#      # First eliminating the digits that are already present in the corresponding square
#     for square in square_units:
#         eliminateStr = []
#         for peer in square:
#             if grid[peer] != "123456789":
#                 eliminateStr.append(grid[peer])
#
#         for peer in square:
#             if grid[peer] == "123456789":
#                 grid[peer] = re.sub("|".join(eliminateStr), "", "123456789")
#
#     # Then remove the elements that are peers that are in rows and columns peers
#     print("\n\n")
#
#     return grid
