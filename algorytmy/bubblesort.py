lst = [6, 2, 7, 8, 3, 6, 4, 2, 7, 2]


def bubble_sort(lst: list):
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst


print(bubble_sort(lst))
