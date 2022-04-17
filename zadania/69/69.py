dane = [i.strip() for i in open('./dane/69/dane_geny.txt', 'r').readlines()]


def pozyskaj_geny(gen):
    geny = []
    flag = gen.find('AA')
    while flag != -1:
        gen = gen[flag:]
        if gen.find('BB') == -1:
            break
        geny.append(gen[:gen.find('BB')+2])
        gen = gen[gen.find('BB')+2:]
        flag = gen.find('AA')
    return geny


# 69.1
# liczba_genow = {}
# for gen in dane:
#     liczba_genow[len(gen)] = liczba_genow.get(len(gen), 0) + 1
# print(len(liczba_genow))
# print(liczba_genow[max(liczba_genow, key=lambda x: liczba_genow[x])])

# 69.2
# geny = list(map(lambda x: sorted(pozyskaj_geny(x)), dane))
# licznik = 0
# for gen in geny:
#     for j in gen:
#         if j.count('BCDDC') > 0:
#             licznik += 1
# print(licznik)

# 69.3
# geny = list(map(lambda x: sorted(pozyskaj_geny(x)), dane))
# print(len(max(geny, key=lambda x: len(x))))
# max_len = 0
# for i in geny:
#     for j in i:
#         if len(j) > max_len:
#             max_len = len(j)
# print(max_len)

# 69.4
def czy_gen_odporny(gen):
    if pozyskaj_geny(gen) == pozyskaj_geny(gen[::-1]):
        return True
    return False


print(len(list(filter(lambda x: x == x[::-1], dane))))
print(len(list(filter(czy_gen_odporny, dane))))
