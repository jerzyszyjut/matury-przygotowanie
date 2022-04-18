dane = open('./dane/75/tekst.txt', 'r').read().strip().split()
probka = [l.strip().split() for l in open('./dane/75/probka.txt', 'r').readlines()]


def szyfr(znak, A, B):
    return chr(((((ord(znak) - 97) * A) + B) % 26) + 97)


def zaszyfruj_wyraz(wyraz, A, B):
    nowy_wyraz = ''
    for i in wyraz:
        nowy_wyraz += szyfr(i, A, B)
    return nowy_wyraz

# # 75.1
# print(set(filter(lambda x: x[0] == x[-1] == 'd', dane)))

# # 75.2
# A, B = 5, 2
# print(list(map(lambda x: ''.join(list(map(lambda y: szyfr(y, A, B), [i for i in x]))), list(filter(lambda x: len(x) >= 10, dane)))))


# # 75.3
# print(probka)
# for i in probka:
#     flag = True
#     for B in range(26):
#         for A in range(26):
#             if zaszyfruj_wyraz(i[0], A, B) == i[1]:
#                 print('Szyfr', A, B)
#             if zaszyfruj_wyraz(i[1], A, B) == i[0]:
#                 print('Deszyfr', A, B)
