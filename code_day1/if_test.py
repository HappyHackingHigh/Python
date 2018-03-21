#!/usr/bin/python
# -*- coding: UTF-8 -*-

number = 2315698

guess = int(raw_input('Enter an integer : '))

if guess == number:
  print 'Congratulations, you guessed it.' # New block starts here
  print "(This is flag: BreakALL{It is easy to write if statement}!)" # New block ends here
elif guess < number:
  print 'No, it is a little higher than that' 
  # You can do whatever you want in a block ...
else:
  print 'No, it is a little lower than that' 
# you must have guess > number to reach here

print 'Done'

# This last statement is always executed, after the if statement is executed