#!/usr/bin/python

from __future__ import print_function
import sys

N_ROWS = 22
N_COLUMNS = 10

# PLAY_AREA: a list of strings where each string represents one row
PLAY_AREA = ['.'*N_COLUMNS for row in range(N_ROWS)]

SCORE = 0

N_LINES_CLEARED = 0

def print_matrix():
    for row in PLAY_AREA:
        print(' '.join(row))

def read_matrix():
    for rnum in range(22):
        line = raw_input()
        new_row = line.replace(' ', '')
        PLAY_AREA[rnum] = new_row

def clear_matrix():
    global PLAY_AREA
    PLAY_AREA = ['.'*N_COLUMNS for row in range(N_ROWS)]

def display_score():
    print(SCORE)

def display_n_lines_cleared():
    print(N_LINES_CLEARED)

def one_step():
    global N_LINES_CLEARED, SCORE
    for rnum, row in enumerate(PLAY_AREA):
        if not '.' in row:
            PLAY_AREA[rnum] = '.'*N_COLUMNS
            N_LINES_CLEARED += 1
            SCORE += 100


execute_instruction = {'q': sys.exit, 
                       'p': print_matrix,
                       'g': read_matrix,
                       'c': clear_matrix,
                       '?s': display_score,
                       '?n': display_n_lines_cleared,
                       's': one_step}

if __name__ == '__main__':
    while True:
        choice = raw_input()
        execute_instruction[choice]()
