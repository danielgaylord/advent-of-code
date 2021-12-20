import unittest, os
from collections import defaultdict

# Read puzzle input and return as usable data structure
def parse_input(file):
    cave_map = defaultdict(list)
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            connection = line.rstrip().split("-")

            # Create a map of every left node to every right node an vise versa
            # If one of the nodes is start, only keep track of what start goes to
            # Similarly if one node is end, only keep track of what goes to end
            if connection[1] != "start" and connection[0] != "end":
                cave_map[connection[0]].append(connection[1])
            if connection[0] != "start" and connection[1] != "end":
                cave_map[connection[1]].append(connection[0])
    
    return cave_map

def core(file, small_visits):
    cave_map = parse_input(file)

    # Recursive depth-first search
    def dfs(cave_map, visited, loc, visited_small):
        
        # Keep track of which nodes have been visited and how many times
        # If just doing part 1, you only need to add the visited node to
        # the dict or use a set instead
        new_visited = visited.copy()
        if loc == "end":
            return 1
        if loc in new_visited:
            new_visited[loc] += 1
        else:
            new_visited[loc] = 1

        # For every node that the current location points to...
        # If going to an upper case node, just go, no worries
        # If going to a lower case node, make sure it's not visited already
        paths = 0
        for to in cave_map[loc]:
            if to.isupper():
                paths += dfs(cave_map, new_visited, to, visited_small)
            elif to not in new_visited:
                paths += dfs(cave_map, new_visited, to, visited_small)
            # For part 2 you can also go to a lower case node if you haven't been
            # twice already or to another node twice
            elif to in new_visited and new_visited[to] < small_visits and not visited_small:
                paths += dfs(cave_map, new_visited, to, True)
        
        return paths

    visited = {}
    return dfs(cave_map, visited, "start", False)

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 10)
        self.assertEqual(core('example2.txt', 1), 19)
        self.assertEqual(core('example3.txt', 1), 226)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 36)
        self.assertEqual(core('example2.txt', 2), 103)
        self.assertEqual(core('example3.txt', 2), 3509)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))