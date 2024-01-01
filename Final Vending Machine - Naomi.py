#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:10:32 2023

@author: naomichellsea
"""
"""
The Vending Machine must have the following features as a minimum requirement:

●       A menu of drinks and snacks presented via the console. The number and range of items is up to you.

●       A set of codes that the user can input to select a particular drink or snack.

●        A way of capturing the user’s inputted code.

●       A way of managing money. The user should be able to input any amount of money and have the correct change returned.

●       A message that tells the user that a particular drink or snack has been dispensed.

●        A message that tells the user how much change they have received.

●        Comments in the code to explain key operations.

You may wish to add additional features to your Vending Machine to achieve higher marks. Below is an indication of some of these features, however you may also wish to come up with your own:

●       A method of categorising items in the vending machine to improve the user experience (e.g. ‘Chocolate’ or ‘Hot Drinks’).

●       A way of allowing users to buy additional items.

●       An intelligence system for suggesting purchases. For example, if you buy a coffee, the vending machine may suggest that you buy biscuits.

●       The use of functions to improve the structure of your program.

●       A stock system meaning the machine may run out of products
"""

import time
import datetime

# Initial stock of items
_stocks_ = [
    {"name": "Hershey's", 'price': 20, 'quantity': 10, "id": 0},
    {"name": "Kisses",  'price': 15, 'quantity': 5, "id": 1},
    {"name": "Reese", 'price': 35, 'quantity': 12, "id": 2},
    {"name": "Maltesers",  'price': 20, 'quantity': 11, "id": 3},
    {"name": "Kitkat",'price': 25, 'quantity': 1, "id": 4},
    {"name": "Sun Chips",'price': 35, 'quantity': 3, "id": 5},
    {"name": "Tacos", 'price': 20, 'quantity': 10, "id": 6},
    {"name": "Doritos", 'price': 30, 'quantity': 15, "id": 7},
    {"name": "Cheetos", 'price': 30, 'quantity': 9, "id": 8},
    {"name": "Takis", 'price': 35, 'quantity': 8, "id": 9},
    {"name": "Pop-Tarts",  'price': 25, 'quantity': 14, "id": 10},
    {"name": "Granola Bar",  'price': 30, 'quantity': 9, "id": 11},
    {"name": "Peanuts",  'price': 15, 'quantity': 13, "id": 12},
    {"name": "Gatorade", 'price': 25, 'quantity': 4, "id": 13},
    {"name": "Pepsi", 'price': 10, 'quantity': 10, "id": 14},
    {"name": "Sprite",  'price': 10, 'quantity': 8, "id": 15},
    {"name": "Water", 'price': 10, 'quantity': 6, "id": 16},
    {"name": "Pocari", 'price': 20, 'quantity': 7, "id": 17},
    {"name": "Cold Coffee",  'price': 25, 'quantity': 6, "id": 18},
    {"name": "Apple Juice",  'price': 35, 'quantity': 9, "id": 19},
    {"name": "Peach Iced Tea", 'price': 30, 'quantity': 10, "id": 20},
]


# Lists to store transaction history and selected items
everything = []
th = []  # transaction history
thebill = """
\t\t** PRODUCT <~~> PRICE **
"""

def goods(_stocks_, everything):
    print("  <<<<<<<<  Welcome to Naomi's Vending Machine  >>>>>>>>  ")
    time.sleep(1)

    play = True
    tp = 0  # total price

    while play:
        print("\n   ~~~~~~~~~~   The Items In Stock Are   ~~~~~~~~~~   \n")
        time.sleep(0.5)

        for i in _stocks_:
            print("Item ID: {} ||| Item: {} ||| Price: {} ||| Quantity: {}".format(i['id'], i['name'], i['price'], i['quantity']))
            if i['quantity'] <= 5:  # Notify when quantity is less than or equal to 5
                print("ALERT: Low inventory for item {}! Quantity: {}".format(i['name'], i['quantity']))

        try:
            purchase = int(input("\nEnter the item ID of the product you want to buy: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= purchase < len(_stocks_) and _stocks_[purchase]['quantity'] > 0:
            everything.append(_stocks_[purchase])
            tp += _stocks_[purchase]['price']
            _stocks_[purchase]['quantity'] -= 1
            print("You have ordered {} for ${}.".format(_stocks_[purchase]['name'], _stocks_[purchase]['price']))
            th.append({
                "item_name": _stocks_[purchase]['name'],
                "item_price": _stocks_[purchase]['price'],
                "timestamp": datetime.datetime.now()
            })
        else:
            print("Invalid product ID or out of stock!")

        while True:
            adding = input("Would you like to add more items? \nPress 'a' to add, or 'q' to quit: ")
            if adding.lower() == "a" or adding.lower() == "q":
                break
            else:
                print("Invalid input. Please enter 'a' or 'q'.")

        if adding.lower() == "q":
            play = False

    billout = int(input("1. Print the receipt? 2. Only print the total sum: "))
    if billout == 1:
        print(_make(everything, thebill, th))

        while tp > 0:
            cash = float(input("Enter the amount you paid: "))
            if cash < 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                tp -= cash
                if tp > 0:
                    print("Remaining amount: {:.2f}".format(tp))
                elif tp == 0:
                    print("Payment completed. Thank you for purchasing with us!")
                else:
                    coins = abs(tp)
                    print("Change: {:.2f}".format(coins))
                    print("Thank you for purchasing with us!")

    elif billout == 2:
        print("Total cost: {:.2f}".format(tp))
        while tp > 0:
            cash = float(input("Enter the amount you paid: "))
            if cash < 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                tp -= cash
                if tp > 0:
                    print("Remaining amount: {:.2f}".format(tp))
                elif tp == 0:
                    print("Payment completed. Thank you for purchasing with us!")
                else:
                    coins = abs(tp)
                    print("Change: {:.2f}".format(coins))
                    print("Thank you for purchasing with us!")

# Function to create a receipt with details of the selected items, including timestamps, and the total sum.
def _make(everything, thebill, th):
    for item, transaction in zip(everything, th):
        timestamp_formatted = transaction["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        thebill += "\n\t{} -- {} -- {}".format(item["name"], item["price"], timestamp_formatted)

    thebill += "\n\tTotal --- {:.2f}\n".format(sum(item["price"] for item in everything))
    return thebill

# Entry point to run the vending machine simulation.
if __name__ == "__main__":
    goods(_stocks_, everything)

 

