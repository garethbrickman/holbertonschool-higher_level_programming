#!/usr/bin/python3
def best_score(ad):
    big = 0
    if ad is None:
        return None
    for i in ad:
        if ad[i] > big:
            big = ad[i]
            name = list(ad.keys())[list(ad.values()).index(big)]
    return name
