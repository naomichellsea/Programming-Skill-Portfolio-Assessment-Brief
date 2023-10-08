#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:35:44 2023

@author: naomichellsea
"""

"""
Write a Python program to display the current date and time.
"""

import datetime #import the datetime
now = datetime.datetime.now()
print ("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S")) #it will print the formatted date and time

