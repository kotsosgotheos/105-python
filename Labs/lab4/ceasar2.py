def encode(text, key):
        lst = [];
	for c in range(len(text)):
		lst.append(text[c]);

	for i in range(len(lst)):
		if lst[i] == " ":
			continue;
		lst[i] = ord(lst[i]) + key;
		if lst[i] > 122:
			lst[i] -= 26;
		lst[i] = chr(lst[i]);
	return "".join(lst);

def breakcode(plaintext, cyphertext):
	for i in range(1, 26):
		if cyphertext == encode(plaintext, i):
			return i;
	return -1;

plaintext = input("Input the plaintext: ");
cyphertext = input("Input the cyphertext: ");

print("Key: %d" %(breakcode(plaintext, cyphertext)));
