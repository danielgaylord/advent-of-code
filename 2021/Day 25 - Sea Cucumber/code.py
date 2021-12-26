import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    seafloor = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            row = [char for char in line.rstrip()]
            seafloor.append(row)
    return seafloor

def print_seafloor(seafloor):
    for row in seafloor:
        for space in row:
            print(space, end="")
        print()
    print()

def core(file, part):
    seafloor = parse_input(file)
    rows = len(seafloor)
    cols = len(seafloor[0])

    movement = True
    steps = 0
    while movement:
        movement = False
        tempfloor = [["." for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if seafloor[row][col] == ">":
                    if seafloor[row][(col + 1) % cols] == ".":
                        tempfloor[row][(col + 1) % cols] = ">"
                        movement = True
                    else:
                        tempfloor[row][col] = ">"
                if seafloor[row][col] == "v":
                    if (seafloor[(row + 1) % rows][col] == "." and not seafloor[(row + 1) % rows][(col - 1) % cols] == ">") or (seafloor[(row + 1) % rows][col] == ">" and seafloor[(row + 1) % rows][(col + 1) % cols] == "."):
                        tempfloor[(row + 1) % rows][col] = "v"
                        movement = True
                    else:
                        tempfloor[row][col] = "v"
        seafloor = tempfloor
        steps += 1

    return steps  

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 58)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 2758514936282235)

if __name__ == "__main__":
    #unittest.main(verbosity=2)

    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    #print(core('input.txt', 2))