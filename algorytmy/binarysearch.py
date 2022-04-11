lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]


def binary_search(lst: list, searched: int):
    l = 0
    r = len(lst) - 1
    mid = (l+r) // 2
    while l <= r:
        if lst[mid] > searched:
            r = mid - 1
        elif lst[mid] < searched:
            l = mid + 1
        else:
            return mid
        mid = (l+r) // 2
    return None


print(binary_search(lst, 6))
