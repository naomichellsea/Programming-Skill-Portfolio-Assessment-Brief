#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:28:12 2023

@author: naomichellsea
"""

"""
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.

"""

def describe_city(city, country="Netherlands"):
    text = city.title() + " is in " + country.title() + "." #statement for city and country
    print(text)
    
describe_city("Amsterdam")
describe_city ("Rotterdam")
describe_city ("Paris", "France")

