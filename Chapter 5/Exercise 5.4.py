#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:39:53 2023

@author: naomichellsea
"""

"""
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""
rivers = {
        "Nile river": "Egypt",
        "Mackenzie river": "Canada",
        "Volga river": "Russia",
       }
for river, country in rivers.items():
     print(" The " + river + " that runs through " + country + ".")
     
#loop to print the name of each river 
print("\nList of rivers:")
for river in rivers.items():
    print(river)
    
#loop to print the name of each country 
print("\nList of countries:")
for country in rivers.values():
    print(country)