liczby0o = [(int(l.strip(), 8), l.strip())
            for l in open('./dane/62/liczby1.txt', 'r').readlines()]
liczby0d = [int(l.strip())
            for l in open('./dane/62/liczby2.txt', 'r').readlines()]


def decToOctal(num: int):
    octal = ''
    while num > 1:
        octal += str(num % (8))
        num -= num % (8)
        num = num // (8)
    return octal[::-1]


def pierwsze():
    print('1: ')
    print(f'Najmniejsza liczba: {min(liczby0o, key=lambda x: x[0])[1]}')
    print(f'Największa liczba: {max(liczby0o, key=lambda x: x[0])[1]}')
    print()


def drugie():
    ciagi = []
    ciag = []
    for i in range(len(liczby0d)-1):
        if liczby0d[i] <= liczby0d[i+1]:
            ciag.append(liczby0d[i])
        else:
            ciag.append(liczby0d[i])
            ciagi.append(ciag)
            ciag = []
    print('2: ')
    print(
        f'Pierwsza liczba ciągu: {max([(i, len(i)) for i in ciagi], key=lambda x: x[1])[0][0]}')
    print(
        f'Długość ciągu: {len(max([(i, len(i)) for i in ciagi], key=lambda x: x[1])[0])}')
    print()


def trzecie():
    liczby = list(zip(liczby0o, liczby0d))
    counter = [0, 0]
    for a, b in liczby:
        if a[0] > b:
            counter[0] += 1
        if a[0] == b:
            counter[1] += 1
    print('3: ')
    print(
        f'Liczba wierzy w których pierwsza liczba jest większa: {counter[0]}')
    print(f'Liczba równych wierszy: {counter[1]}')
    print()


def czwarte():
    print('4: ')
    print(
        f'Liczba szóstek w zapisie ósemkowym: {"".join([str(decToOctal(i)) for i in liczby0d]).count("6")}')
    print(
        f'Liczba szóstek w zapisie dziesiętnym: {open("./dane/62/liczby2.txt", "r").read().count("6")}')
    print()


pierwsze()
drugie()
trzecie()
czwarte()
