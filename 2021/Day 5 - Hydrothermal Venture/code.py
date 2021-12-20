import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    segments = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            line = line.rstrip().split(" -> ")
            seg = [[int(val) for val in point.split(",")] for point in line]
            segments.append(seg)
    return segments

def core(file, part):
    segments = parse_input(file)
    
    # Create sea floor
    maxRow = 0
    maxCol = 0
    for segment in segments:
        for point in segment:
            maxCol = max(maxCol, point[0])
            maxRow = max(maxRow, point[1])
    floor = [[0 for _ in range(maxCol + 1)] for _ in range(maxRow + 1)]
    
    for start, end in segments:
        # Part 1 only cares about horizontal and vertical lines
        if part == 1 and not (start[0] == end[0] or start[1] == end[1]):
            continue
        beginX = start[0]
        beginY = start[1]
        endX = end[0]
        endY = end[1]
        xChange = 0
        yChange = 0
        if beginX < endX:
            xChange = 1
        elif beginX > endX:
            xChange = -1
        if beginY < endY:
            yChange = 1
        elif beginY > endY:
            yChange = -1
        while beginX != endX or beginY != endY:
            floor[beginY][beginX] += 1
            beginX += xChange
            beginY += yChange
        floor[beginY][beginX] += 1
    
    # Count the number of positions where two or more lines intersect
    count = 0
    for r in floor:
        for c in r:
            if c > 1:
                count += 1
    return count

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 5)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 12)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))