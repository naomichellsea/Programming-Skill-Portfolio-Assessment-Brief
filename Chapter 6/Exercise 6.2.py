#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:57:31 2023

@author: naomichellsea
"""

"""
A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""

a = "Please enter your age:"
a += "\nPlease enter 'Done' when you are finished." #+ sign to add in the first variable

while True:
    b = input(a)
    if b == "Done": #break the loop
        break
    c = int(b) #to turn the age input into an integer
  
    
    if c < 3:
      print("Your ticket is free!") #print the price of ticket
    elif c>=3 and c<=12:
      print("Your ticket will cost you $10.")
    else:
      print("Your ticket will cost you $15.")