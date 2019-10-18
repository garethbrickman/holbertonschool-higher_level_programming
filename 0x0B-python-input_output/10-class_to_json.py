#!/usr/bin/python3
def class_to_json(obj):
    import json
    x = json.dumps(obj.__dict__)
    return x
