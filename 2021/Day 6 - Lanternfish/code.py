import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    ages = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        ages = [int(age) for age in input.readline().split(",")]
    return ages

def calc_fish(age, days_rem, spawn_check):
    spawn = days_rem - age
    family = 0
    while spawn >= 1:
        if spawn_check[spawn]:
            family += spawn_check[spawn]
        else:
            spawn_check[spawn] = 1 + calc_fish(8, spawn - 1, spawn_check)
            family += spawn_check[spawn]
        spawn -= 7
    return family

def core(file, days):
    ages = parse_input(file)
    
    spawn_check = [None for _ in range(300)]
    total = 0
    for age in ages:
        total += 1 + calc_fish(age, days, spawn_check)
    return total

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 80), 5934)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 256), 26984457539)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 80))
    print(core('input.txt', 80))
    
    # Part 2 solution
    #print(core('example.txt', 256))
    print(core('input.txt', 256))