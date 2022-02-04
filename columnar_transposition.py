from collections import OrderedDict

# Print the dictionary
def print_dict(dictionary):
	# List [] notation for all of the keys of the dictionary
	keys = list(dictionary.keys())

	# Keys are just a single character of the secret phrase
	temp = ' '.join(keys[i] for i in range(len(keys)))

	print(temp)
	print('-'*len(temp))
	
	# Create a list of a strings contained at the keys
	strings = [dictionary[key] for key in keys]
	# Find the longest one by length
	longest = max(strings, key=len)

	# For i in range of the length of the longest string
	for i in range(len(longest)):
		# Print out the dictionary strings vertically with spaces in between
		# each of the characters. For example: 'S T R I N G' is our secret phrase,
		# and each character of 'STRING' has a string associated with it. Print the
		# character associated with the index 'i' of the string and the column
		# 'a' associated with the enumeration of keys (example: (S, 0)). Otherwise,
		# just print a space (the "or ' '" in the statement).
		print(' '.join(dictionary[a][i:i+1] or ' ' for j, a in enumerate(keys)))
	return

# Columnar Transposition cipher
def main():
	# Initializing a dictionary to hold the columns
	dictionary = {}

	# Take input from the user for text to encrypt
	to_encrypt = str(input('Write a string to encrypt: '))

	# Remove spaces
	if (' ' in to_encrypt):
		to_encrypt = "".join(to_encrypt.split())
	
	# Take input from the user for the secret word
	secret = str(input('Enter a secret word: '))

	# Remove spaces
	if (' ' in secret):
		to_encrypt = "".join(secret.split())
	
	# Add values to the list
	dictionary = {key: to_encrypt[i::len(secret)] for i, key in enumerate(secret)}

	print ('Text before encryption: \n')

	print_dict(dictionary)
	
	print('\nText after encryption: \n')

	# Using OrderedDict to sort the dictionary alphabetically
	dictionary = OrderedDict(sorted(dictionary.items()))

	print_dict(dictionary)
main()
		
