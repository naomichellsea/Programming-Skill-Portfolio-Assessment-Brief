#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 01:44:11 2023

@author: naomichellsea
"""

"""
Make a list called sandwich_orders and fill it with the names of various 

sandwiches. Then make an empty list called finished_sandwiches. Loop through 

the list of sandwich orders and print a message for each order, such as I made 

your tuna sandwich. As each sandwich is made, move it to the list of finished 

sandwiches. After all the sandwiches have been made, print a message listing 

each sandwich that was made.
"""

sandwich_orders = ["grilled cheese","egg sandwich","ham sandwich"]
finished_sandwiches = [] #empty list to store the sandwiches

while sandwich_orders: #loop for sandwich orders list
    sandwich = sandwich_orders.pop() #enters and remove the last sandwich order
    print("I brought you this " + sandwich + ".")
    finished_sandwiches.append(sandwich) #adds the sandwich to finished sandwiches

for orders in finished_sandwiches:
    print("I made this " + orders +"," + " I hope you like it.")
    
    
    