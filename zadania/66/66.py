def czy_trojkat(liczby):
    if sum(liczby)-max(liczby) > max(liczby):
        return '1'
    return '0'


def czy_prostokatny(liczby):
    a, b, c = liczby
    if ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2):
        return '1'
    return '0'


def eratostenes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for j in range(i*i, limit, i):
                a[j] = False


def suma_cyfr(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma


dane = [[int(k) for k in l.strip().split()] for l in open('./dane/66/trojki.txt').readlines()]
limit = max(list(map(lambda x: max(x[0:2]), dane)))
liczby_pierwsze = list(eratostenes(limit))

# 66.1
print(list(filter(lambda x: (suma_cyfr(x[0]) + suma_cyfr(x[1])) == x[2], dane)))

# 66.2
print(list(filter(lambda x: x[0] in liczby_pierwsze and x[1] in liczby_pierwsze and (x[0] * x[1]) == x[2], dane)))

# 66.3
print(list(map(lambda x: x[0], list(filter(lambda x: x[1] == 'T', list(zip(dane, [i for i in ''.join(list(map(czy_prostokatny, dane))).replace('11', 'TT').replace('1', '0')])))))))

# 66.4
print(max(list(map(lambda x: len(x), ''.join(list(map(czy_trojkat, dane))).split('0')))))
print(''.join(list(map(czy_trojkat, dane))).count('1'))
