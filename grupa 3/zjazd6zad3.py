# Proponuję Państwu napisanie programu, który rozwiązuje datowany na antyczny problem znany od nazwiska żydowskiego
# historyka z I wieku n.e. Józefa Flawiusza.
#
# 'N' żydowskich powstańców przeciwko Rzymskiemu Imperium zostało zagonionych w pułapkę. Nie chcąc popaść w niewolę
# powstańcy zadecydowali aby popełnić zbiorowe samobójstwo. Jednakże czyn samobójstwa jest szczególnie obrzydliwy
# w oczach Boga. Powstańcy zadecydowali aby stanąć w kole i zabijać kolejno co 'k' tego odliczonego powstańca,
# aż pozostanie ostatni - który jako jedyny popełni samobójstwo. Koło ma ustalony początek.
#
# Pomiędzy powstańcami jest jednak również Józek Flawiusz i jego przyjaciel, którzy nie chcą umierać i wolą się poddać.
# Na jakich dwóch miejscach w kole muszą stanąć, aby uniknąć śmierci z ręki pozostałych powstańców?
#
# Wymagania:
#
# Do rozwiązania zadania potrzebne są pętle, instrukcje warunkowe, oraz do wyboru: operator % działań modulo lub listy.
#
# N i k są parametrami wejściowymi. Program powinien zwrócić dwa numery miejsc [1,...N] które wypadną jako ostatnie
# w tej śmiertelnej odliczance.

# dwa warianty
# 1. faktycznie usuwamy obiekty z pamieci
# 2. mamy spis elementow ktore pozostaja aktywne na tej liscie

def jozef_flawiusz(N, k):
    # stworzyc odpowiednie struktury w pamieci
    lista = [i for i in range(1,N+1)]
    zywi = [True for _ in range(N)]
    # kolejnosc umierania
    kill_list = []
    ilosc_zywych = N
    indeks = 0
    i = 0
    while ilosc_zywych > 0:
        print(f'Iteracja {i}')
        i += 1
        print(lista)
        print(zywi)
        # wybrac nastepna osobe do zabicia
        odliczanie = k
        while odliczanie > 0:
            indeks += 1
            indeks %= N
            if zywi[indeks] == True:
                odliczanie -= 1
        # zabic osobe ktora zostala wskazana
        kill_list.append(lista[indeks])
        zywi[indeks] = False
        ilosc_zywych -= 1

    return kill_list
print(jozef_flawiusz(10, 2))

def jozef_flawiusz2(N, k):
    lista = [i for i in range(1,N+1)]
    kill = []
    lista.append(lista.pop(0)) # bo 1 nie ginie w pierwszym kroku
    while len(lista) > 0:
        print(lista)
        for _ in range(k-1):
            lista.append(lista.pop(0))
        kill.append(lista.pop(0))
    return kill

print(jozef_flawiusz2(10,2))
