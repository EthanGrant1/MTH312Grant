import numpy as n

# Hill Cipher
def main():
	# A 67 character alphabet
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?'

	# Hill cipher of block size 2 translates pairs of characters in numerical values,
	# creates new numerical values, of translates new number pairs back into characters
	
	# Equations for translation
	y1 = lambda a, x1, b, x2, m: (a*x1 + b*x2) % m
	y2 = lambda c, x1, d, x2, m: (c*x1 + d*x2) % m

	# Say we choose a = 3, b = 7, c = 9, d = 5. Our m value is the length of our alphabet..
	a = 3
	b = 7
	c = 9
	d = 5
	m = len(alphabet)
	
	# An example string for us to encrypt
	example_string = 'A short, simple message!'

	# Encode the string into numbers using our alphabet
	encoded = []
	for char in range(len(example_string)):
		encoded.append(alphabet.index(example_string[char]))
	
	print('String encoding using our alphabet:\n' +
	     f'{example_string} ----> {encoded}\n')
	
	# Encrypt the string using pairs of numbers derived from our translation equations
	encrypted = ''
	for num in range(0, len(encoded) - 1, 2):
		first = y1(a, encoded[num], b, encoded[num + 1], m)
		second = y2(c, encoded[num], d, encoded[num + 1], m)

		encrypted += alphabet[first] + alphabet[second]
	
	print(f'String after encryption using y1 = (a*x1 + b*x2) % m and y2 = (c*x1 + d*x2) % m\n' +
	     f'{encoded} ----> {encrypted}\n')
	
	# Matrix of a, b, c, and d
	M = n.zeros((2,2))
	M[0, 0] = a
	M[0, 1] = b
	M[1, 0] = c
	M[1, 1] = d
	
	print(f'Matrix of a, b, c, and d: \n{M}\n')
	
	# Size of the columns
	size = int(len(example_string) / 2)

	# Create a matrix to hold our encoded characters
	M2 = n.zeros((2, size))
	
	# Place the characters in our matrix
	count = 0
	for col in range(size):
		for row in range(len(M2)):
			M2[row][col] = encoded[count]
			count += 1

	print(f'Matrix of encoded characters: \n{M2}\n')
	
	# Let's try a different set of a, b, c, and d
	M3 = M2

	# Perform matrix multiplication on a, b, c, d and our encoded characters
	M2 = n.matmul(M, M2)
	
	# New a, b, c, d
	M[0, 0] = 5
	M[0, 1] = 20
	M[1, 0] = 3
	M[1, 1] = 11
	
	# Perform matrix multiplication on our new a, b, c, d and our encoded characters
	M3 = n.matmul(M, M3)

	# String representations
	encrypted = ''
	encrypted2 = ''
	for col in range(size):
		for row in range(len(M2)):
			# Perform modular arithmetic on all of our values
			M2[row][col] = int(M2[row][col] % len(alphabet))
			M3[row][col] = int(M3[row][col] % len(alphabet))
			
			# Find the index of the character, and access our alphabet. This is our ciphertext.
			encrypted += alphabet[int(M2[row][col])]
			encrypted2 += alphabet[int(M3[row][col])]
	
	print(f'Matrix representation of encryption: \n{M2}')
	print(f'Encrypted string: \n{encrypted}\n')

	print(f'Matrix representation of encryption using a = 5, b = 20, c = 3, d = 11: \n{M3}')
	print(f'Encrypted string: \n{encrypted2}')

if __name__ == "__main__":
	main()
