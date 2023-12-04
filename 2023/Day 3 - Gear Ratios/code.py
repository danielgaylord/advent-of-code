import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    schematic = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            schematic.append([char for char in line.rstrip()])

    return schematic

def core(file):
    schematic = parse_input(file)
    symloc = {}
    total = 0
    gears = {}
    geartotal = 0

    for y in range(0, len(schematic)):
        for x in range(0, len(schematic[y])):
            symbol = schematic[y][x]
            if not symbol.isdigit() and not symbol == '.':
                if y not in symloc:
                    symloc[y] = [x]
                else:
                    symloc[y] += [x]
            if symbol == '*':
                gears[str(x) + ", " + str(y)] = []
    
    print(gears)

    for y in range(0, len(schematic)):
        partnum = 0
        validpart = False
        potgear = ""
        for x in range(0, len(schematic[y])):
            digit = schematic[y][x]
            if digit.isdigit():
                if partnum == 0:
                    if ((x - 1) in symloc.get(y - 1, [])) or ((x - 1) in symloc.get(y, [])) or ((x - 1) in symloc.get(y + 1, [])):
                        validpart = True
                        if str(x - 1) + ", " + str(y - 1) in gears:
                            potgear = str(x - 1) + ", " + str(y - 1)
                        if str(x - 1) + ", " + str(y) in gears:
                            potgear = str(x - 1) + ", " + str(y)
                        if str(x - 1) + ", " + str(y + 1) in gears:
                            potgear = str(x - 1) + ", " + str(y + 1)
                if ((x) in symloc.get(y - 1, [])) or ((x) in symloc.get(y + 1, [])):
                    validpart = True
                    if str(x) + ", " + str(y - 1) in gears:
                        potgear = str(x) + ", " + str(y - 1)
                    if str(x) + ", " + str(y + 1) in gears:
                        potgear = str(x) + ", " + str(y + 1)
                partnum *= 10
                partnum += int(digit)
            else:
                if partnum != 0:
                    if ((x) in symloc.get(y - 1, [])) or ((x) in symloc.get(y, [])) or ((x) in symloc.get(y + 1, [])):
                        validpart = True
                        if str(x) + ", " + str(y - 1) in gears:
                            potgear = str(x) + ", " + str(y - 1)
                        if str(x) + ", " + str(y ) in gears:
                            potgear = str(x) + ", " + str(y )
                        if str(x) + ", " + str(y + 1) in gears:
                            potgear = str(x) + ", " + str(y + 1)
                if validpart:
                    total += partnum
                    if potgear:
                        gears[potgear] += [partnum]
                partnum = 0
                validpart = False
                potgear = ""
        if partnum != 0 and validpart:
            total += partnum
            if potgear:
                gears[potgear] += [partnum]
    
    for gear, values in gears.items():
        if len(values) == 2:
            gearval = values[0] * values[1]
            geartotal += gearval

    return geartotal

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    print("Testing...")
    # def test_part1(self):
    #     self.assertEqual(core('example.txt'), 4361)
    
    # def test_part2(self):
    #     self.assertEqual(core('example.txt'), 467835)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        