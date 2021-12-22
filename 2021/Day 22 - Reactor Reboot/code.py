import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    steps = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            step = {}
            bit, coord = line.rstrip().split(" ")
            step["bit"] = 1 if bit == "on" else 0
            coord = coord.split(",")
            x_dim = [int(e) for e in coord[0].split("=")[1].split("..")]
            y_dim = [int(e) for e in coord[1].split("=")[1].split("..")]
            z_dim = [int(e) for e in coord[2].split("=")[1].split("..")]
            cuboids = set()
            if -50 <= x_dim[0] <= 50 and -50 <= x_dim[1] <= 50 and -50 <= y_dim[0] <= 50 and -50 <= y_dim[1] <= 50 and -50 <= z_dim[0] <= 50 and -50 <= z_dim[1] <= 50:
                for x in range(x_dim[0], x_dim[1] + 1):
                    for y in range(y_dim[0], y_dim[1] + 1):
                        for z in range(z_dim[0], z_dim[1] + 1):
                            cuboids.add((x, y, z))
            step["cuboids"] = cuboids
            steps.append(step)
    return steps

def core(file, part):
    steps = parse_input(file)
    
    on = set()
    for step in steps:
        if step["bit"] == "on":
            on.union(step["cuboids"])
        else:
            on.difference(step["cuboids"])

    return len(on)

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
    #print(core('example.txt', 1))
    print(core('example2.txt', 1))
    #print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    #print(core('input.txt', 2))