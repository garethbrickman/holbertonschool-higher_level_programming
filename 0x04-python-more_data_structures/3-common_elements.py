#!/usr/bin/python3
def common_elements(s1, s2):
    for x in s1:
        for y in s2:
            if x == y:
                return x
