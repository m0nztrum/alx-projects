#!/usr/bin/python3
"""Script that sends a request and displays the body of the response"""
from sys import argv

import requests

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print(f"Error code: {req.status_code}")
