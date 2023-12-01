import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    lines = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        lines = [line.rstrip() for line in input]
    return lines

def core(file):
    lines = parse_input(file)
    conversion = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    total = 0
    
    for line in lines:
        digits = ""
        for i in range(0, len(line)):
            # Part 1: Total of calibration values
            if line[i].isdigit():
                digits += line[i]

            # Part 2: Total of calibration values including string numbers
            for k in conversion.keys():
                if line.startswith(k, i):
                    digits += conversion[k]

        total += (int(digits[0]) * 10) + int(digits[-1])

    return total

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    print("Testing...")
    # def test_part1(self):
    #     self.assertEqual(core('example.txt'), 142)
    
    # def test_part2(self):
    #     self.assertEqual(core('example.txt'), 281)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        