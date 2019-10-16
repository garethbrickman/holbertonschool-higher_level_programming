#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    with open(filename) as f:
        x = f.read()
        x = f.tell()
        return x
