n = 12


def fib_recursive(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_dynamic(n):
    a, b = 0, 1
    if n == 1:
        return b
    if n == 0:
        return a
    for i in range(n-1):
        a, b = b, a + b
    return b


print(fib_recursive(n))
print(fib_dynamic(n))
