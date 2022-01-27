#####################################
# SHIFT_CIPHER.PY:                  #
#                                   #
# This program uses a shift cipher  #
# to encrypt text.                  #
#####################################

# An array that holds the alphabet, both lowercase and uppercase.
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# shift(char, num): This function shifts the index of
# "char" by "num"'s value
def shift(char, num):

	# Ignore spaces
	if (char == ' '):
		return ' '
	
	# Invalid characters
	if (char not in alphabet):
		raise Exception('Invalid characters in string')
	
	# Else, the charaters are part of our character set
	else:
		# If the index we are trying to access needs to wrap...
		if ((alphabet.index(char) + num) > len(alphabet) or num < 0):
			# Use modular arithmetic to find the remainder after division by our alphabet's size
			return alphabet[(alphabet.index(char) + num) % (len(alphabet) + 1)]
		else:
			# Otherwise, just increment the index by num
			return alphabet[alphabet.index(char) + num]
def main():
	# Asking input from the user for the string and number to shift by
	string_to_encode = input('Please enter a string (letters and spaces only): ')
	num_to_shift = int(float(input('Please enter a value to shift by (positive or negative ints): ')))

	# Initialize our strings
	encoded_string = ''
	decoded_string = ''

	# Shift all of the characters in our original string by num_to_shift
	for char in string_to_encode:
		encoded_string += shift(char, num_to_shift)
	
	print('String before decoding: ' + str(string_to_encode) + '\n')
	print('String after encoding: ' + str(encoded_string) + '\n')
	print('Decoding string...' + '\n')

	# Reverse the process by subtracting our shift amount
	for char in encoded_string:
		decoded_string += shift(char, (num_to_shift*-1))
	
	print('String after decoding: ' + str(decoded_string))
main()
