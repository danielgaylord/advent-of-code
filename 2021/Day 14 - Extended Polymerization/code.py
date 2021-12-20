import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    template = ""
    pairs = {}
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        template = input.readline().rstrip()
        input.readline() # Skip "/n"
        for line in input:
            temp = line.rstrip().split(" -> ")
            pairs[temp[0]] = temp[1]
    return template, pairs

# Add the given element to the given list an amount number of times
def add_to_dict(element, dictionary, amount):
    if element in dictionary:
        dictionary[element] += amount
    else:
        dictionary[element] = amount

def core(file, iterations):
    # First build the initial dictionaries using the puzzle input so we begin with...
    # - one dictionary to keep count of how many times each element occurs
    # - another dictionary to do the same for pairs
    template, pairs = parse_input(file)
    ele_counts = {}
    pair_counts = {} 
    # Add first element since below loop begins at 1
    add_to_dict(template[0], ele_counts, 1)
    for i in range(1, len(template)):
        add_to_dict(template[i], ele_counts, 1)
        add_to_dict(template[i - 1:i + 1], pair_counts, 1)

    # For the number of iterations, go through each pair in the pair count dict
    # Temp dict is used so each step can occur simultaneously
    for _ in range(iterations):
        temp_pair_counts = pair_counts.copy()
        for pair in pair_counts:
            if pair in pairs:
                amt_of_pair = pair_counts[pair]
                ele_to_add = pairs[pair]
                # Add new element to element count dict
                add_to_dict(ele_to_add, ele_counts, amt_of_pair)
                # Add the newly formed pairs to the temp dict and reduce the
                # amount of the previous pair
                # e.g. HHH > HBHBH means...
                # - HH was 2 pairs, now it's 0 pairs
                # - HB (new left) now has 2 pairs
                # - BH (new right) now has 2 pairs
                new_left_pair = pair[0] + ele_to_add
                new_right_pair = ele_to_add + pair[1]
                add_to_dict(new_left_pair, temp_pair_counts, amt_of_pair)
                add_to_dict(new_right_pair, temp_pair_counts, amt_of_pair)
                add_to_dict(pair, temp_pair_counts, -amt_of_pair)
        # Move temp results to main pair count dict
        pair_counts = temp_pair_counts
    
    # FInally, return most common element's count minus least common element's count
    max_ele = max(ele_counts.values())
    min_ele = min(ele_counts.values())
    return max_ele - min_ele

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 10), 1588)
    
    def test_extended_polymerization_part2(self):
        self.assertEqual(core('example.txt', 40), 2188189693529)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 10))
    print(core('input.txt', 10))
    
    # Part 2 solution
    #print(core('example.txt', 40))
    print(core('input.txt', 40))
        