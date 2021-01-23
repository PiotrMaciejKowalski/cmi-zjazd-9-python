# Liczby a, b są zaprzyjaźnione gdy suma dzielników właściwych liczby a jest równa liczbie b a suma dzielników właściwych
# liczby b jest równa liczbie a. Dzielnik właściwy liczby to każdy jej dzielnik mniejszy od tej liczby.
# Przykład:
# Przykładem pary najmniejszych liczb zaprzyjaźnionych są liczby 220 i 284.
# Dzielniki właściwe liczby 220 to 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
# więc suma dzielników 220 wynosi 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
# Dzielniki właściwe liczby 284 to 1, 2, 4, 71, 142,
# więc suma dzielników 284 wynosi 1 + 2 + 4 + 71 + 142 = 220
#
#     Starożytni Grecy wierzyli, że bransoletki z wygrawerowanymi liczbami zaprzyjaźnionymi zapewniają szczęście w miłości.
# Znalezienie liczb zaprzyjaźnionych nie jest bardzo prostym zadaniem. Wyobraź sobie, że przenosisz się ze swoim laptopem
# (oczywiście masz naładowany akumulator) do Świata Antycznego. Pomóż swojemu przyjacielowi Grawerixowi w przygotowaniu
# nowych bransoletek przyjaźni ponieważ klienci nie chcą już kupować tych z nadrukiem „220,284”.
#
# Zadanie 1 (łatwiejsze)
#     Napisz funkcję która pobiera dwie liczby i zwraca wartość prawda (true) gdy podane na wejściu liczby są
# zaprzyjaźnione, luba fałsz (false) w przeciwnym wypadku. Napisz program testujący tę funkcję. Jeśli nie znasz funkcji
# napisz program bez użycia funkcji.

def czy_zaprzyjaznione(x , y):

    # znajdz dzielniki x
    dzielniki_x = []
    for i in range(1,x):
        if x % i == 0:
            dzielniki_x.append(i)
    # znajdz sume dzielnikow
    suma_dzielnikow_x = 0
    for dzielnik in dzielniki_x:
        suma_dzielnikow_x += dzielnik

    if suma_dzielnikow_x != y:
        return False

    #znalezc dzielniki y
    dzielnik_y = []
    for i in range(1,y):
        if y % i == 0:
            dzielnik_y.append(i)

    suma_dzielnikow_y = 0
    for dzielnik in dzielnik_y:
        suma_dzielnikow_y += dzielnik

    if suma_dzielnikow_y != x:
        return False

    return True

print(czy_zaprzyjaznione(1184, 1210))
import math

def znajdz_dzielniki(x):
    #uwazac na pierwiastek oraz na pare dzielnika od 1

    dzielniki_x = [1]
    p = 2
    while p*p < x:
        if x % p == 0: # p jest dzielnikiem liczby x
            dzielniki_x.append(p)
            dzielniki_x.append(x // p)
        p += 1
    if p*p == x:
        dzielniki_x.append(p)
    return dzielniki_x


    # for i in range(1, x):  # [1..sqrt(x)] ale ona będzie posiadała swojego dzielnika bliźniaka x = i * j i=1 -> j = 220
    #     if x % i == 0:
    #         dzielniki_x.append(i)
    # return sorted(dzielniki_x)

def sumuj_liczby(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma

# dzielnikow liczby 36, 6 ; 36 = 6*6

def czy_zaprzyjaznione_opt(x , y):
    dzielniki_x = znajdz_dzielniki(x)
    suma_dzielnikow_x = sumuj_liczby(dzielniki_x)
    if suma_dzielnikow_x != y:
        return False
    dzielniki_y = znajdz_dzielniki(y)
    suma_dzielnikow_y = sumuj_liczby(dzielniki_y)
    if suma_dzielnikow_y != x:
        return False
    return True

print(czy_zaprzyjaznione_opt(1184, 1210))

print(znajdz_dzielniki(36))