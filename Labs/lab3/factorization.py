def main():
    n = int(input("Please enter a natural number greater that 1: "));
    primes = [];
    for tested in range(2, n + 1):
        for p in primes:
            if not tested % p:
                break;
        else:
            primes.append(tested);

    i = 0;
    factors = [];
    div = n;
    while div > 1:
        if not div % primes[i]:
            factors.append(primes[i]);
            div = div // primes[i];
        else:
            i += 1;

    print(n, "= ",end='');
    for i in range(len(factors) - 1):
        print(str(factors[i]) + "*",end='');

    print(factors[-1]);
    return;

if(__name__ == "__main__"):
    main();
