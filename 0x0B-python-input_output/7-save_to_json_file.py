#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    from json import dumps as d
    with open(filename, mode='w') as f:
        f.write(d(my_obj))
