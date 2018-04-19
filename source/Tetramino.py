from helper import print_matrix

TETRAMINO_DICT = {'I': ['....', 'cccc', '....', '....'],
                  'O': ['yy', 'yy'],
                  'Z': ['rr.', '.rr', '...'],
                  'S': ['.gg', 'gg.', '...'],
                  'J': ['b..', 'bbb', '...'],
                  'L': ['..o', 'ooo', '...'],
                  'T': ['.m.', 'mmm', '...']}

class Tetramino:
    def __init__(self, shape):
        self.tetramino_matrix = TETRAMINO_DICT[shape]

    def show(self):
        print_matrix(self.tetramino_matrix)
 
    def rotate_cw(self):
        self.tetramino_matrix = zip(*(self.tetramino_matrix[::-1]))
