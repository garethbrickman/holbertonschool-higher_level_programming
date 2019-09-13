#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    def infadd(*argv):
        total = 0
        for arg in argv:
            total += int(arg)
            print(total)
