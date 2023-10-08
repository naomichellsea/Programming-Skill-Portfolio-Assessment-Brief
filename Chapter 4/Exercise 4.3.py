#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:50:13 2023

@author: naomichellsea
"""
"""
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color = "red" #color of the alien
if alien_color == "green": #if elif else chain
    print ("You just earned 5 points!")
elif alien_color == "yellow":
    print ("You just earned 10 points!")
else:
    print ("You just earned 15 points!")
    
    