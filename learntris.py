#!/usr/bin/python

import sys

# MATRIX: a list of strings where each string represents one row
MATRIX = ['.'*10 for row in range(22)]

def print_matrix():
    for row in MATRIX:
        print(' '.join(row))

if __name__ == '__main__':
    choice = raw_input()
    if choice == 'q':
        sys.exit()
    elif choice == 'p':
        print_matrix()
