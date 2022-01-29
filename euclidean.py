# Knuth's Extended Euclidean Algorithm
def euclid(vec1, vec2):
	
	# Whole number quotient q_k+1 for r_k-1 / r_k
	q = vec1[0] // vec2[0]
	print ('Value of q: ' + str(q))

	# Multiply q_k+1 * v_k
	for ele in range(len(vec2)):
		vec2[ele] *= q
	
	# New vector v_k+1 = v_k-1 - (q_k+1 * v_k)
	# v_k-1 = [r_k+1, m_k+1, n_k+1]
	vk_plus1 = []
	for ele in range(len(vec1)):
		vk_plus1.append(vec1[ele]-vec2[ele])

	print ('Value of vec1 ... ' + str(vec1))
	print ('Value of vec2 ... ' + str(vec2))
	print ('Value of (vec1 - (q * vec2)) ... ' + str(vk_plus1))
	
	# If r_k+1 = 0, r_k is the greatest common factor of a and b
	if (vk_plus1[0] == 0):
		print ('Result has been found!')
		
		# TODO: This needs to be debugged. Some of the values aren't right in the vectors.
		for ele in range(len(vec2)):
			vec2[ele] /= q

		# Final values of v_k
		print (str(vec2[0]) + ' = ' + str(vec2[1]) + ' * a + ' + str(vec2[2]) + ' * b')
	
	# Else, increase k by one and start again
	else:
		return euclid(vec2, vk_plus1)
def main():
	# Take input from the user for 2 integers, a and b
	a = int(input('Enter a number for a: '))
	b = int(input('Enter a number for b: '))

	# Step 0: r0 = a, r1 = b, then v0 = [r0, 1, 0] and v1 = [r1, 0, 1]
	v0 = [a, 1, 0]
	v1 = [b, 0, 1]

	# Start the algorithm
	euclid(v0, v1)
main()
