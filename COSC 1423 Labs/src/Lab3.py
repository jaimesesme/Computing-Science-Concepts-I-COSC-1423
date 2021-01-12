# Lab #3
# Ruvi Jaimes

# This program gives the individual bill amount w
# when it is split between people (it includes the tip amount)

import random

def main():
    welcome_message()
    tables_num = random.randint(1,25) 
    total_tip = 0
    for i in range (tables_num):
    
        tip = user_inputs()
        total_tip += tip
        print("total tip is:",total_tip)

# print message 
def welcome_message():
    print("Hello ")
    print("This program allows the bill to be split between people,") 
    print("suggests the tip amount for a bill, and gives the total tips.")

# inputs: total bill amount, the tip percentage and 
# the number of people splitting the bill
# outputs: amount each person will pay and the total tip    
def user_inputs():
    print("\n")
    initial_bill = float(input("Enter the total bill amount: "))
    
    ten = .1*(initial_bill)
    fifteen = .15*(initial_bill)
    twenty = .2*(initial_bill)
    
    # tips 
    tip_choice= int(input(""" 
                            1. 10%
                            2. 15%
                            3. 20%
    
    """))
    
    if tip_choice == 1:
        tip = ten 
    elif tip_choice == 2:
        tip = fifteen
    elif tip_choice == 3:
        tip = twenty    
    
    # number of people splitting the bill 
    num_ppl = int(input("Enter total number of people splitting the bill: "))
    
    # calculations 
    total_bill = initial_bill + tip 
    split_bill = total_bill/num_ppl
    # rounds to two decimals 
    split_bill = str(round(split_bill, 2))
    
    print("\n")
    print("Each person's share, including tip is", split_bill)
    return tip 
    
main()
