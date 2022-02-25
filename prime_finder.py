
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

	print(str(n) + ' is a prime.')
	return True

# Some driver code
def main():
	
	# A list of all of the primes that have been found
	prime_list = []

	# The upper bound for the prime check
	bound = ''
	while (not bound.isdigit()):
		# Ask input from the user
		bound = input('Upper bound for prime search (integers only): ')
	
	# Check odd numbers
	for i in range(1, bound, 2):
		if check_prime(i):
			prime_list.append(i)
	
	print('Prime list: \n' + str(prime_list))

main()
