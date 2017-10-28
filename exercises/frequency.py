"""Write a function called histogram. It should take a string, and return a dict that maps each letter 
in that string, to the frequency with which it occurs in that string.
Eg:
>>> histogram("joanita gomez")
should return a dict that looks like this:

>>> {'a': 2, ' ': 1, 'e': 1, 'g': 1, 'i': 1, 'j': 1, 'm': 1, 'o': 2, 'n': 1, 't': 1, 'z': 1}"""

from sys import argv

def histogram(sentence):
	dict = {}	
	words = sentence.split()
	for word in words:
		
		if dict.has_key(word):
			dict[word] = dict[word] + 1
		else: 
			dict[word] = 1		
	return dict
	
file = open(argv[1]).read()	
print histogram(file)	

