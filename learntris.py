#!/usr/bin/python

from __future__ import print_function
import sys

# PLAY_AREA: a list of strings where each string represents one row
PLAY_AREA = ['.'*10 for row in range(22)]

def print_matrix():
    for row in PLAY_AREA:
        print(' '.join(row))

def read_matrix():
    for rnum in range(22):
        line = raw_input()
        new_row = line.replace(' ', '')
        PLAY_AREA[rnum] = new_row

execute_instruction = {'q': sys.exit, 
                       'p': print_matrix,
                       'g': read_matrix}

if __name__ == '__main__':
    while True:
        choice = raw_input()
        execute_instruction[choice]()
