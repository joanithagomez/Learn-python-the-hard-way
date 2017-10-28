import random


def pick_word():
	"""
		Pick a word to challenge the player with.
	"""
	# read new_words.txt
	# return a random word from that file
	
	
	file = open("new_words.txt")
	
	return random.choice([x.rstrip() for x in file])
	
def guess_check(guess):
	if len(guess) != 4:
		return False
	else:
		return True

			  
	
		
def bulls(word, guess):
	counter = 0
	for index in range(0,4):
		if word[index] == guess[index]:
			counter += 1
	return counter		

#make
#mean

	
# TODO: Use enumerate below to simplify
# TODO: confirm the abba vs adef, 1B/1C situation
def cows(word, guess):			
	counter = 0
	word_pos = 0
	guess_pos = 0
	for letter in word:	     
		for character in guess:
			if letter == character and word.index(letter) != guess.index(character):
				counter += 1
			guess_pos += 1
		word_pos +=1 
	return counter
	 
		
