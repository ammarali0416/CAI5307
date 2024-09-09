"""This is a sample file for hw1. 
It contains the function that should be submitted,
except all it does is output a random value out of the
possible values that are allowed.
- Dr. Licato"""

import random


def problem1(NPs, s):
	hypernyms = set()
	for i in range(len(NPs)-1):
		hypernyms.add( (NPs[i], NPs[i+1]) )
	return hypernyms


def problem2(s1, s2):
	return random.randint(0, abs(len(s1) - len(s2)))