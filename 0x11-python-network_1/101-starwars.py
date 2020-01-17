#!/usr/bin/python3
""" Takes in a string and sends a search request to the Star Wars API
    Handles pagination
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://swapi.co/api/people/",
                     params={'search': argv[1]})
    data = r.json()
    print("Number of results: {}".format(data.get("count")))
    for results in data.get("results"):
        print(results.get("name"))

    while data.get("next") is not None:
        url = data.get("next")
        r = requests.get(url)
        data = r.json()
        for results in data.get("results"):
            print(results.get("name"))
