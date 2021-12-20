import unittest, os

# Read puzzle input and return as usable data structure
def parse_input(file):
    enh_algo = []
    image = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r') as input:
        enh_algo = [x for x in input.readline().rstrip()]
        input.readline()
        for line in input:
            image.append([x for x in line.rstrip()])
    return enh_algo, image

def core(file, times):
    enh_algo, image = parse_input(file)

    # 9 directions to check and keeping track of what an 'empty space' represents due to flashing
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    inf_spc = "0"

    for _ in range(times):
        rows = len(image)
        cols = len(image[0])
        # Image grows 1 in every direction each iteration
        enh_image = [['.' for _ in range(cols + 2)] for _ in range(rows + 2)]
        for row in range(-1, rows + 1):
            for col in range(-1, cols + 1):
                pixel = ""
                # Convert 3x3 square to binary, if out of bounds use 'empty space'
                for rc, cc in dirs:
                    p_row = row + rc
                    p_col = col + cc
                    if 0 <= p_row < rows and 0 <= p_col < cols:
                        pixel += "1" if image[p_row][p_col] == "#" else "0"
                    else:
                        pixel += inf_spc
                # Update new, enhanced image with binary pixel and enhancement algorithm
                enh_image[row + 1][col + 1] = enh_algo[int(pixel, 2)]
        # Set image to enhanced image and update 'empty space'
        inf_spc = "1" if enh_algo[int((inf_spc * 9), 2)] == "#" else "0"
        image = enh_image

    # Displaying the image for the fun...can't really see anything though
    for row in image:
        for ele in row:
            print(ele, end = "")
        print()

    return sum ([line.count("#") for line in image])

# Unit testing on given test input and expected results
class TestCases(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(core('example.txt', 2), 35)
    
    def test_part2(self):
        self.assertEqual(core('example.txt', 50), 3351)

if __name__ == "__main__":
    #unittest.main(verbosity=2)
    
    # Part 1 solution
    #print(core('example.txt', 2))
    print(core('input.txt', 2))
    
    # Part 2 solution
    #print(core('example.txt', 50))
    print(core('input.txt', 50))
        