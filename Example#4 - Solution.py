# Example 4 - Guessing Game - Correct Solution
import random

my_num = random.randrange(1,101)
guess = int(input("Enter guess: "))

while guess != my_num:
  if guess < my_num:
    print ("too low, try again")
  else:
    print ("too high, try again")
  guess = int(input("Enter guess: "))
  
print ("congradulations you got it")