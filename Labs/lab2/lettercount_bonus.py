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

    l = list(d.items());
    l.sort();
    for x in l:
        print(x[0] + ":", x[1]);

    return;

if(__name__ == "__main__"):
    main();

