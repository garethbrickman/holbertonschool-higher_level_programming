#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        f = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return None
    return f
