from __future__ import print_function
from copy import deepcopy

from Tetramino import Tetramino
from helper import print_matrix

class Game:
    def __init__(self):
        self.N_ROWS = 22
        self.N_COLUMNS = 10

        # PLAY_AREA: a list of strings where each string represents one row
        self.PLAY_AREA = [list('.' * self.N_COLUMNS) for row in range(self.N_ROWS)]

        self.temp_PLAY_AREA = None
        
        self.SCORE = 0
        self.N_LINES_CLEARED = 0
        self.active_tetramino = Tetramino('I') # default value -- the I tetramino
        self._active_tetramino_rnum = None
        self._active_tetramino_cnum = None

    def _set_active_tetramino_position(self, rnum=0, cnum=0):
        '''
        Changes the position of active tetramino if possible.
        :param rnum:
            The row index of the new position of the active tetramino
        :param cnum:
            The column index of the new position of the active tetramino
        '''
        self._active_tetramino_cnum = cnum
        self._active_tetramino_rnum = rnum

    def read_play_area(self):
        for rnum in range(22):
            line = raw_input()
            new_row = line.replace(' ', '')
            self.PLAY_AREA[rnum] = new_row

    def clear_matrix(self):
        self.PLAY_AREA = [list('.' * self.N_COLUMNS) for row in range(self.N_ROWS)]

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
        self._active_tetramino_rnum = 0
        if len(self.active_tetramino.tetramino_matrix) == 2:
            self._active_tetramino_cnum = 4
        else:
            self._active_tetramino_cnum = 3

    def print_active_tetramino_on_matrix(self):
        self.spawn_active_tetramino()
        print_matrix(self.temp_PLAY_AREA)

    def spawn_active_tetramino(self):
        self.temp_PLAY_AREA = deepcopy(self.PLAY_AREA)
        active_tetramino_size = len(self.active_tetramino.tetramino_matrix)
        for row_idx in range(self._active_tetramino_rnum, 
                             self._active_tetramino_rnum+active_tetramino_size):
            self.temp_PLAY_AREA[row_idx][self._active_tetramino_cnum : 
                    self._active_tetramino_cnum+active_tetramino_size] = \
                    [ch.upper() for ch in self.active_tetramino.tetramino_matrix
                            [row_idx - self._active_tetramino_rnum][:]]

    def nudge_active_tetramino_left(self): 
        self._set_active_tetramino_position(cnum=self._active_tetramino_cnum-1,
                                            rnum=self._active_tetramino_rnum)

    def nudge_active_tetramino_right(self): 
        self._set_active_tetramino_position(cnum=self._active_tetramino_cnum+1,
                                            rnum=self._active_tetramino_rnum)

    def nudge_active_tetramino_down(self):
        self._set_active_tetramino_position(cnum=self._active_tetramino_cnum,
                                            rnum=self._active_tetramino_rnum+1)

