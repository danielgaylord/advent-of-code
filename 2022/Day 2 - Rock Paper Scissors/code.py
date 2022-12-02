import unittest, os, heapq

# Read puzzle input and return as usable data structure
def parse_input(file):
    plays = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        plays = [line.rstrip().split(" ") for line in input]
    return plays

def core(file):
    plays = parse_input(file)

    # Part 1: XYZ are Rock/Paper/Scissors
    score = 0
    ptDict = {"X": {"A": 3, "B": 0, "C": 6}, 
              "Y": {"A": 6, "B": 3, "C": 0}, 
              "Z": {"A": 0, "B": 6, "C": 3}}

    for play in plays:
        if play[1] == "X":
            score += 1
        elif play[1] == "Y":
            score += 2
        else:
            score += 3
        score += ptDict[play[1]][play[0]]

    # Part 2: XYZ are Lose/Tie/Win
    score = 0
    ptDict = {"X": {"A": 3, "B": 1, "C": 2}, 
              "Y": {"A": 1, "B": 2, "C": 3}, 
              "Z": {"A": 2, "B": 3, "C": 1}}

    for play in plays:
        if play[1] == "X":
            score += 0
        elif play[1] == "Y":
            score += 3
        else:
            score += 6
        score += ptDict[play[1]][play[0]]
        
    return score

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt'), 15)
    
    def test_part2(self):
        self.assertEqual(core('example.txt'), 12)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        