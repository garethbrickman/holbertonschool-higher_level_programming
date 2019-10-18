#!/usr/bin/python3
import json
from sys import argv
list1 = []
filename = "add_item.json"

try:
    with open(filename, mode='r', encoding='utf-8') as f:
        list1 = json.load(f)
except:
    pass
finally:
    list1.extend(argv[1:])
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(list1, f)
