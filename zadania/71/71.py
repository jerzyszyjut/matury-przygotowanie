funkcje = [[float(i) for i in l.strip().split()] for l in open('./dane/71/funkcja.txt', 'r').readlines()]


def f(x):
    if x >= 0 and x < 1:
        return (funkcje[0][0]) + (funkcje[0][1] * (x)) + (funkcje[0][2] * (x ** 2)) + (funkcje[0][3] * (x ** 3))
    if x >= 1 and x < 2:
        return (funkcje[1][0]) + (funkcje[1][1] * (x)) + (funkcje[1][2] * (x ** 2)) + (funkcje[1][3] * (x ** 3))
    if x >= 2 and x < 3:
        return (funkcje[2][0]) + (funkcje[2][1] * (x)) + (funkcje[2][2] * (x ** 2)) + (funkcje[2][3] * (x ** 3))
    if x >= 3 and x < 4:
        return (funkcje[3][0]) + (funkcje[3][1] * (x)) + (funkcje[3][2] * (x ** 2)) + (funkcje[3][3] * (x ** 3))
    if x >= 4 and x < 5:
        return (funkcje[4][0]) + (funkcje[4][1] * (x)) + (funkcje[4][2] * (x ** 2)) + (funkcje[4][3] * (x ** 3))


# 71.1
print(f(1.5))

# 71.2
wyniki = []
for i in range(40000, 45000):
    wyniki.append((i/10000, abs(f(i/10000))))
print(max(wyniki, key=lambda x: x[1]))

# 71.3
dokladnosc = 100000
przedzial = (0.5, 0.6)
pierwsze = []
for i in range(int(przedzial[0] * dokladnosc), int(przedzial[1] * dokladnosc)):
    pierwsze.append((i/dokladnosc, abs(f(i/dokladnosc))))

przedzial = (2.5, 2.65)
drugie = []
for i in range(int(przedzial[0] * dokladnosc), int(przedzial[1] * dokladnosc)):
    drugie.append((i/dokladnosc, abs(f(i/dokladnosc))))

przedzial = (3.25, 3.4)
trzecie = []
for i in range(int(przedzial[0] * dokladnosc), int(przedzial[1] * dokladnosc)):
    trzecie.append((i/dokladnosc, abs(f(i/dokladnosc))))

przedzial = (4.75, 4.9)
czwarte = []
for i in range(int(przedzial[0] * dokladnosc), int(przedzial[1] * dokladnosc)):
    czwarte.append((i/dokladnosc, abs(f(i/dokladnosc))))

print(min(pierwsze, key=lambda x: x[1])[0], min(drugie, key=lambda x: x[1])[0], min(trzecie, key=lambda x: x[1])[0], min(czwarte, key=lambda x: x[1])[0])
