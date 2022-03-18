# Playfair cipher
def main():
	# Remove 1 letter from the alphabet. 'Q' is usually the best option
	# because it appears very infrequently in words.
	alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'

	# Ask the user for a secret phrase
	secret = input('Please enter a secret phrase (letters only): ')

	# Eliminate repeats / spaces and put it in uppercase
	secret = ''.join(secret.split()).upper()
	key = ''
	for char in secret:
		if (char not in key and char in alphabet):
			key += char
	
	# Apeend the rest of the characters in alphabetical order
	for char in alphabet:
		if (char not in key):
			key += char
	
	print ('\nKey phrase has been generated. Your key phrase is: \n' + key + '\n')
	
	# Creating a matrix out of the key
	temp = ''
	count = 0
	row = 0
	mat = [[], [], [], [], []]
	for char in key:
		temp += char + ' '
		mat[row].append(char)
		count += 1

		# Every 5 characters, go to a new row
		if (count == 5):
			print(temp)
			temp = ''
			count = 0
			row += 1
	
	# Our text to encipher
	to_encipher = input('\nPlease enter a string to encrypt: ')
	to_encipher = ''.join(to_encipher.split()).upper()
	
	# "Q" is not in our alphabet, so we replace it with "K" instead.
	# Also, "QU" is changed to "KW" for clarity.
	if ("QU" in to_encipher):
		to_encipher = to_encipher.replace('QU', 'KW')
	
	if ("Q" in to_encipher):
		to_encipher = to_encipher.replace('Q', 'K')

	# Append "X" to digrams that have the same letter
	new = ''
	for i in range(len(to_encipher) - 1):
		if (to_encipher[i] == to_encipher[i + 1]):
			new += to_encipher[i] + 'X'
		else:
			new += to_encipher[i]

	new += to_encipher[len(to_encipher) - 1]
	
	# Append "X" or "A" if the string is of odd length
	if (len(new) % 2) > 0:
		if (new[len(new) - 1] == 'X'):
			new += 'A'
		else:
			new += 'X'

	# Space out the digrams
	temp = ''
	for i in range(len(new)):
		if ((i % 2) == 0) and (i > 0):
			temp += ' ' + new[i]
		else:
			temp += new[i]

	print('\nDigrams created. The digrams look like this: \n' + temp)

	digrams = [[]]
	count = 0
	# Place the digrams into separate lists
	for char in range(len(temp)):
		if temp[char] == ' ':
			digrams.append([])
			count += 1
		else:
			digrams[count].append(temp[char])

	count = 0
	temp = ''
	# Encrypt the digrams
	for i in range(len(digrams)):
		# Keepings track of the positions
		row1 = 0
		col1 = 0
		row2 = 0
		col2 = 0

		# For every row in the matrix...
		for row in range(len(mat)):
			# Set the row and col for each letter of the digram
			if digrams[i][0] in mat[row]:
				row1 = row
				col1 = mat[row].index(digrams[i][0])
			if digrams[i][1] in mat[row]:
				row2 = row
				col2 = mat[row].index(digrams[i][1])
		
		# If the characters are in the same row, use the letter to the
		# right of the character in the ciphertext, wrapping left as necessary
		if (row1 == row2):
			if (col1 == len(mat[row1])-1):
				temp += mat[row1][0]
			else:
				temp += mat[row1][col1+1]
			
			if (col2 == len(mat[row2])-1):
				temp += mat[row2][0]
			else:
				temp += mat[row2][col2+1]
		
		# If the characters are in the same column, use the letter below
		# the character in the ciphertext, wrapping upwards as necessary
		elif (col1 == col2):
			if (row1 == len(mat)-1):
				temp += mat[0][col1]
			else:
				temp += mat[row1+1][col1]

			if (row2 == len(mat)-1):
				temp += mat[0][col2]
			else:
				temp += mat[row2+1][col2]
		
		# Else, the letters must be on different rows and different columns.
		# In this case, use the two letters as two corners of a square and assign
		# each letter the one parallel to the other by column. (For example,
		# the first letter will be in its row, but in the second letter's column,
		# and the second letter will be in its row, but in the first lett's column.)
		else:
			temp += mat[row1][col2] + mat[row2][col1]
	
	print('Translation complete! The translation is: ' + str(temp))
main()
