#!/usr/bin/python3
def common_elements(s1, s2):
    if (s1 & s2):
        return (s1 & s2)
    else:
        return None
