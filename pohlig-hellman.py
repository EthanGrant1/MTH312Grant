import numpy as n
import math as m
from random import randrange as r
import copy as c
import sys

# Check if a number is prime
def check_prime(n):	
	n = abs(int(n))

	if n < 2:
		return False

	if n == 2:
		return True

	if not n & 1:
		return False

	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

# Create a matrix of powers mod a number "a"
def power(a):
	return n.array([[base**num % a for num in range(1, a)] for base in range(1, a)])

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

def main():
	# Some examples of Fermat's Little Theorem
	print('Fermat\'s Little Theorem:\n')
	print('Table of powers of ints mod 5')
	arr = power(5)
	print(arr)
	print()
	
	print('Table of powers of ints mod 7')
	arr = power(7)
	print(arr)
	print()
	
	print('Table of pwoers of ints mod 11')
	arr = power(11)
	print(arr)
	print()

	# Ask input from the user
	plain = input('Please enter text to encrypt: ')
	
# Old error checking stuff. Don't use now.
#	done = False
#	while done == False:
#		try:

	# Find a random large prime
	p = 0
	while not check_prime(p):
		p = r(1000000, 100000000)

	print('p\'s value is ' + str(p) + '\n')
		
	# Find a random value between 0 and p-1
	E = 0
	while E % 2 != 1:
		E = r(1, p-1)

	# Calculate the number we will use for encryption
	e = int(E / m.gcd(E, p-1))
	print('e\'s value is: ' + str(e))
	

# Old eror checking stuff. Don't use it now.
#			temp = 0
#			for i in range(len(plain)):
#				temp = int(powermod(ord(plain[i]), e, p))
#				print('Temp: ' + str(temp))
#			done = True
#		
#		# Just in case if something goes wrong
#		except Exception as e:
#			print(e)
#			continue

	# Initializing some values
	numbers = ''
	num_list = []
	encrypted = ''
	encrypt_list = []
	decrypted = ''
	decrypt_list = []
	num = 0

	# Encrypt our plaintext
	for i in range(len(plain)):
		# ASCII value of the character
		numbers += str(ord(plain[i]))
		num_list.append(ord(plain[i]))
		
		num = int(powermod(ord(plain[i]), e, p))

		encrypted += str(num)
		encrypt_list.append(num)		

	print('Number representation of your string: ' + numbers)
	print('After encryption: ' + encrypted + '\n')

	print('Finding a value for d.')
	
	# Find a value for "d"
	d = 0
	while((d*e) % (p-1)) != 1:
		d += 1

	print('d\'s value is: ' + str(d) + '\n')
			
	# Decrypt the text using the d value
	for i in range(len(encrypt_list)):
		decrypt_list.append(powermod(encrypt_list[i], d, p))
	
	print('Original number list: ' + str(num_list))
	print('Encrypted list after decryption: ' + str(decrypt_list) + '\n')

	for i in range(len(decrypt_list)):
		decrypted += str(chr(decrypt_list[i]))

	print('Decrypted text: ' + str(decrypted))

main()
