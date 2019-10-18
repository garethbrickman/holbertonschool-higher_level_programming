#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    f = open(filename, mode='r', encoding='utf-8')
    for line in f:
        if line == search_string:
            f.close()
            with open(filename, mode='a', encoding='utf-8') as f:
                f.write(new_string)
