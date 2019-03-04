#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

root = doc.getroot()
print(root, root.tag)

ip = root.find("innerplanets")
if len(ip):
    for planet in ip.findall('planet'):
        print(planet.get('planetname'))
        for moon in planet.findall('moon'):
            print(f'\t{moon.text}')
print('-' * 60)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f'\t{moon.text}')
