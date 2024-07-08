#!/usr/bin/python3
#sends a request to the URL and displays the body of the response

import urllib.request
import urllib.error
import sys


if len(sys.argv) < 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Decoding and displaying the body of the response
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.HTTPError as e:
    # Handling HTTPError exceptions and printing the error code
    print(f"Error code: {e.code}")
