#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 02:02:34 2023

@author: naomichellsea
"""

"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 

'pastrami' appears in the list at least three times. Add code near the 

beginning of your program to print a message saying the deli has run out of 

pastrami, and then use a while loop to remove all occurrences of 'pastrami' 

from sandwich_orders. Make sure no pastrami sandwiches end up in 

finished_sandwiches.
"""

sandwich_orders = ["grilled cheese","pastrami","egg sandwich","pastrami","ham sandwich","pastrami"]
finished_sandwiches = [] #empty list to store the sandwiches

print("Sorry, we have run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")#remove all the pastrami from list

while sandwich_orders:
    orders = sandwich_orders.pop() #get and remove the last sandwich order
    print("We have alternative sandwiches such as " + orders + ".")
    finished_sandwiches.append(orders)
    
for sandwiches in finished_sandwiches:
    print("I made this " + sandwiches +"," + " I hope you like it.")