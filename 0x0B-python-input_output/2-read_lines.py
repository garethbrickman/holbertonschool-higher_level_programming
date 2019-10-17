#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    x = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            x += 1
    if nb_lines <= 0 or nb_lines >= x:
        with open(filename, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line, end="")
    else:
        with open(filename, mode='r', encoding='utf-8') as f:
            for line_no, line in enumerate(f):
                if line_no == nb_lines:
                    break
                print(line, end="")
