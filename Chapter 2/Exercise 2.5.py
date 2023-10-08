#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 01:31:32 2023

@author: naomichellsea
"""

"""
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""

usb = 6
budget = 50

_bought = (budget//usb) #calculate the number of usb sticks that can be bought

_remaining = (budget % usb) #calculate the remaining budget 

print('she can buy', _bought, 'usb sticks.')
print('she will have £', _remaining, 'left.')