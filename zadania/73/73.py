dane = [l.strip() for l in open('./dane/73/tekst.txt', 'r').readlines()]


def czestotliwosc(wyraz):
    litery = {}
    for i in wyraz:
        litery[i] = litery.get(i, 0) + 1
    return {k: [litery[k], {k: round((v / len(wyraz)) * 100, 2) for k, v in litery.items()}[k]] for k in list(sorted(litery))}


def najdluzsze_podslowo(wyraz):
    wyraz = wyraz.upper()
    samogloski = 'aeiouy'.upper()
    ostatnia_litera = None
    liczniki = []
    licznik = 0
    for i in wyraz:
        if i not in samogloski:
            licznik += 1
        else:
            liczniki.append(licznik)
            licznik = 0
    liczniki.append(licznik)
    return max(liczniki)


# 73.1
wyrazy = dane[0].split()
licznik = 0
for wyraz in wyrazy:
    last_letter = None
    for i in wyraz:
        if last_letter == None:
            last_letter = i
            continue
        if last_letter == i:
            licznik += 1
            break
        last_letter = i
print(licznik)


# 73.2
litery = dane[0].replace(' ', '')
print(czestotliwosc(litery))

# 73.3
slowa = list(map(lambda x: [x, najdluzsze_podslowo(x)], dane[0].split()))
max_dlugosc = max(slowa, key=lambda x: x[1])[1]
print(max_dlugosc, len(list(filter(lambda x: x[1] == max_dlugosc, slowa))), list(filter(lambda x: x[1] == max_dlugosc, slowa))[0][0])
