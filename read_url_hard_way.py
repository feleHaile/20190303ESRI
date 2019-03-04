#!/usr/bin/env python
import requests

ESRI_URL = "https://www.python.org/q=foobar"

response = requests.get(
    ESRI_URL,
    # auth=(AUTH_ID, AUTH_TOKEN),
    # data={'food':'spam', 'animal':'wombat'},
    # params={'q':'foobar'},
    # proxy={'http':'https://myproxy.wherever.com/'},

)

if response.status_code == requests.codes.OK:

    print(response.content.decode())

    data = response.json()
