#https://www.codewars.com/kata/52223df9e8f98c7aa7000062/discuss#label-issue
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
rot13alphabet = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
ROT13ALPHABET = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def rot13(message):
	decipheredMessage = []
	asdf = ""
	message = list(message)
	for i in message:
		if i in rot13alphabet:
			index = rot13alphabet.index(i)
			decipheredMessage.append(alphabet[index])
		elif i in alphabet:
			index = alphabet.index(i)
			decipheredMessage.append(rot13alphabet[index])
		elif i in ALPHABET:
			index = ALPHABET.index(i)
			decipheredMessage.append(ROT13ALPHABET[index]) 
		elif i in ROT13ALPHABET:
			index = ROT13ALPHABET.index(i)
			decipheredMessage.append(ALPHABET[index])
		else:
			decipheredMessage.append(i)
	for i in decipheredMessage:
		asdf+=i
	return asdf