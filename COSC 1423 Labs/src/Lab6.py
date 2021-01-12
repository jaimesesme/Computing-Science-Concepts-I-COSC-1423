# Lab 6
# Ruvi Jaimes
# Using a dictionary, we give each player the values 
# num and wins. When the code finds the largest randomized number 
# from each player it turns the wins from a 0 to 1. 
# Prints our the winner. 

import random

# welcome message 
print("Welcome to 'Whose is the Largest?' Calculator")

# innitiating the dictionary of players 
player_dict={}

# getting number of players 
playernumber = int(input("Enter the number of players (less than 50): "))

# input the name of each player
for i in range (playernumber):
    name = input("Enter name: ")
    player_dict[name]={"num": 0, 
                       "wins": 0}

input("Press enter to generate your number...\n")

# giving each player a random number 
for name in player_dict:
    number= random.randint(1,50)
    player_dict[name]["num"] = number  
     
winner = []
win_num = 0

# find winner 
for name in player_dict.items():
    if name[1]["num"] > win_num:
        win_num = name[1]["num"]
        winner = [name[0]]
    elif name[1]["num"] == win_num:
        winner +=[name[0]]
        

# pring message       
print("The winner is: " + winner[0])
