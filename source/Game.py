from __future__ import print_function
from Tetramino import Tetramino
from helper import print_matrix

class Game:
    def __init__(self):
        self.N_ROWS = 22
        self.N_COLUMNS = 10

        # PLAY_AREA: a list of strings where each string represents one row
        self.PLAY_AREA = [list('.' * self.N_COLUMNS) for row in range(self.N_ROWS)]
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

    def print_spawn_matrix(self):
        size = len(self.active_tetramino.tetramino_matrix)
