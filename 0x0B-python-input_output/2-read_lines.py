#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    x = 0
    y = 0
    with open(filename) as f:
        for line in f:
            x += 1
    if nb_lines <= 0 or nb_lines >= x:
        with open(filename) as f:
            for line in f:
                print(line, end="")
    else:
        with open(filename) as f:
            for line in f:
                while y < nb_lines:
                    print(line, end="")
                    y += 1
