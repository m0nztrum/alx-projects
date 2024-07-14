#!/usr/bin/python3
"""script that sends a POST request with a letter as
a parameter"""
from sys import argv

import requests

if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    try:
        req = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={"q": letter},
        )
        if req.json() == {}:
            print("No result")
        else:
            print(f"[{req.json()['id']}] {req.json()['name']}")
    except Exception:
        print("Not a valid JSON")
