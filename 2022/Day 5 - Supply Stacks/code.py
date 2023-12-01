import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    stacks = []
    ops = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        pairs = [line.rstrip().split(",") for line in input]
    return pairs

def core(file):
    pairs = parse_input(file)

    return overlaps

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt'), 2)
    
    def test_part2(self):
        self.assertEqual(core('example.txt'), 4)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        