#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL 
with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if len(sys.argv) < 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email data
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')  # Convert to bytes

req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    # Decoding and displaying the body of the response
    body = response.read().decode('utf-8')
    print(body)
