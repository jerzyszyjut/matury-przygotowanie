ciagi = [i.strip() for i in open('./dane/63/ciagi.txt', 'r').readlines()]


def eratostenes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


liczby_pierwsze = list(eratostenes(max([int(i, 2) for i in ciagi])+1))


def czynniki_pierwsze(n):
    i = 0
    while n > 1:

        while n % liczby_pierwsze[i] == 0:
            n = n / liczby_pierwsze[i]
            yield liczby_pierwsze[i]
        i += 1


def dwucykliczne():
    for ciag in ciagi:
        if ciag[:len(ciag)//2] == ciag[len(ciag)//2:]:
            yield ciag


def pierwsze():
    print('1: ')
    print(f'Ciągi: {list(dwucykliczne())}')
    print()


def drugie():
    print('2: ')
    print(
        f"Liczba ciągów: {len(list(filter(lambda x: x.count('11') == 0, ciagi)))}")
    print()


def trzecie():
    liczby_polpierwsze = list(filter(lambda x: len(
        list(czynniki_pierwsze(x))) == 2, map(lambda x: int(x, 2), ciagi)))
    print('3: ')
    print(
        f"Liczba liczb półpierwszych: {len(liczby_polpierwsze)}")
    print(f"Największa liczba półpierwsza: {max(liczby_polpierwsze)}")
    print(f"Najmniejsza liczba półpierwsza: {min(liczby_polpierwsze)}")
    print()


pierwsze()
drugie()
trzecie()
