def zaszyfruj(wiadomosc, klucz, wypisz_powtorzenia=False):
    wiadomosc = [i for i in wiadomosc]
    i = 0
    j = 0
    while i < len(wiadomosc):
        if wiadomosc[i] in ' ,.':
            i += 1
            continue
        indeks_klucza = ord(klucz[j % len(klucz)])-65
        wiadomosc[i] = chr(((((ord(wiadomosc[i]) + indeks_klucza) - 65) % 26)) + 65)
        i += 1
        j += 1
    if wypisz_powtorzenia:
        print(f'Liczba powtórzeń: {int(j / len(klucz)) + 1}')
    return ''.join(wiadomosc)


def odszyfruj(wiadomosc, klucz):
    i = 0
    j = (len(wiadomosc.replace(' ', '').replace(',', '').replace('.', '')) % len(klucz)) * -1
    wiadomosc = [i for i in wiadomosc][::-1]
    klucz = klucz[::-1]
    while i < len(wiadomosc):
        if wiadomosc[i] in ' ,.':
            i += 1
            continue
        indeks_klucza = ord(klucz[j % len(klucz)])-65
        wiadomosc[i] = chr(((abs((26 + ord(wiadomosc[i]) - indeks_klucza) - 65) % 26)) + 65)
        i += 1
        j += 1
    return ''.join(wiadomosc)[::-1]


def liczba_wystapien(wiadomosc):
    wiadomosc = wiadomosc.replace(' ', '').replace(',', '').replace('.', '')
    wystapienia = {}
    for i in wiadomosc:
        wystapienia[i] = wystapienia.get(i, 0) + 1
    return wystapienia


def indeks_koincydencji(wiadomosc):
    licznik = 0
    mianownik = 0
    for i in liczba_wystapien(wiadomosc).values():
        licznik += (i*(i-1))
    suma = sum(liczba_wystapien(wiadomosc).values())
    mianownik = suma * (suma - 1)
    return licznik / mianownik


# # 77.1
# dane = open('./dane/77/dokad.txt', 'r').read().strip()
# print(zaszyfruj(dane, 'LUBIMYCZYTAC', wypisz_powtorzenia = True))

# # 77.2
# dane, klucz = [l.strip() for l in open('./dane/77/szyfr.txt', 'r').readlines()]
# print(odszyfruj(dane, klucz))

# # 77.3
# dane, klucz = [l.strip() for l in open('./dane/77/szyfr.txt', 'r').readlines()]
# d = 0.0285 / (indeks_koincydencji(dane) - 0.0385)
# print(d, len(klucz))
