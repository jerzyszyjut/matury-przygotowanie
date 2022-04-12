lst = [6, 2, 7, 8, 3, 6, 4, 2, 7, 2]


def quicksort(lst: list):
    less = []
    greater = []
    equal = []

    if len(lst) < 2:
        return lst

    pivot = lst[0]
    for element in lst:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return quicksort(less) + equal + quicksort(greater)


print(quicksort(lst))
