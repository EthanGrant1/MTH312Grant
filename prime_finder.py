
def check_prime(n, prime_list):
	m = str(n)
	last = m[len(m)-1]
	
	if (n in prime_list):
		return True
	
	if ((last == '0' or last == '2' or last == '4' or last == '5' or
	    last == '6' or last == '8')):
#	    	print(str(n) + ' is not a prime.')
	    	return False
	
	res = 0
	for num in prime_list[1:-1]:
		res = n % num
		if (res == 0):
#			print(str(n) + ' is not a prime.')
			return False

	print(str(n) + ' is a prime.')
	return True

def main():
	prime_list = [1, 2, 3, 5, 7]
	
	bound = ''
	while (not bound.isdigit()):
		bound = input('Upper bound for prime search (integers only): ')
	
	bound = abs(int(bound))

	for i in range(1, bound):
		if check_prime(i, prime_list):
			prime_list.append(i)
	
	print('Prime list: \n' + str(prime_list))

main()
