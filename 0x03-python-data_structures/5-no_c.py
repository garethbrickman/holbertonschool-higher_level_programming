#!/usr/bin/python3
def no_c(my_string):
    chars = {ord('c'): None, ord('C'): None}
    new = my_string.translate(chars)
    return new
