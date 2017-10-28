# cat /usr/share/dict/words | python words.py
# reads input line by line
# print out the words that begin with a small letter and have 4 letters in them

import sys 

file = sys.stdin 

word = file.readline()

while word != '':

	if len(word) == 4 and word[0].islower() and word[3] != 's':		
		print word
	word = file.readline().rstrip()
