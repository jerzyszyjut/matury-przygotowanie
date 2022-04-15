def fib(n):
    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n):
        a, b = b, a + b
    return a


def czy_pierwsza(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** (1/2))+1, 2):
        if n % i == 0:
            return False
    return True


# 67.1
print(fib(10), fib(20), fib(30), fib(40))

# 67.2
print(list(filter(lambda x: czy_pierwsza(x), [fib(i) for i in range(1, 41)])))

# 67.3
binarki = [bin(fib(i))[2:] for i in range(1, 41)]
max_dlugosc = max(list(map(lambda x: len(x), binarki)))
binarki_2 = list(map(lambda x: ((max_dlugosc-len(x)) * '0') + x, binarki))
print(binarki_2)

# 67.4
print(list(filter(lambda x: x.count('1') == 6, binarki)))
