#!/usr/bin/python3
""" Sends POST request to URL with letter as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) is not 2:
        q = ""
    else:
        q = argv[1]
    post = requests.post(url, data={'q': q})
    try:
        data = post.json()
    except:
        print("Not a valid JSON")
    else:
        if data.get("id") is None:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
