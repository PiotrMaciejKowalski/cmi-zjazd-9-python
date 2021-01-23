# W pewnej firmie informatycznej ze względu na epidemię  SARS-CoV-2 zespół projektowy podzielony został na dwie sekcje.
# Członkowie pierwszej sekcji spotykają się w siedzibie firmy co x dni, a członkowie drugiej sekcji co y dni.
# Po ilu dniach spotkają się w firmie oba zespoły.

def spotkania_sekcji(x, y):
    day = 0
    while True:
        print("!")
        day += x
        if day % y == 0: #dochodzi do spotkania obu sekcji
            break
    return day

# wynik = spotkania_sekcji(6,4)
# print(f'Do spotkania obu grup dojdzie w dniu {wynik}')

wynik = spotkania_sekcji(12,15)
print(f'Do spotkania obu grup dojdzie w dniu {wynik}')

# czy dałoby przyśpieszyć (zoptymalizować) działanie tego programu ?
# mamy liczby x, y , czego szukamy? i problemem nwd? nww

# niech d = nwd(x,y)
# istnieja wtedy a,b takie, że
# x = d * a
# y = d * b
# nww(x,y) = d*a*b = x * b

def nwd(x,y): #implementacja algorytmu euklidesa
    licznik = x if x >y else y
    dzielnik = y if x>y else x
    reszta = licznik % dzielnik
    while reszta > 0:
        print('@')
        licznik, dzielnik = dzielnik, reszta
        reszta = licznik % dzielnik
    return dzielnik

def spotkania_sekcji_nwd(x,y):
    d = nwd(x,y)
    b = y //d
    return x*b

# wynik = spotkania_sekcji_nwd(6,4)
# print(f'Do spotkania obu grup dojdzie w dniu {wynik}')

wynik = spotkania_sekcji_nwd(12,15)
print(f'Do spotkania obu grup dojdzie w dniu {wynik}')