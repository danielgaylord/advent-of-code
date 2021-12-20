import unittest, os, heapq
from collections import deque
from functools import reduce

# Read puzzle input and return as usable data structure
def parse_input(file):
    heightmap = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            heightmap.append([int(char) for char in line.rstrip()])
    return heightmap

# Function to go through a basin and mark each spot with a -1 to count as 'visited' and increase size by 1
def mark_basin(start, heightmap):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append(start)
    size = 0
    while queue:
        row, col = queue.popleft()
        if heightmap[row][col] != -1:
            size += 1
            heightmap[row][col] = -1
            for rc, cc in dirs:
                new_row = row + rc
                new_col = col + cc
                if 0 <= new_row < len(heightmap) and 0 <= new_col < len(heightmap[0]) and heightmap[new_row][new_col] != -1 and heightmap[new_row][new_col] != 9:
                    queue.append((new_row, new_col))
    return size

def core(file, part):
    heightmap = parse_input(file)
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows = len(heightmap)
    cols = len(heightmap[0])
    risk_sum = 0

    # Initialize heap to be of 'size' 3
    sizes = [float('-inf'), float('-inf'), float('-inf')]
    heapq.heapify(sizes)
    
    # Part 1
    # For each spot in the heightmap, check to make sure it is smaller than all of its neighbors
    # If so, add its height + 1 to the sum of risks
    for row in range(rows):
        for col in range(cols):
            all_less = True
            for rc, cc in dirs:
                new_row = row + rc
                new_col = col + cc
                if 0 <= new_row < rows and 0 <= new_col < cols and heightmap[row][col] >= heightmap[new_row][new_col]:
                    all_less = False
            if all_less:
                risk_sum += heightmap[row][col] + 1

    # Part 2
    # For each spot in the heightmap, if it hasn't been visited yet and is not a 9 it is a new basin
    # If so, find the size of the basin and mark all of its regions as visited (Heap ensures we only keep top 3 values)
    for row in range(rows):
        for col in range(cols):
            if heightmap[row][col] != -1 and heightmap[row][col] != 9:
                heapq.heappushpop(sizes, mark_basin((row, col), heightmap))
 
    if part == 1:
        return risk_sum
    if part == 2:
        return reduce((lambda x, y: x * y), sizes)
        
# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 15)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 1134)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))