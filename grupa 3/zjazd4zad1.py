# W pewnej firmie informatycznej ze względu na epidemię  SARS-CoV-2 zespół projektowy podzielony został na dwie sekcje.
# Członkowie pierwszej sekcji spotykają się w siedzibie firmy co x dni, a członkowie drugiej sekcji co y dni.
#
# Po ilu dniach spotkają się w firmie oba zespoły.

def spotkanie_sekcji(x, y):
    day = 0
    while True:
        print('!')
        day += x
        if day % y == 0:
            break
    return day
dni = spotkanie_sekcji(12,150)
print(f'Spotkanie sekcji odbyło się po {dni} dniach')

# Czy umiałbym rozwiązać to zadanie w sposób szybszy?

# algorytm euklidesa -> najwiekszy wspolny dzielnik -> nwd

# czego naprawde poszukujemy dla liczb x oraz y - najmniejsza wspolna wielokrotnosc - nww

# jesli mamy x oraz y i oznaczymy sobie d = nwd(x,y)
# to istniec musza liczby a,b takie ze
# x = d * a
# y = d * b
# wspolne wielokrotnosc liczb x i y , to x*y
# liczba ktora bylaby wspolna wielokrotnosc liczb x oraz y jest d*a*b

def nwd(x, y): # algorytm euklidesa
    licznik = x if x > y else y
    dzielnik = y if x>y else x
    reszta = licznik % dzielnik
    while reszta > 0:
        print('@')
        licznik, dzielnik = dzielnik, reszta
        reszta = licznik % dzielnik
    return dzielnik

def spotkanie_sekcji_opt(x, y):
    d = nwd(x, y)
    a = x // d
    b = y // d
    return d*a*b
dni = spotkanie_sekcji_opt(12,150)
print(f'Spotkanie sekcji odbyło się po {dni} dniach')