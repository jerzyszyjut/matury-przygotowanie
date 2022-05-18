num = 11


def is_prime(num):
    if num < 3:
        return False
    for i in range(3, int(num**(1/2))+1, 2):
        if (num % i) == 0:
            return False
    return True


print(is_prime(num))
