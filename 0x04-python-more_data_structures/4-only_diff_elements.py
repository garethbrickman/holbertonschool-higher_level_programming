#!/usr/bin/python3
def only_diff_elements(s1, s2):
    same1 = s1-s2
    same2 = s2-s1
    same3 = same1 | same2
    return same3
