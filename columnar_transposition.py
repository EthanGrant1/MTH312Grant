from collections import OrderedDict

# Print the dictionary
def print_dict(dictionary):
	keys = list(dictionary.keys())

	temp = ' '.join(keys[i] for i in range(len(keys)))

	print(temp)
	print('-'*len(temp))

	for i in range(len(dictionary[keys[0]])):
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
		
