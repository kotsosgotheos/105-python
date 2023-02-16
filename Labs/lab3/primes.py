def main():
    n = int(input("Please enter a natural number greater that 1: "));
    primes = [];
    for tested in range(2, n):
        for p in primes:
            print(p);
            print(tested);
            if not tested % p:
                break;
        else:
            primes.append(tested);

    print(primes);
    return;

if(__name__ == "__main__"):
    main();
