#!/usr/bin/python

from __future__ import print_function
import sys

# MATRIX: a list of strings where each string represents one row
MATRIX = ['.'*10 for row in range(22)]

def print_matrix():
    for row in MATRIX:
        print(' '.join(row))

def read_matrix():
    for rnum in range(22):
        line = raw_input()
        new_row = line.replace(' ', '')
        MATRIX[rnum] = new_row

execute_instruction = {'q': sys.exit, 
                       'p': print_matrix,
                       'g': read_matrix}

if __name__ == '__main__':
    while True:
        choice = raw_input()
        execute_instruction[choice]()
