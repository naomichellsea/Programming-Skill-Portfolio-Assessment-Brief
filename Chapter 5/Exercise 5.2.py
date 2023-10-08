#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 01:04:47 2023

@author: naomichellsea
"""

"""
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.    
"""
glossary={ #glossary dictionary
    "first":"Variable: Memory for storing data values.",
    "second":"Assignment Operator: Type of operator used to assign values to variables.",
    "third":"Boolean: Data type representing 'true' or 'false'. ",
    "fourth":"Bitwise Operator: It is a type of operator used to perform bitwise calculations on integers.",
    "fifth":"Loop: A control structure that repeat a block of code multiple times."
    }
#print each terms from glossary
print(glossary["first"])
print(glossary["second"])
print(glossary["third"])
print(glossary["fourth"])
print(glossary["fifth"])
