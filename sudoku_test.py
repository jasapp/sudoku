import sudoku as s
import puzzles as p
import unittest
from cStringIO import StringIO
import sys

class TestSudoku(unittest.TestCase):

    # 0 is used to represent an empty spot on the board
    # values 1 through 9 are considered occupied spots
    # empty_board creates an array of 0s of length 81
    def test_empty_board(self):
        e = s.empty_board()
        self.assertEqual(len(e), 81)
        for i in e:
            self.assertEqual(i,0)

    # the next function is print_board()
    # it takes an array of length 81 and prints them like a sudoku puzzle
    # This is sample output from my print_board function. I don't print zeros,
    # but everything else I print. The tests check to see if you've got more than
    # 9 newline characters and if you've got 81 1s on the invalid board

    # s.print_board(s.empty_board())
    #          |         |         
    #          |         |         
    #          |         |         
    # ----------------------------
    #          |         |         
    #          |         |         
    #          |         |         
    # ----------------------------
    #          |         |         
    #          |         |         
    #          |         |         

    # s.print_board(p.invalid)
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 
    # ----------------------------
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 
    # ----------------------------
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 
    #  1  1  1 | 1  1  1 | 1  1  1 

    # when numbers are greater than 9 things get misaligned, but that doesn't matter
    # this will give you an idea how array indexes translate into positions on the board
    #      1   2  | 3   4    5 | 6   7   8 
    #  9   10  11 | 12  13  14 | 15  16  17 
    #  18  19  20 | 21  22  23 | 24  25  26 
    # ----------------------------
    #  27  28  29 | 30  31  32 | 33  34  35 
    #  36  37  38 | 39  40  41 | 42  43  44 
    #  45  46  47 | 48  49  50 | 51  52  53 
    # ----------------------------
    #  54  55  56 | 57  58  59 | 60  61  62 
    #  63  64  65 | 66  67  68 | 69  70  71 
    #  72  73  74 | 75  76  77 | 78  79  80

    def test_print_board(self):

        sys.stdout = output = StringIO()

        s.print_board(s.empty_board())
        self.assertTrue(output.getvalue().count("\n") >= 9)

        s.print_board(p.invalid)
        self.assertTrue(output.getvalue().count("\n") >= 9)
        self.assertTrue(output.getvalue().count("1") == 81)

        sys.stdout = sys.__stdout__

    # offset takes an array as the first argument and offsets 
    # all the values in the array by the second argument
    def test_offset(self):
        r = s.offset([0,1,2,3], 1)
        self.assertEqual(r, [1,2,3,4])

        r = s.offset([0,1,2,3], 5)
        self.assertEqual(r, [5,6,7,8])

        r = s.offset([0,0,0], 5)
        self.assertEqual(r, [5,5,5])

    # the column_indexes function takes a column number [0 -> 8] and returns 
    # an array containing a list of the *indexes* for that column...
    # An example might make more sense...

    #  we're using an array of length 81 to represent a board
    #  if we were to print the indexes this is what we'd see
    #  0   1   2  | 3   4    5 | 6   7   8 
    #  9   10  11 | 12  13  14 | 15  16  17 
    #  18  19  20 | 21  22  23 | 24  25  26 
    # ----------------------------
    #  27  28  29 | 30  31  32 | 33  34  35 
    #  36  37  38 | 39  40  41 | 42  43  44 
    #  45  46  47 | 48  49  50 | 51  52  53 
    # ----------------------------
    #  54  55  56 | 57  58  59 | 60  61  62 
    #  63  64  65 | 66  67  68 | 69  70  71 
    #  72  73  74 | 75  76  77 | 78  79  80

    # this array is p1 from puzzles.py
    # p1[0] = 7
    # p1[1] = 8
    # p1[2] = 9
    # p1[3] = 0
    # p1[9] = 1
    # p1[80] = 6
    #  7  8  9 |    2    |    3  5 
    #  1       |    4  3 | 7       
    #        4 | 8  7    |    2  1 
    # ----------------------------
    #  9       | 4       |    7    
    #          |         |         
    #     5    |       2 |         
    # ----------------------------
    #  2  6    |    1  8 | 3       
    #        3 | 2  5    |       8 
    #  8  1    |    3    | 2  5  6 

    # so we'd like column indexes to take a column number which can be 0 through 8
    # and return a list of all the indexes in that column. Remember, these are just
    # indexes and NOT values from the board. You'll want to use the offset function
    # that we've already written inside this function
    # for example:
    # >>> column_indexes(0)
    # [0, 9, 18, 27, 36, 45, 54, 63, 72]
    #
    # >>> column_indexes(1)
    # [1, 10, 19, 28, 37, 46, 55, 64, 73]
    #
    # >>> column_indexes(5)
    # [5, 14, 23, 32, 41, 50, 59, 68, 77]
    #

    def test_column_indexes(self):
        self.assertEqual(s.column_indexes(0), [0, 9, 18, 27, 36, 45, 54, 63, 72])
        self.assertEqual(s.column_indexes(1), [1, 10, 19, 28, 37, 46, 55, 64, 73])
        self.assertEqual(s.column_indexes(5), [5, 14, 23, 32, 41, 50, 59, 68, 77])
        self.assertEqual(s.column_indexes(8), [8, 17, 26, 35, 44, 53, 62, 71, 80])
        
    # empty_spots takes an array of length 81 and returns the 
    # indexes of every zero in the array
    # empty_spots([0,1,9,0,1,1,1,1....]) -> [0,3]
    def test_empty_spots(self):
        e = s.empty_board()
        r = s.empty_spots(e)
        self.assertEqual(r,range(0,81))
        
        e[0] = 1
        self.assertEqual(e,[1] + e[1:])

        e[0] = 9
        self.assertEqual(e,[9] + e[1:])

        e[0] = 1
        e[1] = 2
        e[4] = 3
        self.assertEqual(e,[1,2,0,0,3] + e[5:])

if __name__ == '__main__':
    unittest.main()
