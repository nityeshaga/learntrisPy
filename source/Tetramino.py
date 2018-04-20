from helper import print_matrix

TETRAMINO_DICT = {'I': [list(elem) for elem in ['....', 'cccc', '....', '....']],
                  'O': [list(elem) for elem in ['yy', 'yy']],
                  'Z': [list(elem) for elem in ['rr.', '.rr', '...']],
                  'S': [list(elem) for elem in ['.gg', 'gg.', '...']],
                  'J': [list(elem) for elem in ['b..', 'bbb', '...']],
                  'L': [list(elem) for elem in ['..o', 'ooo', '...']],
                  'T': [list(elem) for elem in ['.m.', 'mmm', '...']]}

class Tetramino:
    def __init__(self, shape):
        self.tetramino_matrix = TETRAMINO_DICT[shape]

    def show(self):
        print_matrix(self.tetramino_matrix)
 
    def rotate_cw(self):
        self.tetramino_matrix = zip(*(self.tetramino_matrix[::-1]))
