import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    rucksacks = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        rucksacks = [line.rstrip() for line in input]
    return rucksacks

def core(file):
    rucksacks = parse_input(file)
    
    # Part 1: Find common item in first and second half of each line
    prioritySum = 0
    for rucksack in rucksacks:
        compartmentSize = len(rucksack) // 2
        item = list(set(rucksack[0:compartmentSize]) & set(rucksack[compartmentSize:]))[0]
        priority = ord(item.lower()) - 96
        if item.isupper():
            priority += 26
        prioritySum += priority 

    # Part 2: Find common item in each set of 3 lines
    prioritySum = 0
    for i in range(len(rucksacks) // 3):
        badge = list(set(rucksacks[3 * i]) & set(rucksacks[3 * i + 1]) & set(rucksacks[3 * i + 2]))[0]
        priority = ord(badge.lower()) - 96
        if badge.isupper():
            priority += 26
        prioritySum += priority

    return prioritySum

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt'), 157)
    
    def test_part2(self):
        self.assertEqual(core('example.txt'), 70)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        