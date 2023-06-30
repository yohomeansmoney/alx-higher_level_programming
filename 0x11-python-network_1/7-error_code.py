#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
