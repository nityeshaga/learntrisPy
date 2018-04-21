from __future__ import print_function
from Tetramino import Tetramino
from helper import print_matrix

class Game:
    def __init__(self):
        self.N_ROWS = 22
        self.N_COLUMNS = 10

        # PLAY_AREA: a list of strings where each string represents one row
        self.PLAY_AREA = [list('.' * self.N_COLUMNS) for row in range(self.N_ROWS)]

        # for debugging purposes
        # print(type(self.PLAY_AREA), type(self.PLAY_AREA[0]))
        
        self.SCORE = 0
        self.N_LINES_CLEARED = 0
        self.active_tetramino = Tetramino('I') # default value -- the I tetramino

    def read_play_area(self):
        for rnum in range(22):
            line = raw_input()
            new_row = line.replace(' ', '')
            self.PLAY_AREA[rnum] = new_row

    def clear_matrix(self):
        self.PLAY_AREA = ['.' * self.N_COLUMNS for row in range(self.N_ROWS)]

    def display_score(self):
        print(self.SCORE)

    def display_n_lines_cleared(self):
        print(self.N_LINES_CLEARED)

    def one_step(self):
        for rnum, row in enumerate(self.PLAY_AREA):
            if not '.' in row:
                self.PLAY_AREA[rnum] = '.' * self.N_COLUMNS
                self.N_LINES_CLEARED += 1
                self.SCORE += 100

    def set_active_tetramino(self, tetramino_key):
        self.active_tetramino = Tetramino(tetramino_key)

    def print_spawned_tetramino(self):

        # debug stuff
        print(type(self.PLAY_AREA), type(self.PLAY_AREA[0]))
        # this should show the types to be `list` , `list` instead
        # of `list` , `string`

        if len(self.active_tetramino.tetramino_matrix) == 2:
            self.spawn_active_tetramino(row_num=0, col_num=4)
        else:
            self.spawn_active_tetramino(row_num=0, col_num=3)

    def spawn_active_tetramino(self, row_num=0, col_num=0):
        active_tetramino_size = len(self.active_tetramino.tetramino_matrix)
        for row_idx in range(row_num, row_num+active_tetramino_size):
            self.PLAY_AREA[row_idx][col_num:col_num+active_tetramino_size] = \
                    self.active_tetramino.tetramino_matrix[row_idx][:]
