
import random

my_num = random.randrange(1,101)
guess = my_num/2
print(my_num)
while guess != my_num:
  guess = int(input("Enter guess: "))
  if guess < my_num:
    print ("too low")
  else:
    print ("too high")
  print ("try again")
print ("congradulations you got it")