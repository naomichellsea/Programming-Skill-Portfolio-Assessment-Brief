#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:27:50 2023

@author: naomichellsea
"""
"""
Write a loop that prompts the user to enter a series of pizza toppings until 

they enter a 'quit' value. As they enter each topping, print a message saying 

you’ll add that topping to their pizza.
"""

pizza = [] #empty list to store the toppings.

while True:
    pizza_topping = input("Please enter a pizza topping ('Quit' to finish):")
    
    if pizza_topping.lower() == 'quit':
        break  #loop will stop if user enters "quit".
    
    print(pizza_topping + " will be added to your pizza.")
    pizza.append(pizza_topping) #print a message saying you’ll add that topping to their pizza.

print("Your pizza with the toppings listed below is ready:")
for pizza in pizza:
    print("- " + pizza)