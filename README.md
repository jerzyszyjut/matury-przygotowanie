# matury-przygotowanie

## Spis treści
- [Wstęp](#wstęp)
- [Algorytmy](#algorytmy)
    - [Sortujące](#sortujące)
        - [Bubble sort](#bubble-sort---sortowanie-bąbelkowe)
        - [Merge sort](#merge-sort---sortowanie-przez-scalanie)
    - [Wyszukujące](#wyszukujące)
        - [Linear search](#linear-search---przeszukiwanie-liniowe)
        - [Binary search](#binary-search---wyszukiwanie-binarne)
    - [Liczbowe](#liczbowe)
        - [Sito Eratostenesa](#sito-eratostenesa)

## Wstęp
Repozytorium zostało stworzone z myślą przygotowań do  egazminu maturalnego. 

Będę umieszczał tutaj rozwiązania wykonywanych przeze mnie zadań oraz algorytmów wymaganych w podstawie programowej.

Na stronie CKE jest dostępny [zbiór zadań](https://www.cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/Matura_Zbi%C3%B3r_zada%C5%84_Informatyka.pdf) oraz [pliki potrzebne do rozwiązania zadań](https://www.cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-dane.zip)

#### Spis treści zbioru zadań
- Zadania z programowania od 106 do 146 strony 
- Zadania Excel od 147 do 185 strony
- Zadania z baz danych od 185 do 218 strony
- Odpowiedzi z programowania od 450 do 468 strony 
- Odpowiedzi Excel od 469 do 486 strony 
- Odpowiedzi z baz danych od 486 do 503 strony 

# Algorytmy
## Sortujące
### [Bubble sort - Sortowanie bąbelkowe)](./algorytmy/bubblesort.py)

Złożoność: **O(n²)**

![bubblesort](./docs/bubblesort.gif)
### [Merge sort - Sortowanie przez scalanie](./algorytmy/mergesort.py)

Złożoność: **O(n × log n)**

![mergesort](./docs/mergesort.gif)

### [Quick sort - Sortowanie szybkie](./algorytmy/quicksort.py)

Średnia złożoność: **O(n × log n)**

Najgorsza złożoność: **O(n²)**

Często stosuje się zamiast merge sorta, ponieważ ma mniejszą złożoność pamięciową i niższą stałą czasową.

![quicksort](./docs/quicksort.gif)

### Wyszukujące
### [Linear search - Przeszukiwanie liniowe](./algorytmy/linearsearch.py)

Złożoność: **O(n)**

![linear](./docs/linearsearch.gif)

### [Binary search - Wyszukiwanie binarne](./algorytmy/binarysearch.py)

Złożoność: **O(log n)**

![binary](./docs/binarysearch.gif)

### Liczbowe
### [Sito Eratostenesa](./algorytmy/eratostenes.py)

Złożoność: **O(n × log(log n))**

![eratostenes](./docs/eratosthenes.gif)
