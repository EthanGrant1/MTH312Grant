from math import gcd as g
from random import randrange as r
import copy as c

# Prime checker
def check_prime(n):
	# Positive values only
	n = abs(int(n))

	# 0 and 1 are not prime because they do not have exactly 2 multiples
	if n < 2:
		return False

	# 2 is the only even prime
	if n == 2:
		return True

	# Otherwise, all other even numbers are not prime
	if not n & 1:
		return False

	# Check numbers from 3 to the square root of n. Only check the odd numbers.
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False

#	print(str(n) + ' is a prime.')
	return True

# Knuth's Extended Euclidean Algorithm
def euclid(vec1, vec2):

	# Whole number quotient q_k+1 for r_k-1 / r_k
	q = vec1[0] // vec2[0]

	# Multiply q_k+1 * v_k
	vec2copy = c.deepcopy(vec2)
	for ele in range(len(vec2copy)):
		vec2copy[ele] *= q
	
	# New vector v_k+1 = v_k-1 - (q_k+1 * v_k)
	# v_k-1 = [r_k+1, m_k+1, n_k+1]
	vk_plus1 = []
	for ele in range(len(vec1)):
		vk_plus1.append(vec1[ele]-vec2copy[ele])

#	print ('Value of vec1 ... ' + str(vec1))
#	print ('Value of q ... ' + str(q))
#	print ('Value of vec2 ... ' + str(vec2))
#	print ('Value of (vec1 - (q * vec2)) ... ' + str(vk_plus1) + '\n')
	
	# If r_k+1 = 0, r_k is the greatest common factor of a and b
	if (vk_plus1[0] == 0):
		print ('Result has been found!')
		
		# Final values of v_k
		print (str(vec2[0]) + ' = ' + str(vec2[1]) + ' * d + ' + str(vec2[2]) + ' * phi')
		return vec2
	
	# Else, increase k by one and start again
	else:
		return euclid(vec2, vk_plus1)

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

# RSA Encryption
def main():
	# Two large primes p and q
	p = 0
	q = 0

	print('Selecting two large primes, p and q...')
	# Pick a random prime number, p
	while not check_prime(p):
		p = r(10000000000000, 1000000000000000)
	print('Value for p: ' + str(p))

	# Pick a random prime q that is different from p
	while (not check_prime(q)) or (q == p):
		q = r(10000000000000, 1000000000000000)
	print('Value for q: ' + str(q) + '\n')

	# M is p times q. This will be part of the public key.
	M = p * q
	print('Value for M = p * q: ' + str(M))
	
	# A variable, phi that we will use for calculating another part of the key
	phi = (p-1) * (q-1)
	print('Value for phi = (p-1) * (q-1): ' + str(phi))

	print('Finding a value d such that: 1 < d < (phi-1), and gcd(d, phi) = 1...')
	d = phi-2
	# Find the greatest common factor of d and phi - 1 and make sure that it equals 1
	while g(d, phi) != 1:
		# Generate a random value for d in the range of 1 < d < (phi-1)
		d = r(2, phi-1)
	print('Value for d: ' + str(d) + '\n')

	# Now we are calculating the next part of the key, a number "e" which is the multiplicitive inverse of d % phi
	vec1 = [d, 1, 0]
	vec2 = [phi, 0, 1]
	print('Performing Euclidean algorithm on d and phi...')
	new_vec = euclid(vec1, vec2)

	# Multiplicitive inverses
	e = new_vec[1]
	k = new_vec[2]
	print('\nValue for e: ' + str(e))
	print('Value for k: ' + str(k) + '\n')
	
	if e < 0:
		e += phi
	
	print('Your public key is: (' + str(M) + ', ' + str(e) + ')\n')
	
	# The encryption process
	string = input('Enter a string to encrypt: ')

	# Encoding to ASCII and encrypting those numbers
	n = 0
	num_list = []
	print('Encoding text into ASCII (call these numbers "m") and then encrypting using n = (m ^ e) % M...')
	for char in range(len(string)):
		m = ord(string[char])
		n = powermod(m, e, M)
		num_list.append(n)

	print('Encryption complete. List of numbers: ' + str(num_list) + '\n')

	print('We got the message back. Now we will decrypt it by decrypting the numbers using c = (n ^ d) % M'
	      + ' and converting c back into readable characters.')

	c = 0
	ascii_list = []
	# Perform our function on all of the encrypted numbers and turn them back into chars
	for num in range(len(num_list)):
		c = powermod(num_list[num], d, M)
		ascii_list.append(chr(c))
	
	string = ''
	
	for char in ascii_list:
		string += char
	print('Decryption complete. The string was: ' + str(string))

main()

