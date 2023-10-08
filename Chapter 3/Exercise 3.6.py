#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:59:46 2023

@author: naomichellsea
"""

"""
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    
"""

guests = ["Mochi", "Yuki", "Omi"]
name = guests[0].title()
print(name + ", can you come to dinner please?")
name = guests[1].title()
print(name + ", can you come to dinner please?")
name = guests[2].title()
print(name + ", can you come to dinner please?")

name = guests[0].title()
print("\nSorry, " + name + " can not make it to dinner.")

#exchange Nathan with Mochi
del(guests[0])
guests.insert(0, 'Nathan')

#Final invitation
name = guests[0].title()
print("\n" + name + ", can you please come to dinner.")

name = guests[1].title()
print(name + ", can you please come to dinner.")

name = guests[2].title()
print(name + ", can you please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("\nSorry, " + name.title() + " there is no room at the table.")

# 2 invitations for 2 people 
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")

# Empty list
del(guests[0])
del(guests[0])

# Prove the list is empty
print(guests)





