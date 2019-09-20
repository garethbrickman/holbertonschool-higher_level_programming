#!/usr/bin/python3
def simple_delete(ad, key=""):
    if key in ad:
        del ad[key]
        return ad
    else:
        return ad
