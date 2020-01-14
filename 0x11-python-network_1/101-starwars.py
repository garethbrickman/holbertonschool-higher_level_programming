#!/usr/bin/python3
""" Takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    r = requests.get(url)
    data = r.json()
    print("Number of results: {}".format(data.get("count")))
    for results in data.get("results"):
        print(results.get("name"))
