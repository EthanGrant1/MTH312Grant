def euclid(vec1, vec2):
	
	q = vec1[0] // vec2[0]
	print ('Value of q: ' + str(q))

	for ele in range(len(vec2)):
		vec2[ele] *= q

	vk_plus1 = []
	for ele in range(len(vec1)):
		vk_plus1.append(vec1[ele]-vec2[ele])

	print ('Value of vec1 ... ' + str(vec1))
	print ('Value of vec2 ... ' + str(vec2))
	print ('Value of (vec1 - (q * vec2)) ... ' + str(vk_plus1))
	
	if (vk_plus1[0] == 0):
		print ('Result has been found!')
		for ele in range(len(vec2)):
			vec2[ele] /= q
		print (str(vec2[0]) + ' = ' + str(vec2[1]) + ' * a + ' + str(vec2[2]) + ' * b')
	else:
		return euclid(vec2, vk_plus1)

def main():
	a = int(input('Enter a number for a: '))
	b = int(input('Enter a number for b: '))

	v0 = [a, 1, 0]
	v1 = [b, 0, 1]

	euclid(v0, v1)
main()
