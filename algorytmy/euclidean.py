a = 10
b = 15


def euclidean(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(euclidean(a, b))
