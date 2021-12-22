import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    steps = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            step = []
            bit, coord = line.rstrip().split(" ")
            step.append(1 if bit == "on" else 0)
            coord = coord.split(",")
            x_dim = coord[0].split("=")[1].split("..")
            y_dim = coord[1].split("=")[1].split("..")
            z_dim = coord[2].split("=")[1].split("..")
            cuboids = set()
            for x in range(int(x_dim[0]), int(x_dim[1]) + 1):
                for y in range(int(y_dim[0]), int(y_dim[1]) + 1):
                    for z in range(int(z_dim[0]), int(z_dim[1]) + 1):
                        cuboids.add((x, y, z))
            step.append(cuboids)
            steps.append(step)
    return steps

def core(file, part):
    steps = parse_input(file)
    
    for step in steps:
        print(step)

    return

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 39)
        self.assertEqual(core('example2.txt', 1), 590784)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), None)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    print(core('example.txt', 1))
    #print(core('example2.txt', 1))
    #print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    #print(core('input.txt', 2))