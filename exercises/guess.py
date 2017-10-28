# guess the number game
# python guess.py 10
# === pick a random number less than 10 as the answer
# Make a guess: 8
# "too high!"
# Make a guess: 1
# "too low!"
# Make a guess: 2
# "you got it!"
# typing in anything that's not a number should quit the program

	
import random
from sys import argv
import sys

random_num = random.randint(0,int(argv[1]))

try:
	guess = int(raw_input("Make a guess: "))
	
except ValueError:

	sys.exit() 	

while guess != random_num:

	if guess > random_num: 
		print "too high"
	else: 
		print "Too low"
		
	guess = int(raw_input("Try again: "))
		
if guess == random_num:
	print "You got it"