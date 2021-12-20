import unittest, os
from collections import defaultdict

# Read puzzle input and return as usable data structure
def parse_input(file):
    target_area = defaultdict(list)
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            prune = line.rstrip().split(": ")
            prune = prune[1].split(", ")
            for dim in prune:
                dim = dim.split("=")
                target_area[dim[0]] = [int(x) for x in dim[1].split("..")]
    return target_area

def core(file, part):
    target_area = parse_input(file)
    probe_s = (0, 0)

    # 'Quick' calc for part 1: Sum of 0 through distance between lowest target y and the start y
    max_height = 0
    y_diff = abs(target_area["y"][0] - probe_s[1])
    for y_val in range(0, y_diff):
        max_height += y_val
    
    if part == 1:
        return max_height

    # For all possible initial y velocities, they will range from the lowest y target to the
    # greatest height (part 1 solution). For each of these velocities, see how many steps it
    # takes them to hit the target area (potentially multiple steps per velocity)
    possible_y = defaultdict(list)
    for init_y in range(target_area["y"][0], y_diff):
        check = init_y
        y_loc = probe_s[1]
        steps = 0
        while y_loc >= target_area["y"][0]:
            if target_area["y"][0] <= y_loc <= target_area["y"][1]:
                possible_y[steps].append(init_y)
            steps += 1
            y_loc += check
            check -= 1

    # For all possible initial x velocities, they will range from the lowest width (similar
    # to greatest height) to the greatest x target. For each of these velocities, see how many 
    # steps it takes them to hit the target area (potentially multiple steps per velocity) The 
    # max number of steps is the max y steps, as x cannot go lower than 0
    min_x = 0
    x_loc = 0
    while x_loc < target_area["x"][0]:
        min_x += 1
        x_loc += min_x
    possible_x = defaultdict(list)
    for init_x in range(min_x, target_area["x"][1] + 1):
        check = init_x
        x_loc = probe_s[0]
        steps = 0
        while steps <= max(possible_y.keys()):
            if target_area["x"][0] <= x_loc <= target_area["x"][1]:
                possible_x[steps].append(init_x)
            steps += 1
            x_loc += check
            check = max(check - 1, 0)

    # Create a set of all possible initial velocities based on initial y and x pairs based on
    # number of steps
    init_vel = set()
    for step in range(max(possible_y.keys()) + 1):
        if step in possible_x and step in possible_y:
            for init_x in possible_x[step]:
                for init_y in possible_y[step]:
                    init_vel.add((init_x, init_y))

    return len(init_vel)

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 45)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 112)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))
        