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
	
	temp = ''
	count = 0
	row = 0
	mat = [[], [], [], [], []]
	for char in key:
		temp += char + ' '
		mat[row].append(char)
		count += 1
		if (count == 5):
			print(temp)
			temp = ''
			count = 0
			row += 1
	
	to_encipher = input('\nPlease enter a string to encrypt: ')
	to_encipher = ''.join(to_encipher.split()).upper()
	
	new = ''
	for i in range(len(to_encipher) - 1):
		if (to_encipher[i] == to_encipher[i + 1]):
			new += to_encipher[i] + 'X'
		else:
			new += to_encipher[i]

	new += to_encipher[len(to_encipher) - 1]
	
	if (len(new) % 2) > 0:
		if (new[len(new) - 1] == 'X'):
			new += 'A'
		else:
			new += 'X'

	temp = ''
	for i in range(len(new)):
		if ((i % 2) == 0) and (i > 0):
			temp += ' ' + new[i]
		else:
			temp += new[i]

	print('\nDigrams created. The digrams look like this: \n' + temp)

	
main()
