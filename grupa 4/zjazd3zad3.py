# Użytkownik podaje liczbę naturalną dodatnią - n.
#
# Proszę napisać program, który sprawdzi czy dana liczba n jest kwadratem innej liczby naturalnej p, takiej że p*p==n.
# W wyniku działania program powinien wypisać liczbę p lub komunikat: "Nie istnieje".

def czy_kwadrat(n):

    if n <=0 :
        return 'Nie istnieje'

    p = 1
    while p*p <= n: #ograniczenie naszych poszukiwan
        if p*p == n:
            return p
        p += 1
    else:
        return 'Nie istnieje'

print(czy_kwadrat(25))

print(czy_kwadrat(26))

n = int(input('Podaj n\n>'))
print(czy_kwadrat(n))