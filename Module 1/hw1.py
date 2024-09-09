"""This is a sample file for hw1. 
It contains the function that should be submitted,
except all it does is output a random value out of the
possible values that are allowed.
- Dr. Licato"""

import random
import re

def problem1(NPs, s):
	hypernyms = set()

	# "All X, such as Y and Z"
	pattern = r'All (\w+), such as (\w+) and (\w+)'

	matches = list(re.finditer(pattern, s))  # Convert iterator to list for indexing instead of yielding

	if matches:  # Ensure there is at least one match
		match = matches[0]  # Get the first match since the problem only has one match
		hypernym = match.group(1)  # All X
		hyponym1 = match.group(2)  # as Y
		hyponym2 = match.group(3)  # and Z

		hypernyms.add((hypernym, hyponym1))
		hypernyms.add((hypernym, hyponym2))

    # "Y are X,/;" where X can be one or more words 
	pattern = r'([A-Za-z]+) are ([A-Za-z]+(?: [A-Za-z]+)?)[,;]?'
	matches = list(re.finditer(pattern, s, re.IGNORECASE))  

	if matches:  
		match = matches[0]  
		hypernym = match.group(2).lower()  # are X
		hyponym = match.group(1).lower()  # Y are

		hypernyms.add((hypernym, hyponym))

	# "Some X, including Y,""
	pattern = r'Some (\w+), including (\w+),'
	matches = list(re.finditer(pattern, s, re.IGNORECASE))  

	if matches:  
		match = matches[0]  
		hypernym = match.group(1).lower()  # Some X
		hyponym = match.group(2).lower()  # including Y

		hypernyms.add((hypernym, hyponym))

	# "Y was an X"
	pattern = r'([A-Za-z]+) was an (\w+)'
	matches = list(re.finditer(pattern, s, re.IGNORECASE))  

	if matches:  
		match = matches[0]  
		hypernym = match.group(2).lower()  # was an X
		hyponym = match.group(1).lower()  # Y was an

		hypernyms.add((hypernym, hyponym))

	# "X was a Y"
	pattern = r'([A-Za-z]+) was a (\w+)'
	matches = list(re.finditer(pattern, s, re.IGNORECASE))  

	if matches:  
		match = matches[0]  
		hypernym = match.group(2).lower()  # was a X
		hyponym = match.group(1).lower()  # Y was a

		hypernyms.add((hypernym, hyponym))

	# X, such as Y and Z
	pattern = r'(\w+), such as ([A-Za-z]+(?: [A-Za-z]+)?) and ([A-Za-z]+(?: [A-Za-z]+)?)'
	matches = list(re.finditer(pattern, s))  

	if matches: 
		match = matches[0]  
		hypernym = match.group(1).lower()  # All X
		hyponym1 = match.group(2).lower()  # as Y
		hyponym2 = match.group(3).lower()  # and Z
		
		hypernyms.add((hypernym, hyponym1))
		hypernyms.add((hypernym, hyponym2))

	return hypernyms

## Helper functions for problem 2
def del_cost(c):
    return 1

def ins_cost(c):
    return 1

def sub_cost(c1, c2):
    if c1 == c2:
        return 0
    else:
        return 1

def problem2(s1, s2):
    n = len(s1)
    m = len(s2)

    # Create a distance matrix
    D = [[0] * (m + 1) for _ in range(n + 1)]

    # Init: the 0th row and column is the distance from the empty string ie 0
    D[0][0] = 0  # Top left corner of the matrix

    # First column and row increment by 1
    for i in range(1, n + 1):
        D[i][0] = D[i - 1][0] + del_cost(s1[i - 1])
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + ins_cost(s2[j - 1])

    # Fill in the rest of the matrix using the helper functions
    for i in range(1, n + 1): # Iterate over the rows
        for j in range(1, m + 1): # For each row, iterate over the columns
            D[i][j] = min(D[i - 1][j] + del_cost(s1[i - 1]), # Cost of deleting the current cell + the cell one row up
                          D[i][j - 1] + ins_cost(s2[j - 1]), # Cost of inserting the current cell + the cell one column to the left
                          D[i - 1][j - 1] + sub_cost(s1[i - 1], s2[j - 1]))  # Substitution cost + the cell one row up and one column to the left

    return D[n][m]