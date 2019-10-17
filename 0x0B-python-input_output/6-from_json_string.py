#!/usr/bin/python3
def from_json_string(my_str):
    from json import loads as d
    return d(my_str)
