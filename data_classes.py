#!/usr/bin/env python
from dataclasses import dataclass, field
from datetime import date

@dataclass # (frozen=True)
class President():

    first_name: str
    last_name: str
    birthdate: date


p = President(first_name='George', last_name='Washington', birthdate=date(1723, 2, 22))

print(p)

print(p.first_name)

print(type(p))

p.first_name = 'Fred'

print(p)
