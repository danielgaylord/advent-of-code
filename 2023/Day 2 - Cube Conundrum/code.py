import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    games = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        games = [line.rstrip() for line in input]

    for game in range(0, len(games)):
        info = [line.split(", ") for line in (games[game].split(": ")[1]).split("; ")]
        games[game] = info

    return games

def core(file):
    games = parse_input(file)
    bag = {"red": 12, "green": 13, "blue": 14}
    total = 0
    powertotal = 0
    
    for game in range(0, len(games)):
        minbag = {"red": 0, "green": 0, "blue": 0}
        valid = True
        for info in games[game]:
            for pull in info:
                pullinfo = pull.split(" ")
                # Part 1: Which games are valid within confines of bag?
                if int(pullinfo[0]) > bag[pullinfo[1]]:
                    valid = False
                
                # Part 2: What is the min of each color that could be in a bag per game?
                if int(pullinfo[0]) > minbag[pullinfo[1]]:
                    minbag[pullinfo[1]] = int(pullinfo[0])
        
        if valid:
            total += (game + 1)
        power = minbag["red"] * minbag["blue"] * minbag["green"]
        powertotal += power

    return powertotal

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    print("Testing...")
    # def test_part1(self):
    #     self.assertEqual(core('example.txt'), 8)
    
    # def test_part2(self):
    #     self.assertEqual(core('example.txt'), 2286)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
        