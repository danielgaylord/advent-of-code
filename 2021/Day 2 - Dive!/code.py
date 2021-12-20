import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    moves = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        moves = [line.rstrip().split(" ") for line in input]
    return moves

def core(file, part):
    moves = parse_input(file)
    
    horiz = 0
    depth = 0
    new_depth = 0
    aim = 0

    for move in moves:
        if move[0] == "forward":
            horiz += int(move[1])
            new_depth += aim * int(move[1])
        elif move[0] == "down":
            depth += int(move[1])
            aim += int(move[1])
        elif move[0] == "up":
            depth -= int(move[1])
            aim -= int(move[1])

    if part == 1:
        return horiz * depth
    if part == 2:
        return horiz * new_depth

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 150)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 900)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2)) 