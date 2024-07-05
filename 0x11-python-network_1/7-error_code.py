#!/usr/bin/python3
#script that takes in a URL, sends a request to the URL and displays the body of the response

import sys
import requests

url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)

