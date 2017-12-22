from utils import *
import time

def main():

    start_time = time.time()

    # Grid 1 : EASY Level
    grid = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    grid = search(grid)
    print("")
    print("")
    display(grid)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))
    start_time = time.time()


    # Grid 2 : HARD Level
    grid2 = grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
    grid2 = search(grid2)
    print("")
    print("")
    display(grid2)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))

    start_time = time.time()

    # Grid 3 : EASY Level
    grid3 = grid_values('1.4.9..68956.18.34..84.695151.....868..6...1264..8..97781923645495.6.823.6.854179')
    grid3 = search(grid3)
    print("")
    print("")
    display(grid3)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))

    start_time = time.time()

    # Grid 4 : HARDEST Level
    grid4 = grid_values('85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.')
    grid4 = search(grid4)
    print("")
    print("")
    display(grid4)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))

    start_time = time.time()

    # Grid 5 : HARDEST Level
    grid4 = grid_values('..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..')
    grid4 = search(grid4)
    print("")
    print("")
    display(grid4)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))

    start_time = time.time()

    # Grid 6 : Long Time (Around 7 seconds)
    grid4 = grid_values('.....6....59.....82....8....45........3........6..3.54...325..6..................')
    grid4 = search(grid4)
    print("")
    print("")
    display(grid4)
    print("Puzzle is solved in ----%s seconds ----"%(time.time() - start_time))
if __name__ == '__main__':
    main()
