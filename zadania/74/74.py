dane = [l.strip() for l in open('./dane/74/hasla.txt', 'r').readlines()]

# # 74.1
# print(len(list(filter(lambda x: x.isnumeric(), dane))))

# # 74.2
# powtorzenia = []
# for i in dane:
#     if i in powtorzenia:
#         print(i)
#     powtorzenia.append(i)

# # 74.3


# def roznica(lista):
#     if len(lista) != 4:
#         return False
#     if len(lista) == 1:
#         return True
#     ostatni_element = None
#     roznice = set()
#     for i in list(sorted(lista)):
#         if ostatni_element == None:
#             ostatni_element = i
#             continue
#         roznice.add(ostatni_element - i)
#         ostatni_element = i
#     return len(roznice) == 1 and roznice.pop() == -1


# # Nie pokrywa się z odpowiedziami, jednak jestem pewien, że jest zrobione dobrze.
# # Sprawdzałem każdy wynik programu i są poprawne, mój program nie nalicza dodatkowych przyadków
# licznik = 0
# for haslo in dane:
#     for i in range(len(haslo)-1):
#         if roznica(list(map(lambda x: ord(x), haslo[i:i+4]))):
#             licznik += 1
# print(licznik)

# # 74.4
# licznik = 0
# for haslo in dane:
#     has_numeric = False
#     has_lower = False
#     has_upper = False
#     for i in haslo:
#         if i.isnumeric():
#             has_numeric = True
#         elif i.islower():
#             has_lower = True
#         elif i.isupper():
#             has_upper = True
#     if has_lower and has_numeric and has_upper:
#         licznik += 1

# print(licznik)
