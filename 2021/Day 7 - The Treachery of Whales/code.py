import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    hor_pos = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        hor_pos = [int(age) for age in input.readline().split(",")]
    return hor_pos

def core(file, part):
    hor_pos = parse_input(file)

    currMin = float('inf')
    for x in range(min(hor_pos), max(hor_pos) + 1):
        subtotal = 0
        for num in hor_pos:
            pos_diff = abs(num - x)

            if part == 1:
                subtotal += pos_diff
            if part == 2:
                subtotal += (pos_diff * (pos_diff + 1)) // 2

            # Quick exit if we can already tell we are getting too large
            if subtotal > currMin:
                break
        currMin = min(subtotal, currMin)
    return currMin

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 37)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 168)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))
        