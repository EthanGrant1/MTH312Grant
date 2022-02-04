import copy as c
import random as r
from collections import OrderedDict as o

# Print the dictionary
def print_dict(dictionary, kind):
	# Access all of the keys in list [] notation
	keys = list(dictionary.keys())
	
	# Make a string out of all the keys
	key_str = ' '.join(keys[i] for i in range(len(keys)))
	
	# If you're printing out the key card
	if (kind == 'card'):
		print('   ' + key_str)
		print('   ' + '-'*len(key_str))
	
	# Else,
	else:
		print(key_str)
		print('-'*len(key_str))
	
	# Get all of the strings in the dictionary
	strings = [dictionary[key] for key in keys]
	# Find the longest string by the length
	longest = max(strings, key=len)

	# For i in range of the length of the longest string
	for i in range(len(longest)):
		# Print the card with the keys on the side
		if (kind == 'card'):
			print(str(keys[i] + '| ' + ' '.join(dictionary[a][i:i+1] or ' ' for j, a in enumerate(keys))))
		
		# Else, we don't want to get index access errors
		else:
			print(str(' '.join(dictionary[a][i:i+1] or ' ' for j, a in enumerate(keys))))
	return

def main():
	# Our 'alphabet' includes all of the letters and numbers 0-9
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

	# Initialize the dictionary with our keys ADFGVX
	card = {'A': '', 'D': '', 'F': '', 'G': '', 'V': '', 'X': ''}
	
	# While there are characters still available
	while (alphabet != ''):
		
		# Go through the keys in order
		for key in card:
			# If there are multiple characters in the alphabet available
			if (len(alphabet) > 1):
				# Pick a random character
				rand = r.randrange(len(alphabet))
			
			# If there's only 1 character left
			elif (len(alphabet) == 1):
				# Make the index 0
				rand = 0

			# Add the chosen character to the current key
			card[key] += alphabet[rand]

			# Get rid of the character. We don't need it anymore.
			alphabet = alphabet.replace(alphabet[rand], '')
	
	print ('Translation card created! You translation card is:\n')
	print_dict(card, 'card')
	print('')
		
	# Take input from the user for text to encrypt
	to_encrypt = str(input('Write a string to encrypt: '))

	# Remove spaces
	if (' ' in to_encrypt):
		to_encrypt = "".join(to_encrypt.split())
	
	# Make all of the chars uppercase
	to_encrypt = to_encrypt.upper()
	
	# Take input from the user for the secret word
	secret = str(input('Enter a secret word: '))

	# Remove spaces
	if (' ' in secret):
		to_encrypt = "".join(secret.split())
	
	# Make all of the chars uppercase
	secret = secret.upper()
	
	# Access the keys in list [] notation
	keys = list(card.keys())

	# Our encoded string
	encoded = ''

	# For every character that we are going to encrypt
	for char in to_encrypt:
		
		# For all of the keys in the card
		for key in card:
			# Check if the character is in the current string. If not, go to the next one.
			if (char not in card[key]):
				continue

			# For every character in the current string
			for ele in card[key]:
				
				# If it is the character we are looking for...
				if (char == ele):
					# encode the character as it's position on the 2D grid
					encoded += str(key) + keys[card[key].index(ele)]

	# Add values to the ciphertext
	ciphertext = {key: encoded[i::len(secret)] for i, key in enumerate(secret)}

	# Add values to the cleartext
	cleartext = {key: to_encrypt[i::len(secret)] for i, key in enumerate(secret)}


	print('Before encryption: \n')
	print_dict(cleartext, 'cleartext')
	print('')


	print('\nEncoded text: ' + encoded + '\n')
	
	print('After encryption: \n')
	print_dict(ciphertext, 'cipher')
	
	# Sort the dictionary alphabetically
	ciphertext = o(sorted(ciphertext.items()))
	
	print('\nAfter sorting: \n')
	print_dict(ciphertext, 'sorted')
main()
