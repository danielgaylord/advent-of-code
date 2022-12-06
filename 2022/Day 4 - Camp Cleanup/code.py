import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    rucksacks = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        rucksacks = [line.rstrip() for line in input]
    return rucksacks

def core(file):
    rucksacks = parse_input(file)

    return prioritySum

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt'), 2)
    
    def test_part2(self):
        self.assertEqual(core('example.txt'), 0)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
        