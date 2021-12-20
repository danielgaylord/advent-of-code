import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    patterns = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        temp = [line.rstrip().split(" | ") for line in input]
        for line in temp:
            patterns.append([list(sorted(line[0].split(" "), key=len)), line[1].split(" ")])
    return patterns

def core(file, part):
    patterns = parse_input(file)

    digit_count = [0 for _ in range(10)]
    output_sum = 0
    for pattern in patterns:
        # Find out which sequence represents which digit
        digit_rep = ["" for _ in range(10)]

        # Easy representations based solely on length
        digit_rep[1] = "".join(sorted(pattern[0][0]))
        digit_rep[4] = "".join(sorted(pattern[0][2]))
        digit_rep[7] = "".join(sorted(pattern[0][1]))
        digit_rep[8] = "".join(sorted(pattern[0][-1]))
        
        # Difficult representations look at how many characters are left when removing the characters from each easy representation, for 8 the math is 'flipped'
        for i in range(3, 9):
            minus1, minus4, minus7, minus8 = pattern[0][i], pattern[0][i], pattern[0][i], digit_rep[8]
            for char in digit_rep[1]:
                minus1 = minus1.replace(char, "")
            for char in digit_rep[4]:
                minus4 = minus4.replace(char, "")
            for char in digit_rep[7]:
                minus7 = minus7.replace(char, "")
            for char in pattern[0][i]:
                minus8 = minus8.replace(char, "")

            if len(minus1) == 4 and len(minus4) == 3 and len(minus7) == 3 and len(minus8) == 1:
                digit_rep[0] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 3 and len(minus7) == 3 and len(minus8) == 2:
                digit_rep[2] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 3 and len(minus4) == 2 and len(minus7) == 2 and len(minus8) == 2:
                digit_rep[3] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 2 and len(minus7) == 3 and len(minus8) == 2:
                digit_rep[5] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 5 and len(minus4) == 3 and len(minus7) == 4 and len(minus8) == 1:
                digit_rep[6] = "".join(sorted(pattern[0][i]))
            elif len(minus1) == 4 and len(minus4) == 2 and len(minus7) == 3 and len(minus8) == 1:
                digit_rep[9] = "".join(sorted(pattern[0][i]))
        
        # Loop through each output digit to form the 4-digit number (and count how many of each digit for part 1)
        output = 0
        for digit in pattern[1]:
            output *= 10
            value = digit_rep.index("".join(sorted(digit)))
            output += value
            digit_count[value] += 1

        # easy_sum is for part 1, output_sum is for part 2       
        output_sum += output
    easy_sum = digit_count[1] + digit_count[4] + digit_count[7] + digit_count[8]

    if part == 1:
        return easy_sum
    if part == 2:
        return output_sum

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 26)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 61229)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))
        