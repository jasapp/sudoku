import math

class Cell():
    def __init__(self, value, idx, *args, **kwargs):
        self.value = value
        self.idx = idx
        row = math.floor(idx / 9)
        col = idx % 9

        # the below should just be functions like they were, i just like objects and redundancy 
        self.col_neighbors = [((y*9)+idx)%81 for y in range(0, 9)] # idx in col, e.g. [0, 9, 18, ... 72]
        self.row_neighbors = [(row*9)+x for x in range(0, 9)]      # idx in row, e.g. [0, 1, 2, ... 8], 
        self.box_neighbors = [] # ((9 * row) + column) @jasapp do this
        self.col_neighbors.sort()
        self.row_neighbors.sort()
        self.possible_values = []
        #print(idx, value, self.col_neighbors)
        #print(idx, value, self.row_neighbors)

    def __str__(self):
        return str(self.value)
        # return '(%i %i)' % (self.value, self.idx)

    def __eq__(self, v):
        return v == self.value

    def __ge__(self, v):
        return self.value >= v


class Board():
    def __init__(self, board, *args, **kwargs):
        self.board = board
        self.max_value = 0
        self.populate_board() # turn [0, 0, ... ] into [Cell, Cell, ...]
        # self.populate_probable_values()
        print(self)

    def __str__(self):
        s = ''
        max_str_size = len(str(self.max_value))
        for i in range(0, 81):
            if (i % 27 == 0 and i > 0):
                s += '\n' + '-' * (24 + (8 * len(str(self.max_value)))) + '\n'
            elif (i % 9 == 0 and i > 0):
                s += '\n'
            elif (i % 3 == 0 and i > 0):
                s += ' | '
            # left-pad cell values so board looks nice
            s += ' %s ' % (str(self.board[i]).zfill(max_str_size))
        return s

    def print_board(self):
        print(self)

    def populate_board(self):
        for idx in range(0, len(self.board)):
            value = self.board[idx]
            self.board[idx] = Cell(value, idx)
            if (value > self.max_value):
                self.max_value = value 

    def populate_probable_values(self):
        """ look at a Cell's row/col/box neighbors, find out what it could possibly be """
        return None

    def get_most_probable_cell(self):
        """ looks through current board and finds Cell with lowest num of possible_values """
        return None

    def empty_spots(self):
        """ return array of indices where value is 0 """
        a = [i for i,x in enumerate(self.board) if x == 0]
        return a

    def offset(self, v):
        """ returns array of Cells of current board offset by v """
        a = [Cell(x.value + v) for x in self.board]
        return a
