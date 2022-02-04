
# Viginere Cipher
def main():
	
	# Regular Latin alphabet
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# The Viginere Square
	square = []

	# The Viginere Square is made up of 26 alphabets, each shifted over by 1 from the previous
	# Example: B, C, D, E...
	#          C, D, E, F...
	#          ...
	for i in range(1, 26):
		# Make a 2D array of characters
		square.append([])

		# Create the new alphabet by slicing the regular alphabet
		# starting at position i, then append the rest, from
		# the beggining to i - 1. Repeat until i = 25.
		sliced = alphabet[i:len(alphabet)] + alphabet[0:i]

		# Create a list of all of the chars
		square[i-1] = [char for char in sliced]
	
	# The last alphabet is just the regular alphabet
	square.append([char for char in alphabet])
	
	print('This is the Viginere Square:\n')
	for row in range(len(square)):
		print(str(' '.join(square[row][col] for col in range(len(square[row])))))
	
	# Ask input from the user for a string to encipher
	plain = input('\nEnter a string to encipher: ')
	
	# Remove spaces
	plain = ''.join(plain.split())

	# Ask input from the user for a secret phrase
	secret = input('Enter a secret phrase: ')
	
	# Remove spaces
	secret = ''.join(secret.split())

	# Create a key phrase
	key = ''
	
	# Repeat the secret phrase as necessary to fill the key
	while (len(key) < len(plain)):
		key += secret
	
	# Slice it to fit the plain text length. Also, put it in upper case.
	key = key[0:len(plain)].upper()

	print('\nPlain text and key: \n' + plain)
	print(key)
	
	# Encipher the text
	enciphered = ''

	# For every character in our plain text
	for char in range(len(plain)):
		# Search the square's rows
		for row in range(len(square)):
			# We are searching for the row that corresponds to our key phrase.
			# Ex: If our key phrase was 'MARYHADALITTLELAMB', we want to search
			# for the row where 'M' is the first letter of the row
			if (square[row][0] == key[char]):
				# Plain alphabet is the last row of the Viginere Square
				plain_alpha = square[len(square) - 1]

				# We want the plain text character
				what_we_want = plain[char].upper()

				# The column that it belongs to corresponds to the plain
				# alphabet's index
				proper_column = plain_alpha.index(what_we_want)

				# Our enciphered string corresponds to the same column as the plain
				# text character, but on the key phrase row
				enciphered += square[row][proper_column]
	
	print('\nEnciphered text: \n' + enciphered)
main()

