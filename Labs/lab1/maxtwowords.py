def main():
	text = input("Please enter some text: ");
	text = text.split();
	text.sort(reverse = True);
	print(text[0] + " " + text[1]);

if(__name__ == "__main__"):
	main();
