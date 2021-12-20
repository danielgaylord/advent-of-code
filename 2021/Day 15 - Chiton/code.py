import unittest, os, heapq

# Read puzzle input and return as usable data structure
def parse_input(file):
    grid = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            row = [ch for ch in line.rstrip()]
            grid.append(row)
    return grid

# For part 2, added growth input that is how much bigger length and width are
def core(file, growth):
    grid = parse_input(file)
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows = len(grid)
    cols = len(grid[0])
    
    # Start at top-left, end at bottom-right and queue up starting location
    start = (0, 0)
    end = ((rows * growth) - 1, (cols * growth) - 1)
    to_visit = [(0, start)]
    distances = {start: 0}
    heapq.heapify(to_visit)
    while to_visit:
        priority, loc = heapq.heappop(to_visit)
        
        # Quick exit when we get to end of path
        if loc == end:
            break
        row, col = loc[0], loc[1]
        
        # To make sure that we only process each location once, if we can get to this
        # location my a shorter path, just move on
        for rc, cc, in dirs:
            new_row = row + rc
            new_col = col + cc

            # Check bounds
            if 0 <= new_row < (rows * growth) and 0 <= new_col < (cols * growth):
                
                # Weight is the value of the location on the original grid + growth which ends up 
                # being sum of row, col // size of original grid. Also make sure to 'loop' from
                # a value of 9 back to 1
                weight = int(grid[new_row % rows][new_col % rows])
                weight += (new_row // rows) + (new_col // cols)
                if weight > 9:
                    weight %= 9
                new_dist = distances[loc] + weight
                new_loc = (new_row, new_col)

                # Only add a node to be visited if we haven't been there before or we have, but we
                # found a shorter path
                if (new_loc in distances and new_dist < distances[new_loc]) or new_loc not in distances:
                    distances[new_loc] = new_dist
                    # Dijkstra
                    #priority = new_dist
                    # A*
                    priority = new_dist + (abs(new_row - end[0]) + abs(new_col - end[1]))
                    heapq.heappush(to_visit, (priority, new_loc))
    
    return distances[end]

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 40)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 5), 315)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 5))
    print(core('input.txt', 5))
        