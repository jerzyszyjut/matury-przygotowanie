def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


print(list(primes_sieve(1000)))
