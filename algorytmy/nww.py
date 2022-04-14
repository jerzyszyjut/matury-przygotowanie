a = 10
b = 15


def nww(a, b):
    return abs(a * b) // euclidean(a, b)


def euclidean(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(nww(a, b))
