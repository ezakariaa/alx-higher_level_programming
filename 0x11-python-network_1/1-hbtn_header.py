#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')

print(x_request_id)
