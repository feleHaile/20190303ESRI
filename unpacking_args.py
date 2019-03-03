#!/usr/bin/env python

def locate(lat, lon):
    print("at {} {}".format(lat, lon))

locate(35.1223, 75.2322)

data = [
    (1.2, 3.4),
    (32.393, 76.3902),
    (14.8, 99.393),
]
for place in data:
    locate(*place)
