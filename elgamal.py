import random
import math
import sys

# Check if a number is prime
def check_prime(n: int):	
	# Positive integers only
	n = abs(n)

	# 0 and 1 are not considered primes because they do not divide by 2 numbers
	if n < 2:
		return False

	# 2 is the only even prime
	if n == 2:
		return True
	
	# If n is even, it is not a prime
	if not n & 1:
		return False

	# From 3 to square root of n, count by 2s (skip even numbers), and check factors
	for i in range(3, int(n**0.5) + 1, 2):
		# If there is another number that divides n, it isn't prime
		if n % i == 0:
			return False

#	print(str(n) + ' is a prime.')

	# n is prime
	return True

# powermod function
def powermod(base, exponent, mod):
	# Initialize a result
	res = 1
	# exponent value that we will use
	e = exponent
	# What we are exponentiating
	power = base

	# Raise by exponent e
	while e > 0:
		# If e is odd
		if (e % 2) == 1:
			# Continue raising the result by power and then mod it
			res = (res*power) % mod
		# Floor division by 2
		e = e // 2
		# Square the power value, then mod it
		power = (power*power) % mod

	return res

# Find the prime factors of a number
def prime_factors(factors, num):
	
	# Continue dividing by 2 to find the smallest even divisor
	while num % 2 == 0:
		factors.add(2)
		num = num // 2
	
	# Find prime factors from 3 to square root of num
	for i in range(3, int(num**0.5) +  1, 2):
		while num % i == 0:
			factors.add(i)
			num = num // i

	# A leftover factor
	if num > 2:
		factors.add(num)

# Find a generator value
def primative(n):
	# Set of prime factors
	s = set()
	
	# Check if n is prime
	if not check_prime(n):
		return 0

	# Prime factors of n - 1, put them into a set
	phi = n - 1
	prime_factors(s, phi)

	# Iterate through numbers from 2 to n
	for i in range(2, phi + 1):
		flag = False
		
		# Iterate over the prime factors
		for item in s:
			# If it is not a primitive root (the result is 1), don't use it
			if (powermod(i, phi // item, n) == 1):
				flag = True
				break
		
		# Else, return i
		if (flag == False):
			return i
	return 0

# The Elgamal Assymetric Encryption / Decryption Cryptosystem
def main():
	print('Finding a (very) large prime p...')

	p = 0
	# Choose a random prime with a lot of digits
	while not check_prime(p):
		p = int(random.randrange(100000000000000, 1000000000000000))

	print('p is: ' + str(p) + '\n')
	
	# Find the generator, or primitive root of prime p
	print('Finding a generator g...')
	g = int(primative(p))
	print('g\'s value is: ' + str(g) + '\n')

	# In practice, there could be some algorithm or method to selecting this number,
	# but for the sake of this example, it will just be random.
	print('Picking a value b (such that 1 < b < p)...')
	b = int(random.randrange(2, p))
	print('b\'s value is: ' + str(b) + '\n')

	# Using what we have, we are generating a public key for the recipient
	print('Calculating Bob\'s number (B =  g^b mod p)')
	B = int(powermod(g, b, p))
	print('Bob\'s number is: ' + str(B))
	print('Bob\'s public key is: (', p, ', ', g, ', ', B, ')\n')

	# Ask input from the user to generate a message
	encode = input('You are Alice. Enter a message to encrypt: ')
	ascii_list = []

	# Convert to ASCII representation
	for char in range(len(encode)):
		ascii_list.append(int(ord(encode[char])))

	# Create a long string of ASCII numbers
	string = ''
	for i in range(len(ascii_list)):
		string += str(ascii_list[i])

	# Again, we select a random number. This time for Alice.
	print('Message after encoding is: ' + string + '\n')
	print('Picking a value r (such that 0 < r < p). This will be our "nonce"...')
	r = random.randrange(1, p)
	print('r\'s value is: ' + str(r))

	# R is our encryption hint
	print('Calculating R = g^r % p')
	R = int(powermod(g, r, p))
	print('R\'s value is: ' + str(R) + '\n')

	print('Calculating ciphertext n = (m*(B**r % p)) % p...')
	
	# Using this formula, we produce new numbers from our ASCII values. This is the ciphertext.
	encrypt_list = []
	for i in range(len(ascii_list)):
		n = int((ascii_list[i] * powermod(B, r, p)) % p)
		encrypt_list.append(n)
	
	# Make the ciphertext one long string
	string = ''
	for i in range(len(encrypt_list)):
		string += str(encrypt_list[i])

	print('Message after encryption is: ' + string)
	print(str(encrypt_list) + '\n')
	print('Bob has received your message. He is decrypting your message by computing c = ((message) * (R ^ (p-1-b)) % p) % p.')
	
	# To decrypt, we use our encryption hint R from earlier
	decrypt_list = []
	for i in range(len(encrypt_list)):
		c = int((encrypt_list[i] * powermod(R, (p-1-b), p)) % p)
		decrypt_list.append(c)
	
	# Convert the decrypted string to a list of ASCII values, and the characters for each one
	string = ''
	string2 = ''
	for i in range(len(decrypt_list)):
		string += str(decrypt_list[i])
		string2 += chr(decrypt_list[i])

	# We have now successfully carried out the Elgamal Cryptosystem
	print('Message after decryption is: ' + string)
	print(str(decrypt_list))
	print('Message after converting to text: ' + string2)
	
main()









