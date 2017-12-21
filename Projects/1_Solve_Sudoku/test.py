from utils import *

def main():
    grid = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print(grid)
    eliminate(grid)
    display(grid)

if __name__ == '__main__':
    main()
