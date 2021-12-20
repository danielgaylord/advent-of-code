import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    chunks = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        for line in input:
            chunks.append(line.rstrip())
    return chunks

def core(file, part):
    chunks = parse_input(file)
    matches = {"(": ")", "[": "]", "{": "}", "<": ">"}
    open = "([{<"
    incomplete = []
    
    # Part 1: For each char in each chunk, if it's an opening bracket add to stack 
    # otherwise, pop last opening braket and check if it matches the closing one
    # if not, add to score and fuhgeddaboudit
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupt_score = 0
    for chunk in chunks:
        chars = []
        corrupt = False
        for char in chunk:
            if char in open:
                chars.append(char)
            else:
                check = chars.pop()
                if matches[check] != char:
                    corrupt_score += points[char]
                    corrupt = True
        # Part 2 addendum, to make sure we can look at incomplete lines, remaining 
        # chars of incomplete lines to a list
        if not corrupt:
            incomplete.append(chars)
    
    # Part 2: For each incomplete line, go through chars in reverse order to
    # calculate the scores and to a list, finally sort the list and find the
    # middle element
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    incomp_scores = []
    for remain in incomplete:
        temp_score = 0
        for char in remain[::-1]:
            temp_score *= 5
            temp_score += points[matches[char]]
        incomp_scores.append(temp_score)
    incomp_scores = list(sorted(incomp_scores))

    if part == 1:
        return corrupt_score
    if part == 2:
        return incomp_scores[len(incomp_scores) // 2]

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 1), 26397)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 2), 288957)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 1))
    print(core('input.txt', 1))
    
    # Part 2 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))
        