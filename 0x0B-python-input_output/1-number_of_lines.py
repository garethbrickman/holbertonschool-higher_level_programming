#!/usr/bin/python3
def number_of_lines(filename=""):
    x = 0
    with open(filename) as f:
        for line in f:
            x += 1
        return x
