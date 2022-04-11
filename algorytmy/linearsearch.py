lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]


def linear_search(input_list: list, element: int):
    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i
    return None


print(linear_search(lst, 3))
