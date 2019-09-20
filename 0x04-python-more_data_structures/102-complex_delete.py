#!/usr/bin/python3
def complex_delete(ad, value):
    if value in ad:
        del ad[value]
        return ad
    else:
        return ad
