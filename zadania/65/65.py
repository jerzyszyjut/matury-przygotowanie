from math import gcd

ulamki = [[int(i) for i in l.strip().split()] for l in open('./dane/65/dane_ulamki.txt').readlines()]


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def sprowadzenie_do_wspolnego_mianownika(ulamek1: list, ulamek2: list):
    LCM = lcm(ulamek1[1], ulamek2[1])
    return [((ulamek1[0] * LCM) // ulamek1[1]) + ((ulamek2[0] * LCM) // ulamek2[1]), LCM]


def wspolne_mianowniki(ulamki):
    ulamek = ulamki.pop(0)
    while len(ulamki) > 0:
        ulamek = sprowadzenie_do_wspolnego_mianownika(ulamek, ulamki.pop(0))
    return ulamek


def pierwsze():
    print('1: ')
    print(f'Ten ułamek to: {min(list(filter(lambda x: x[2] == min(list(map(lambda x: [x[0], x[1], round(x[0]/x[1], 5)], ulamki)), key=lambda x: x[2])[2], list(map(lambda x: [x[0], x[1], round(x[0]/x[1], 5)], ulamki)))), key=lambda x: x[1])[:2]}')
    print()


def drugie():
    print('2: ')
    print(f'Liczba tych ułamków to: {len(list(filter(lambda x: gcd(x[0], x[1]) == 1, ulamki)))}')
    print()


def trzecie():
    skrocone_ulamki = list(map(lambda x: [x[0] // gcd(x[0], x[1]), x[1] // gcd(x[0], x[1])], ulamki))
    suma_licznikow = sum(list(map(lambda x: x[0], skrocone_ulamki)))
    print('3: ')
    print(f'Suma liczników to: {suma_licznikow}')
    print()


def czwarte():
    print('4: ')
    duza_liczba = (2*2*3*3*5*5*7*7*13)
    koncowy_ulamek = wspolne_mianowniki(ulamki)
    print((koncowy_ulamek[0] * duza_liczba) // koncowy_ulamek[1])
    print()


# pierwsze()
# drugie()
# trzecie()
# czwarte()
