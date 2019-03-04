#!/usr/bin/env python
import urllib.request

ESRI_URL = "https://www.python.org"

response = urllib.request.urlopen(ESRI_URL)

print(response.info())

content = response.read().decode()

print(content)
