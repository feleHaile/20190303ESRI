#!/usr/bin/env python
import lxml.etree as ET
# import xml.etree.ElementTree as ET

data = [
    ['Arizona', 'Phoenix'],
    ['California', 'Sacramento'],
    ['Oregon', 'Salem'],
    ['North Carolina', 'Raleigh'],
    ['Montana', 'Helena'],
]

root = ET.Element("states")

for state_name, capital_name in data:
    state = ET.SubElement(root, 'state', name=state_name)
    # capital = ET.SubElement(state, 'capital')
    # capital.text = capital_name
    ET.SubElement(state, 'capital').text = capital_name

print(ET.tostring(root).decode())


