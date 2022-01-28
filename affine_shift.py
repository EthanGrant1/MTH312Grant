# Examaple of a affine shift

# Calculate (18 + 22) mod 26
example = (18 + 22) % 26
print ('(18 + 22) % 26 = ' + str(example) + '\n')

# Two integers (a and b) that are congruent to 18 mod 26
a = b = 0
target = 18 % 26

while ((a % 26) != target or (a == 18)):
	a += 1
b = a + 1
while ((b % 26) != target):
	b += 1

print ('Values of a and b that are congruent to (18 % 26)... a: ' + str(a) + ' ... b: ' + str(b))

# Two integers (c and d) that are congruent to 22 mod 26
c = d = 0
target = 22 % 26

while ((c % 26) != target or (c == 22)):
	c += 1
d = c + 1
while ((d % 26) != target):
	d += 1

print ('Values of c and d that are congruent to (22 % 26)... c: ' + str(c) + ' ... d: ' + str(d) + '\n')

# Calculating the following equations
equation_a = (a + c) % 26
equation_b = (a + d) % 26
equation_c = (b + c) % 26
equation_d = (b + d) % 26

print ('Value of (a + c) % 26 = ' + str(equation_a))
print ('Value of (a + d) % 26 = ' + str(equation_b))
print ('Value of (b + c) % 26 = ' + str(equation_c))
print ('Value of (b + d) % 26 = ' + str(equation_d) + '\n')

# Calculating the following equations... but multiplying
equation_a = (a * c) % 26
equation_b = (a * d) % 26
equation_c = (b * c) % 26
equation_d = (b * d) % 26

print ('Value of (a * c) % 26 = ' + str(equation_a))
print ('Value of (a * d) % 26 = ' + str(equation_b))
print ('Value of (b * c) % 26 = ' + str(equation_c))
print ('Value of (b * d) % 26 = ' + str(equation_d) + '\n')

# Encrypting using an affine shift
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
alphabet_list = [char for char in alphabet]
# print ('Alphabet: ' + str(alphabet))
word = 'AMAZING'
print ('Word that we are going to encrypt: ' + word)
# print (str(alphabet_list[5]))

# f(x) = (7x + 5) % 26
alphabet_2 = []
for i in range(len(alphabet_list)):
	res = (7 * i) + 5
	print (str(res))
	if (res >= len(alphabet_list)):
		alphabet_2.append(alphabet_list[res % 26])
	else:
		alphabet_2.append(alphabet_list[res])

indices = [word.index(char) for char in word]
string = ''.join(alphabet_2[indices[i]] for i in indices)
print ('Alphabet encrypted with f(x) = (7x + 5) % 26... \n' + str(alphabet_2))
print (word + ' after encryption is: ' + string + '\n')

# f(x) = (6x + 2) % 26
alphabet_2 = []
for i in range(len(alphabet_list)):
	res = (6 * i) + 2
	# print (str(res))
	if (res >= len(alphabet_list)):
		alphabet_2.append(alphabet_list[res % 26])
	else:
		alphabet_2.append(alphabet_list[res])

indices = [word.index(char) for char in word]
string = ''.join(alphabet_2[indices[i]] for i in indices)
print ('Alphabet encrypted with f(x) = (6x + 2) % 26... \n' + str(alphabet_2))
print (word + ' after encryption is: ' + string + '\n')

# f(x) = (13x + 7) % 26
alphabet_2 = []
for i in range(len(alphabet_list)):
	res = (13 * i) + 7
	# print (str(res))
	if (res >= len(alphabet_list)):
		alphabet_2.append(alphabet_list[res % 26])
	else:
		alphabet_2.append(alphabet_list[res])

indices = [word.index(char) for char in word]
string = ''.join(alphabet_2[indices[i]] for i in indices)
print ('Alphabet encrypted with f(x) = (13x + 7) % 26... \n' + str(alphabet_2))
print (word + ' after encryption is: ' + string + '\n')
