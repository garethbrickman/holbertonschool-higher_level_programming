#!/usr/bin/python3
""" Fetches website info using urllib library
"""
if __name__ == "__main__":
    from urllib import request
    print("Body response:")
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("\t- type: {}".format(type(response.read().decode())))
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("\t- content: {}".format(response.read().decode()))
