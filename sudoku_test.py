import sudoku as s
import puzzles as p
import unittest

class TestSudoku(unittest.TestCase):

    # 0 is used to represent an empty spot on the board
    # values 1 through 9 are considered occupied spots
    # empty_board creates an array of 0s of length 81
    def test_empty_board(self):
        e = s.empty_board()
        self.assertEqual(len(e), 81)
        for i in e:
            self.assertEqual(i,0)
    
    # offset takes an array as the first argument and offsets 
    # all the values in the array by the second argument
    def test_offset(self):
        r = s.offset([0,1,2,3], 1)
        self.assertEqual(r, [1,2,3,4])

        r = s.offset([0,1,2,3], 5)
        self.assertEqual(r, [5,6,7,8])

        r = s.offset([0,0,0], 5)
        self.assertEqual(r, [5,5,5])

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
