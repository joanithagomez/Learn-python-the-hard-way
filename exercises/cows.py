from cows_lib import *

word = pick_word()
guess = ''
guess_count = 0
while guess != word and guess_count < 15:
	guess = raw_input("Make a guess: (%d left)" % (15 - guess_count))
	if not guess_check(guess):
		print "Invalid guess"
		continue
		
	print "%dBull(s) %dCow(s)" % (bulls(word, guess), cows(word, guess))
	
	if guess == word:
		break
	else:
		guess_count += 1

	
if guess_count == 15:
	print "Better luck next time. The word was %s" % word
else:
	print "Good job!"
	
