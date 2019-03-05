#!/usr/bin/env python
from functools import wraps

# @MYDECORATOR
# def myfunction():
#     pass
#
# myfunction = MYDECORATOR(myfunction)

my_functions = []

def bark(original_function):

    @wraps(original_function)
    def new_function(*args, **kwargs):
        my_functions.append(original_function)
        print("woof! woof!")
        result = original_function(*args, **kwargs)
        return result
    return new_function

@bark
def animal(animal_type):
    print(f"I am a {animal_type}")

@bark
def vegetable(vtype):
    print(f"I am a {vtype}")

animal("wombat")
vegetable("cucumber")
animal("wombat")
vegetable("cucumber")
print(animal.__name__)
print(vegetable.__name__)
