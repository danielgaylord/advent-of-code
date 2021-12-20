import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    sweeps = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        sweeps = [int(line.rstrip()) for line in input]
    return sweeps

def core(file, part):
    sweeps = parse_input(file)
    
    # Part 1: Check if each element is smaller than the next element
    increases = 0
    for i in range(len(sweeps) - 1):
        if sweeps[i + 1] > sweeps[i]:
            increases += 1

    # Part 2: Update the sum by adding the next element and removing the pervious one
    # and checking if each sum is greater than the previous one
    sum_increases = 0
    curr = None
    sum = sweeps[0] + sweeps[1]
    for i in range(len(sweeps) - 2):
        sum += sweeps[i + 2]
        if curr != None and sum > curr:
            sum_increases += 1
        curr = sum
        sum -= sweeps[i]

    if part == 1:
        return increases
    if part == 2:
        return sum_increases

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 7)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 5)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))