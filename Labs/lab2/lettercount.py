from string import ascii_letters

def main():
    d = {};
    text = input("Please enter some text: ");

    for c in text:
        if c in ascii_letters:
            c = c.upper();
            if c in d:
                d[c] += 1;
            else:
                d[c] = 1;

    for c in d:
        print(c + ":", d[c]);

    return;

if(__name__ == "__main__"):
    main();