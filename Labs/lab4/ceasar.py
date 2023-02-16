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

def decode(text, key):
	lst = [];
	for c in range(len(text)):
		lst.append(text[c]);

	for i in range(len(lst)):
		if lst[i] == " ":
			continue;
		lst[i] = ord(lst[i]) - key;
		if lst[i] < 97:
			lst[i] += 26;
		lst[i] = chr(lst[i]);
	return "".join(lst);

text = input("Input the text for encoding: ");
key = int(input("Input a key between 1 and 25: "));

print(encode(text, key));
print(decode(encode(text, key), key));
