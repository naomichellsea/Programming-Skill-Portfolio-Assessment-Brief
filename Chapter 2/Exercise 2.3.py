#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 01:15:43 2023

@author: naomichellsea
"""

"""
Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

name = "\tNaomi Chellsea\n"

print("Unmodified:")
print(name) #print the unmodified string

print("\n lstrip():")
print(name.lstrip()) #print the string after left stripping

print("\n rstrip():")
print(name.rstrip()) #print the string after right stripping 

print("\n strip():")
print(name.strip())