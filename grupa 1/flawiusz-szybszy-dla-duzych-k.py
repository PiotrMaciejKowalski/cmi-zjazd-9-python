
N = 100
k = 1000007

L = list(range(1, N+1))

skip = k - 1
j = 0 # element listy

last, prev = -1, -1

while L: # dopoki lista nie jest pusta
  if j == len(L): # zawin liste w kolko
    j = 0
    skip = skip % len(L)
  if skip == 0: # usun element
    last, prev = L.pop(j), last
    skip = k - 1
    #print(last)
  else: # lub przejdz dalej
    j += 1
    skip -= 1

print(prev, last)
