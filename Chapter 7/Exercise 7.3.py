#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:04:10 2023

@author: naomichellsea
"""

"""
Write a function called make_shirt() that accepts a size and the text of a 

message that should be printed on the shirt. The function should print a 

sentence summarizing the size of the shirt and the message printed on it. 

Call the function once using positional arguments to make a shirt. Call the 

function a second time using keyword arguments.
"""

def make_shirt(size, text):
    print("I am going to manufacture a " + size + " shirt. ") #print the size of shirt
    print("that has a message of " + text + '"') #print the message of shirt
make_shirt('medium', 'I like you. ')
make_shirt(size= 'large', text = 'I miss you.' )
   