#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for x in sorted(a_dictionary):
        print("{}: {}".format(x, a_dictionary[x]))
