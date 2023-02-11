# fruits = ["apple", "Orange", "pear"]
# for i in fruits:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

#####

# Day 5 Project: Password generator

import random

lowercaseLetters = [chr(i) for i in range(97, 123)]
uppercaseLetters = [chr(i) for i in range(65, 91)]
allAlphabets = lowercaseLetters + uppercaseLetters

symbols = ["!", "@", "#", "%", "^", "&", "*", "=", "+", "_", "-", "/", "?"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like in your password?\n"))
numNumbers = int(input("How many numbers would you like in your password?\n"))

shuffledRandomList = random.choices(allAlphabets, k=numLetters) + random.choices(symbols, k=numSymbols) 
+ random.choices(numbers, k=numNumbers)
random.shuffle(shuffledRandomList)

print(f"Here is your password: {''.join(str(i) for i in shuffledRandomList)}")

