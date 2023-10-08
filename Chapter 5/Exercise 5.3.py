#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 20:57:31 2023

@author: naomichellsea
"""

"""
Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

#dictionary of glossary
glossary = {
    "Variable": "Memory for storing data values.",
    "Assignment Operator": "Type of operator used to assign values to variables.",
    "Boolean": "Data type representing 'true' or 'false'.",
    "Bitwise Operator": "It is a type of operator used to perform bitwise calculations on integers.",
    "Loop": "A control structure that repeats a block of code multiple times.",
    "List": "A collection of items.",
    "Module": "A file that has Python code.",
    "String" : "A series of text used in coding.",
    "Dictionary": "A collection of key-value pairs.",
    "Function": "block of code that performs a specific task.",
   
}

# loop through dictionary and will print each.
for term, definition in glossary.items():
    print(term + ": " + definition)