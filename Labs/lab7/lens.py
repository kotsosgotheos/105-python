from string import ascii_letters
ascii_letters += "-\a\b\f\n\r\t\v ";

def strip_punc(text):
	text = list(text);
	for letter in range(len(text)):
		if text[letter] in ascii_letters and len(text[letter]) > 0:
			continue;
		text[letter] = "";
	return "".join(text);

def count_lens(s):
	words = {};
	s = s.split();
	for word in s:
		if len(word) not in words:
			words[len(word)] = 1;
		else:
			words[len(word)] += 1;
	return sorted(words.items());

def main():
	f = open("ourladyschild.txt", "r");
	text = f.read();
	s = strip_punc(text);
	words = count_lens(s);
	for item in words:
		print("%d words have length %d" %(item[1], item[0]));
	f.close();

if(__name__ == "__main__"):
	main();
