#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:24:37 2023

@author: naomichellsea
"""

"""
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""

locations = ['Zurich','Tokyo','Siargao','Amsterdam', 'Barcelona'] #list of locations

print("Original Order:")
print (locations)
print("Alphabetical:")
print(sorted(locations))
print("\nOriginal Order:")
print (locations)
print ("Reverse Alphabetical:")
print(sorted(locations, reverse=True))
print("\nOriginal Order:")
print(locations)
print("Reversed:")
locations.reverse()
print(locations)
print("\nOriginal Order:")
locations.reverse()
print(locations)
print("\nAlphabetical:")
locations.sort()
print(locations)
print("\nReverse Alphabetical:")
locations.sort(reverse=True)
print(locations)