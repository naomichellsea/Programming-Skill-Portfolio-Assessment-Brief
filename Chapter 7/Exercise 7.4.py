#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 01:19:25 2023

@author: naomichellsea
"""

"""
Modify the make_shirt() function so that shirts are large by default with a 

message that reads I love Python. Make a large shirt and a medium shirt with 

the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="large", text = "I love Python"):
    print("\nI am going to manufacture a " + size + " shirt. ") #print size of shirt
    print("that has a message of " + text + ".") #print message of shirt

make_shirt()
make_shirt(size = "small")
make_shirt("medium", "I love you")
    