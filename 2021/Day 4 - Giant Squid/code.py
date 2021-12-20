import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    draws = []
    boards = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        draws = input.readline().rstrip().split(",")
        while input.readline() == "\n":
            board = []
            for _ in range(5):
                board.append(input.readline().rstrip().split())
            boards.append(board)
    return draws, boards

# Mark a given boards spot for a drawn number
def mark(board, num):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == num:
                board[row][col] = -1

# Check if a board has won in a row or column
def check(board):
    tboard = list(map(list, zip(*board)))
    for row in board:
        if all(e == -1 for e in row):
            return True
    for row in tboard:
        if all(e == -1 for e in row):
            return True
    return False

# Finds the score of a given board
def score(board):
    total = 0
    for row in board:
        for num in row:
            if num != -1:
                total += int(num)
    return total

def core(file, part):
    draws, boards = parse_input(file)
    
    # Go through each drawn number, mark all boards, then check to see if any won
    win_board = None
    last_num = -1
    for num in draws:
        for board in boards:
            mark(board, num)
        for board in boards:
            if check(board):
                win_board = board
                boards.remove(board)
        last_num = int(num)
        # End part 1 when there is a winning board, end part 2 when no boards left
        if (win_board and part == 1) or len(boards) == 0:
            break
    
    if part == 1:
        return score(win_board) * last_num
    if part == 2:
        return score(board) * last_num

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 4512)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 1924)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))