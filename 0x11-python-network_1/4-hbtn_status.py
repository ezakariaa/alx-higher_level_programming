#!/usr/bin/python3
#script that fetches https://alx-intranet.hbtn.io/status

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(response.text)))
    print('\t- content: {_content}'.format(_content=response.text))
else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
