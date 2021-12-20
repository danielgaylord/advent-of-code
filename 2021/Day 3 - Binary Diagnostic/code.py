import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    report = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        report = [line.rstrip() for line in input]
    return report

def core(file, part):
    report = parse_input(file)
    
    report_size = len(report)
    gamma, epsil = '', ''
    result = list(map(list, zip(*report)))
    oxygen = [1 for _ in range(report_size)]
    co2 = [1 for _ in range(report_size)]

    for l in result:
        total = sum(map(int, l))
        gamma += "1" if total >= report_size / 2 else "0"
        epsil += "0" if total >= report_size / 2 else "1"

        o_size = sum(oxygen)
        if o_size > 1:
            o_total = sum([int(r) * e for r, e in zip(l, oxygen)])
            if o_total >= o_size / 2:
                check = "1"
            else:
                check = "0"
            for i in range(report_size):
                oxygen[i] = 1 * oxygen[i] if l[i] == check else 0 

        c_size = sum(co2)
        if c_size > 1:
            c_total = sum([int(r) * e for r, e in zip(l, co2)])
            if c_total >= c_size / 2:
                check = "0"
            else:
                check = "1"
            for i in range(report_size):
                co2[i] = 1 * co2[i] if l[i] == check else 0

    if part == 1:
        return int(int(gamma, 2)) * int(int(epsil, 2))
    if part == 2:
        return int(int(report[oxygen.index(1)], 2)) * int(int(report[co2.index(1)], 2))

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 198)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 230)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))