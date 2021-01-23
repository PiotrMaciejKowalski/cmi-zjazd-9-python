# Sprawnie działające lotnisko jest istnym koszmarem logistycznym. Nie przeszkodziło to jednak twojemu przyjacielowi
# zatrudnić się w jego wieży kontrolnej. Na razie jego zadanie jest dość proste - ma przypisywać samoloty do konkretnych
# wyjść na lotnisku. Lotnisko nie jest zbyt obciążone ruchem, więc samoloty otwierają swoje bramki o pełnych godzinach.
# Na daną godzinę kolega otrzymuje liczbę samolotów potrzebujących bramki, oraz listę dostępnych bramek. Kolega
# obawia się pomyłki, i np. wysłania dwóch samolotów do tej samej bramki. Pomóż mu pisząc program obliczający ilość
# różnych sposobów podziału bramek na obsługujące i nie.
#
# Uwaga! Który samolot podejdzie do konkretnej z bramek - leży już w kompetencji współpracownika kolegi. Kolega wskazuje
# jedynie listę bramek, które trzeba przygotować. (Samoloty są nie rozróżnialne, bramki jednak tak)
#
# Dane:
# n - ilość samolotów dla których trzeba zabezpieczyć bramkę
# m - ilość dostępnych bramek (bramki są oznaczane 1,2,...,m) [wersja podstawowa]
# lista_bramek - lista obiektów typu str z nazwami dostępnych bramek [wersja zaawansowana]
# Wynik:
# z - ilość dostępnych przypisań które bramki mają obsługiwać samolot o danej godzinie. [wersja podstawowa i zaawansowana]
# sol - lista z listami wygenerowanych układów bramek (wszystkie poprawne wybory) [wersja zaawansowana]

# Jeśli lotnisko ma m bramek, to ile jest sposobow na otwarcie tych bramek?
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1

# kluczem jest reprezentacja binarna liczb
# trzeba przeszukac az 2^m
# interesuja nas te ustawienia w ktorych jest dokladnie n - jedynek


def policz_jedynki_binarne(liczba):
    result = 0
    while liczba > 0:
        result += liczba % 2 # 1 lub 0
        liczba //= 2 # usuniecie ostatniej cyfry binarnej
    return result

def bramki(n, m):

    if n > m :
        return 0, [] # 0 mozliwych przypisan, zatem lista rozwiazan jest pusta

    result = 0 #ilosci rozwiazan
    sol = [] # lista rozwiazan
    for i in range(0,2**m):
        # trzeba policzyc ilosc 1 w reprezentacji binarnej liczby
        if policz_jedynki_binarne(i) == n:
            result += 1
            sol.append(i)
    return result, sol

result , sol = bramki(5, 7)
print(f'Jest dostepnych {result} rozwiazan')
for s in sol:
    print(f'{s:b}')

