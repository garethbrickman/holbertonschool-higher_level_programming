#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename, mode='r', encoding='utf-8') as f:
        x = json.load(f)
        return x
