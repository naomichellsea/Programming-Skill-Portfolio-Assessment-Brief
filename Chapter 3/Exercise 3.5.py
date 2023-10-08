#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:30:10 2023

@author: naomichellsea
"""

"""
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
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