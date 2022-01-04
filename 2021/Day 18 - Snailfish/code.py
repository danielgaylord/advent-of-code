import unittest, os

class SnailNumber():
    def __init__(self, string):
        if string[1] == "[":
            comma_loc = self.find_comma(string)
            self.left_num = SnailNumber(string[1:comma_loc])
        else:
            comma_loc = string.index(",")
            self.left_num = int(string[1: comma_loc])
        if string[comma_loc + 1] == "[":
            self.right_num = SnailNumber(string[comma_loc + 1:-1])
        else:
            self.right_num = int(string[comma_loc + 1: -1])

    def __str__(self):
        return " {}\n {}".format(self.left_num, self.right_num)
    
    def find_comma(self, string):
        bracket = 0
        for i in range(1, len(string)):
            if string[i] == "[":
                bracket += 1
            elif string[i] == "]":
                bracket -= 1
            if bracket == 0:
                return i + 1
        return -1
    
    def add(self, snail_num):
        new_number = SnailNumber(self, "")
        new_number.left_num = self
        new_number.right_num = snail_num
        return new_number.reduce()
    
    def reduce():
        pass

    def magnitude(self):
        left = self.left_num if isinstance(self.left_num, int) else self.left_num.magnitude()
        right = self.right_num if isinstance(self.right_num, int) else self.right_num.magnitude()
        return 3 * left + 2 * right

# Read puzzle input and return as usable data structure
def parse_input(file):
    numbers = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            numbers.append(line.rstrip())
    return numbers

def core(file, part):
    numbers = parse_input(file)
    sn = SnailNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    return sn

# Practicing unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 3488)
        self.assertEqual(core('example2.txt', 1), 4140)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 112)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    print(core('example.txt', 1))
    #print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    #print(core('input.txt', 2))
        