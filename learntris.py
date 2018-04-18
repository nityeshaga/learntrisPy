#!/usr/bin/python

import sys

if __name__ == '__main__':
    choice = raw_input()
    if choice == 'q':
        sys.exit()
    elif choice == 'p':
        print_matrix()
