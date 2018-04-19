#!/usr/bin/python

from __future__ import print_function
import sys

from helper import print_matrix
from Game import Game


if __name__ == '__main__':

    myGame = Game()
    execute_instruction = {'q': sys.exit, 
                           'p': (lambda: print_matrix(myGame.PLAY_AREA)),
                           'g': myGame.read_play_area,
                           'c': myGame.clear_matrix,
                           '?s': myGame.display_score,
                           '?n': myGame.display_n_lines_cleared,
                           's': myGame.one_step,
                           't': (lambda: myGame.active_tetramino.show()),
                           'I': (lambda: myGame.set_active_tetramino('I')),
                           'O': (lambda: myGame.set_active_tetramino('O')),
                           'Z': (lambda: myGame.set_active_tetramino('Z')),
                           'S': (lambda: myGame.set_active_tetramino('S')),
                           'J': (lambda: myGame.set_active_tetramino('J')),
                           'L': (lambda: myGame.set_active_tetramino('L')),
                           'T': (lambda: myGame.set_active_tetramino('T')),
                           ')': (lambda: myGame.active_tetramino.rotate_cw()),
                           ';': (lambda: print('\n', end=''))}

    while True:
        for choice in raw_input().split(' '):
            execute_instruction[choice]()
