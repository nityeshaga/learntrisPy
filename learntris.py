#!/usr/bin/python

from __future__ import print_function
import sys

TETRAMINO = {'I': ['....', 'cccc', '....', '....'],
             'O': ['yy', 'yy'],
             'Z': ['rr.', '.rr', '...'],
             'S': ['.gg', 'gg.', '...'],
             'J': ['b..', 'bbb', '...'],
             'L': ['..o', 'ooo', '...'],
             'T': ['.m.', 'mmm', '...']}

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

class Game:
    N_ROWS = 22
    N_COLUMNS = 10

    # PLAY_AREA: a list of strings where each string represents one row
    PLAY_AREA = ['.' * N_COLUMNS for row in range(N_ROWS)]

    SCORE = 0

    N_LINES_CLEARED = 0

    active_tetramino = TETRAMINO['I'] # default value -- the I tetramino

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
        self.active_tetramino = TETRAMINO[tetramino_key]

    def display_active_tetramino(self):
        print_matrix(self.active_tetramino)


if __name__ == '__main__':

    myGame = Game()
    execute_instruction = {'q': sys.exit, 
                           'p': (lambda: print_matrix(myGame.PLAY_AREA)),
                           'g': myGame.read_play_area,
                           'c': myGame.clear_matrix,
                           '?s': myGame.display_score,
                           '?n': myGame.display_n_lines_cleared,
                           's': myGame.one_step,
                           't': myGame.display_active_tetramino,
                           'I': (lambda: myGame.set_active_tetramino('I')),
                           'O': (lambda: myGame.set_active_tetramino('O')),
                           'Z': (lambda: myGame.set_active_tetramino('Z')),
                           'S': (lambda: myGame.set_active_tetramino('S')),
                           'J': (lambda: myGame.set_active_tetramino('J')),
                           'L': (lambda: myGame.set_active_tetramino('L')),
                           'T': (lambda: myGame.set_active_tetramino('T'))}

    while True:
        for choice in raw_input().split(' '):
            execute_instruction[choice]()
