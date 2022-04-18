def szyfrowanie(wiadomosc, klucz):
    wiadomosc = [i for i in wiadomosc]
    for i in range(len(wiadomosc)):
        index_zamiany = klucz[i % len(klucz)] - 1
        wiadomosc[i], wiadomosc[index_zamiany] = wiadomosc[index_zamiany], wiadomosc[i]
    return ''.join(wiadomosc)


def deszyfrowanie(wiadomosc, klucz):
    wiadomosc = [i for i in wiadomosc]
    for i in list(range(len(wiadomosc)))[::-1]:
        index_zamiany = klucz[i % len(klucz)] - 1
        wiadomosc[i], wiadomosc[index_zamiany] = wiadomosc[index_zamiany], wiadomosc[i]
    return ''.join(wiadomosc)

# # 76.1
# dane = [l.strip() for l in open('./dane/76/szyfr1.txt').readlines()][:-1]
# klucze = [int(i) for i in [l.strip() for l in open('./dane/76/szyfr1.txt').readlines()][-1].split()]
# print([szyfrowanie(l, klucze) for l in dane])

# # 76.2
# dane = [l.strip() for l in open('./dane/76/szyfr2.txt').readlines()][:-1]
# klucze = [int(i) for i in [l.strip() for l in open('./dane/76/szyfr2.txt').readlines()][-1].split()]
# print(szyfrowanie(dane[0], klucze))


# # 76.3
# dane = [l.strip() for l in open('./dane/76/szyfr3.txt').readlines()]
# print(deszyfrowanie(dane[0], [6, 2, 4, 1, 5, 3]))
