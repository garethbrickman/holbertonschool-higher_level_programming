#!/usr/bin/python3
def append_write(filename="", text=""):
    f = open(filename, mode='a', encoding='utf-8')
    f.write(text)
    x = f.seek(0, 2)
    f.close()
    return x
