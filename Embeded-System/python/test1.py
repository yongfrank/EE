'''
Author: Frank Chu
Date: 2022-11-01 10:22:49
LastEditors: Frank Chu
LastEditTime: 2022-12-06 00:47:15
FilePath: /EE/Embeded-System/python/test1.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
from random import randint, random

def play():
    # Return random integer in range [a, b], 
    # including both end points.
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("What number did we guess (0-100)?"))

        if user_guess == random_int:
            print(f"You found the number ({random_int}). Congrats!")
            break

        if user_guess < random_int:
            print("Your number is less than the number")
            continue

        if user_guess > random_int:
            print("Your number is more than the number")

if __name__ == '__main__':
    play()
    
