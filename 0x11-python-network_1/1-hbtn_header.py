#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL


from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(f"{html}")
