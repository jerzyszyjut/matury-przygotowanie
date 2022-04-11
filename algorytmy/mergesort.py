def merge(a: list, b: list) -> list:
    final_array = []
    while len(a) != 0 or len(b) != 0:
        print(a, b)
        if len(a) == 0:
            for element in b:
                final_array.append(element)
            break
        if len(b) == 0:
            for element in a:
                final_array.append(element)
            break
        if a[0] > b[0]:
            final_array.append(b.pop(0))
        elif a[0] < b[0]:
            final_array.append(a.pop(0))
        elif a[0] == b[0]:
            final_array.append(a.pop(0))
            final_array.append(b.pop(0))
    return final_array


def mergesort(lst: list) -> list:
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    print(lst[:mid], lst[mid:])
    return merge(mergesort(lst[:mid]), mergesort(lst[mid:]))


print(merge([1, 4, 6, 8], [1, 2, 4, 7, 10]))
