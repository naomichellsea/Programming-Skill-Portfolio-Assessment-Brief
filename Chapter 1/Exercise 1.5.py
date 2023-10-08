#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:39:24 2023

@author: naomichellsea
"""

"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi #import pi from math module
r = float(input("Input the radius of the circle:"))
print("The area of the circle", pi * r**2)