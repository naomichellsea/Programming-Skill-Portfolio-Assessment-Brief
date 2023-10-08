#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 01:45:45 2023

@author: naomichellsea
"""

"""
Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list 
and as you do, print everything you know about each pet
"""


pets =[] #empty list
a_pet = { #dictionary of pets
     "animal type" : "dog",
     "name" : "mochi",
     "owner" : "naomi",
     "eats" : "bones",
     }
pets.append(a_pet)

b_pet = { #second dictionary
       "animal type" : "cat",
       "name": "Yuki",
       "owner" : "Noeme",
       "eats" : "meat",
       }
pets.append(b_pet)

c_pet = { #third dictionary
       "animal type":"bird",
       "name":"Felix",
       "owner":"Louie",
       "eats":"seeds",
       }
pets.append(c_pet)
print(pets)
for pet in pets:
    print("\nThis is everything i know about " + pet["name"].title()+":")
    for key,value in pet.items():
        print("\t"+key+":"+str(value))