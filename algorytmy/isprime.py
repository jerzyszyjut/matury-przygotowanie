num = 11


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False
    else:
        return True


print(is_prime(num))
