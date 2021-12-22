from functools import lru_cache
import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    p1_start = 0
    p2_start = 0
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        p1_start = int(input.readline().rstrip()[-1]) - 1
        p2_start = int(input.readline().rstrip()[-1]) - 1
    return p1_start, p2_start

# Part 1 die
def deterministic_die(p1_place, p2_place, spaces, faces, to_win):
    die_value = p1_score = p2_score = rolls = 0
    p1_turn = True

    # Keep taking turns until someone wins
    while p1_score < to_win and p2_score < to_win:

        # Roll die 3 times making sure it 'resets' to 1 when it passes # of faces
        roll1, die_value = die_value + 1, (die_value + 1) % faces
        roll2, die_value = die_value + 1, (die_value + 1) % faces
        roll3, die_value = die_value + 1, (die_value + 1) % faces
        rolls += 3
        total_move = roll1 + roll2 + roll3

        # On any player's turn, add the total of the rolls to the player's location,
        # make sure they pass the last space back to 1, then increase their score
        if p1_turn:
            p1_place += total_move
            p1_place %= spaces
            p1_score += p1_place + 1
        else:
            p2_place += total_move
            p2_place %= spaces
            p2_score += p2_place + 1
        # change turns
        p1_turn = not p1_turn
    
    # Set winner and loser based on final score and return this info w/ number of rolls
    if p1_score > p2_score:
        win, lose = p1_score, p2_score
    else:
        win, lose = p2_score, p1_score
    return win, lose, rolls

# Part 2 die
def quantum_die(p1_place, p2_place, spaces, faces, to_win):

    # Caching for a DP solution so it doesn't run forever
    @lru_cache(maxsize=None)
    def take_turn(p1_score, p2_score, p1_place, p2_place, p1_turn):
        # If a player won, return this win to be calculated
        if p1_score >= to_win:
            return 1, 0
        if p2_score >= to_win:
            return 0, 1

        tot_p1_wins = 0
        tot_p2_wins = 0

        for roll1 in range(1, faces + 1):
            for roll2 in range(1, faces + 1):
                for roll3 in range(1, faces + 1):
                    total_move = roll1 + roll2 + roll3

                    # On any player's turn, add the total of the rolls to the player's location,
                    # make sure they pass the last space back to 1, then increase their score.
                    # Hold in a temp variable so it doesn't mess up future calls in this timeline
                    if p1_turn:
                        new_place = p1_place + total_move
                        new_place %= spaces
                        new_score = p1_score + new_place + 1

                        # Split universes for the 27 different combinations of rolls and change turn
                        p1_wins, p2_wins = take_turn(new_score, p2_score, new_place, p2_place, not p1_turn)
                    else:
                        new_place = p2_place + total_move
                        new_place %= spaces
                        new_score = p2_score + new_place + 1

                        # Split universes for the 27 different combinations of rolls and change turn
                        p1_wins, p2_wins = take_turn(p1_score, new_score, p1_place, new_place, not p1_turn)
                    
                    # Add wins to the total of each player based on the branches of this timeline and return them
                    tot_p1_wins += p1_wins
                    tot_p2_wins += p2_wins     
        return tot_p1_wins, tot_p2_wins
    
    # To set off the recursive calls and return the universe winners
    return take_turn(0, 0, p1_place, p2_place, True)

def core(file, part):
    p1_start, p2_start = parse_input(file)
    win = lose = rolls = None

    if part == 1:
        win, lose, rolls = deterministic_die(p1_start, p2_start, 10, 100, 1000)
        return min(win, lose) * rolls
    if part == 2:
        p1_wins, p2_wins = quantum_die(p1_start, p2_start, 10, 3, 21)
        return max(p1_wins, p2_wins)

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 739785)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 444356092776315)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))