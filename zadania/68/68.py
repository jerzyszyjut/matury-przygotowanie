dane = [l.strip().split() for l in open('./dane/68/dane_napisy.txt', 'r').readlines()]


def count_letters(string):
    litery = {}
    for litera in string:
        litery[litera] = litery.get(litera, 0) + 1
    return dict(map(lambda x: (x, litery[x]), sorted(litery)))

# 68.1
# licznik = 0
# for i in dane:
#     zbior = set()
#     for j in ''.join(i):
#         zbior.add(j)
#     if len(zbior) == 1 and i[0] == i[1]:
#         licznik += 1
# print(licznik)


# 68.2
# licznik = 0
# for i in dane:
#     if count_letters(i[0]) == count_letters(i[1]):
#         licznik += 1
# print(licznik)

# 68.3
liczniki = []
for i in dane:
    liczniki.append(count_letters(i[0]))
    liczniki.append(count_letters(i[1]))
liczniki_2 = []
for i in liczniki:
    liczniki_2.append(liczniki.count(i))
print(max(liczniki_2))
