dane = [l.strip().split() for l in open('./dane/72/napisy.txt', 'r').readlines()]


def dlugosc_zakonczenia(wyrazy):
    a, b = wyrazy[0][::-1], wyrazy[1][::-1]
    i = 0
    while a[i] == b[i]:
        i += 1
    return i


# 72.1
print(list(filter(lambda x: (len(x[0]) * 3) <= len(x[1]) or (len(x[1]) * 3) <= len(x[0]), dane))[0], len(list(filter(lambda x: (len(x[0]) * 3) <= len(x[1]) or (len(x[1]) * 3) <= len(x[0]), dane))))

# 72.2
print(list(map(lambda x: [x, x[1][len(x[0]):]], list(filter(lambda x: x[0] in x[1] and x[0] == x[1][:len(x[0])], dane)))))


# 72.3
dlugosci = list(map(lambda x: [x, dlugosc_zakonczenia(x)], dane))
max_dlugosc = max(dlugosci, key=lambda x: x[1])[1]
print(list(filter(lambda x: x[1] == max_dlugosc, dlugosci)))
