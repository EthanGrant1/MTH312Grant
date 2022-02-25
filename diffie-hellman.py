import math

# Diffie-Hellman Key Exchange Protocol
def main():
	# Our alphabet of 26 characters. Capital letters only.
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# Some functions that we are verifying
	f = lambda x: (7*x + 11) % 26
	g = lambda x: (15*x + 17) % 26
	h = lambda x: (17*x + 5) % 26
	k = lambda x: (23*x + 15) % 26
	
	print('Functions that we will use...')
	print('f(x) = 7x + 11')
	print('g(x) = 15x + 17')
	print('h(x) = 17x + 5')
	print('k(x) = 23x + 15' + '\n')

	# Testing multiplicitive inverses
	print('Testing inverses...')
	for x in range(0, 26):
		print('Values for x = ' + str(alphabet[x]))
		print('Value of f(x) = ' + str(alphabet[f(x)]) + ' Value of f(g(x)) = ' + str(alphabet[f(g(x))]))
		print('Value of h(x) = ' + str(alphabet[h(x)]) + ' Value of k(h(x)) = ' + str(alphabet[h(k(x))]) + '\n')
	
	print('Simplification of functions...')
	print('Simplification of h(f(x)) = 17(7x + 11) + 5 = 119x + 187 + 5 = 119x + 192')
	print('Simplication of f(h(x)) = 7(17x + 5) + 11 = 119x + 35 + 11 = 119x + 46\n')

	# Encoding a sample string as its index values
	string = 'HELLO'
	temp = ''
	for char in string:
		temp += str(alphabet.index(char)) + '-'
	temp = temp[0:-2]
	
	print(string + ' after being encoded to numbers 0 through 25 is ' + temp + '\n')

	print('Enciphering using f(x) = (7x + 11) % 26')

	# Encrypting using one of our functions f
	temp = ''
	for char in string:
		temp += alphabet[f(alphabet.index(char))]

	print(string + ' ---> ' + temp + '\n')
	print('Re-enciphering using h(x) = (17x + 5) % 26')

	# Enciphering again using another function h
	temp2 = ''
	for char in temp:
		temp2 += alphabet[h(alphabet.index(char))]
	
	print(temp + ' ---> ' + temp2 + '\n')
	
	print('Deciphering using g(x) = (15x + 17) % 26')
	
	# Deciphering using f's inverse function g
	temp = ''
	for char in temp2:
		temp += alphabet[g(alphabet.index(char))]
	
	print(temp2 + ' ---> ' + temp + '\n')
	print('Deciphering using k(x) = (23x + 15) % 26')

	# Deciphering again using h's inverse function k
	temp2 = ''
	for char in temp:
		temp2 += alphabet[k(alphabet.index(char))]
	
	print(temp + ' ---> ' + temp2 + '\n')
	
	print('The deciphering process did not undo the cipher properly because' +
	'the compositions of the functions creates different results due to the distributive property\n')

	# That didn't work. Let's try again using some slightly different functions.
	f = lambda x: (7*x) % 26
	g = lambda x: (15*x) % 26
	h = lambda x: (17*x) % 26
	k = lambda x: (23*x) % 26

	print('Functions that we will use...')
	print('f(x) = 7x')
	print('g(x) = 15x')
	print('h(x) = 17x')
	print('k(x) = 23x' + '\n')

	# Testing that these are indeed inverse functions
	print('Testing inverses...')
	for x in range(0, 26):
		print('Values for x = ' + str(alphabet[x]))
		print('Value of f(x) = ' + str(alphabet[f(x)]) + ' Value of f(g(x)) = ' + str(alphabet[f(g(x))]))
		print('Value of h(x) = ' + str(alphabet[h(x)]) + ' Value of k(h(x)) = ' + str(alphabet[h(k(x))]) + '\n')
	
	print('Simplifying functions...')
	print('h(f(x)) = 17(7*x) = 119x')
	print('f(h(x)) = 7(17*x) = 119x')

	# Encoding our sample string
	string = 'HELLO'
	temp = ''
	for char in string:
		temp += str(alphabet.index(char)) + '-'
	temp = temp[0:-2]
	
	print(string + ' after being encoded to numbers 0 through 25 is ' + temp + '\n')

	print('Enciphering using f(x) = (7x) % 26')
	
	# Encrypting using f
	temp = ''
	for char in string:
		temp += alphabet[f(alphabet.index(char))]

	print(string + ' ---> ' + temp + '\n')
	print('Re-enciphering using h(x) = (17x) % 26')

	# Encrypting again using h
	temp2 = ''
	for char in temp:
		temp2 += alphabet[h(alphabet.index(char))]
	
	print(temp + ' ---> ' + temp2 + '\n')
	
	print('Deciphering using g(x) = (15x) % 26')

	# Decrypting using f's inverse function g
	temp = ''
	for char in temp2:
		temp += alphabet[g(alphabet.index(char))]
	
	print(temp2 + ' ---> ' + temp + '\n')
	print('Deciphering using k(x) = (23x) % 26')

	# Decrypting using h's inverse function k
	temp2 = ''
	for char in temp:
		temp2 += alphabet[k(alphabet.index(char))]
	
	# It worked properly. We were able to decipher without ever knowing the other person's encryption method.
	print(temp + ' ---> ' + temp2 + '\n')
	print('These functions are able to be deciphered properly because there is no distribution taking place. ' +
	'The order mattered for the other functions because it depended on what the other number of the function was' +
	' getting multiplied by. These new functions however, produce the same result regardless of order, so they are able' +
	' to be decomposed in any order.\n')

	print('Generators modulo a prime number...')
	print('(11^8) % 31 = ' + str((11**8) % 31))
	print('(8^12) % 29 = ' + str((8**12) % 29) + '\n')

	print('Repeated Squaring...\n')

	# Some examples of repeated squaring
	modulus1 = 29
	base1 = 8
	exponent1 = 25
	res1 = 1

	modulus2 = 31
	base2 = 11
	exponent2 = 13
	res2 = 1

	print('(8^25) % 29')
	while (exponent1 > 0):
		if (exponent1 % 2 == 1):
			# Find the result of multiplying by the base over and over again
			temp = res1
			res1 = (res1 * base1) % modulus1
			print('(' + str(temp) + ' * ' + str(base1) + ') ' + '% ' + str(modulus1) + ' = ' + str(res1))
		
		# Find the next whole number exponent
		exponent1 = math.floor(exponent1 / 2)

		# Extra case
		if (exponent1 > 0):
			base1 = (base1 * base1) % modulus1

	print('(8^25) % 29 = ' + str(res1) + '\n')

	# Do the same thing. This time with 11, 13 and 31.
	print('(11^13) % 31')
	while (exponent2 > 0):
		if (exponent2 % 2 == 1):
			temp = res2
			res2 = (res2 * base2) % modulus2
			print('(' + str(temp) + ' * ' + str(base2) + ') ' + '% ' + str(modulus2) + ' = ' + str(res2))
		
		exponent2 = math.floor(exponent2 / 2)
		
		if (exponent2 > 0):
			base2 = (base2 * base2) % modulus2
	
	print('(11^13) % 31 = ' + str(res2) + '\n')

	# Diffie-Hellman Key Exchange Protocol
	p = 29
	g = 8
	a = 12
	b = 17
	A = (g**a) % p
	B = (g**b) % p
	print('Diffie-Hellman Protocol...')
	print('Assume two people, Alice and Bob, that choose a common prime p and generator g.')
	print('Assume a prime p = ' + str(p) + ' and a generator g = ' + str(g) + '. Now assume some numbers a = ' + str(a) + ' and b = ' + str(b) + 
	'. Now we will calculate \ng^a mod p which is ' + str(A) + '. Call this number A. Then, we will calculate g^b mod p which is ' + str(B) +
	'. Call this number B. \nNow, (A^b) % p = ' + str(A) + '^' + str(b) + ' mod ' + str(p) + ' = ' + str((A**b) % p) + ' and (B^a) % p = ' + 
	str(B) + '^' + str(a) + ' mod ' + str(p) + ' = ' + str((B**a) % p) + '. Both are equal. Alice and Bob chose their secret exponents a and b.\n' + 
	'Alice calculates (g^a) mod p, which results in their number A. A is sent to Bob, who then computes (g^b) mod p which results in their number B.\n' + 
	'Then, using their same exponents from before, Alice computes K = (B^a) mod p and Bob computes K = (A^b) mod p. They now have the same key that\n' +
	'they can use for encryption.\n')

	print('Using XOR bitwise operations...')
	print('"Hi" in binary representation is ' + str(format(48, '08b')) + ' ' + str(format(69, '08b')))
	
	# An example. Use the 8-bit representation of H and i to form "Hi". Also, use the key K as our method of encryption.
	H = str(format(48, '08b'))
	i = str(format(69, '08b'))
	K = str(format(34707, '16b'))

	Hi = H + i
	res = ''
	for char in range(len(Hi)):
		# Bitwise XOR function
		res += str(int(Hi[char]) ^ int(K[char]))
	
	print('Performing bitwise XOR on "Hi" with the key K = ' + str(K) + ', the result is: ' + res)

	# Decrypting using our key. Notice how we can encode again using hexadecimal, so it's an extra layer or protection.
	C9FC = str("{0:16b}".format(int("C9FC", 16)))
	print('"C9FC" converted to binary is ' + C9FC + '.')
	
	res = ''
	for char in range(len(K)):
		# Bitwise XOR function
		res += str(int(C9FC[char]) ^ int(K[char]))
	
	print('Performing bitwise XOR on "C9FC" results in ' + str(res) + '.')
	print('Converting this to binary and then ASCII, we have 78-111 ---> "No"' )
main()
