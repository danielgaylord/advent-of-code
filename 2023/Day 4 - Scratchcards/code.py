import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    cards = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        temp = [line.rstrip().split(": ")[1].rstrip().split(" | ") for line in input]
        for line in temp:
            cards.append([set(line[0].rstrip().split()), set(line[1].rstrip().split())])

    return cards

def core(file):
    cards = parse_input(file)
    total = 0
    copies = [1 for x in range(0, len(cards))]

    for num in range(0, len(cards)):
        card = cards[num]
        winning = card[0].intersection(card[1])
        if len(winning) > 0:
            # Part 1: Winning values give power of 2 points
            total += 2**(len(winning) - 1)

            # Part 2: Winning values give copies of following cards
            for i in range(0, len(winning)):
                copies[num + i + 1] += copies[num]

    return sum(copies)

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    print("Testing...")
    # def test_part1(self):
    #     self.assertEqual(core('example.txt'), 13)
    
    # def test_part2(self):
    #     self.assertEqual(core('example.txt'), 30)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    
    # Part 1 solution
    # print(core('example.txt'))
    # print(core('input.txt'))
    
    # Part 2 solution
    # print(core('example.txt'))
    print(core('input.txt'))
        