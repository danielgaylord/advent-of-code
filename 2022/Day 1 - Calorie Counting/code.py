import unittest, os, heapq

# Read puzzle input and return as usable data structure
def parse_input(file):
    elves = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        calories = 0
        for line in input:
            if line.strip():
                calories += int(line.rstrip())
            else:
                elves.append(calories)
                calories = 0
        elves.append(calories)
    return elves

def core(file, nlargest):
    elves = parse_input(file)

    # Part 1: Return largest amount of calories
    largest = 0
    for elf in elves:
        if elf > largest:
            largest = elf
    # return largest

    # Part 2: Return sum of top 3
    heapq.heapify(elves)
    return sum(heapq.nlargest(nlargest, elves))

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 24000)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 3), 45000)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt', 1))
    # print(core('input.txt', 1))
    
    # Part 2 solution
    # print(core('example.txt', 3))
    print(core('input.txt', 3))
        