
N = 100
k = 1000007

L = list(range(1, N+1))

i = 1 # krok iteracji
j = 0 # element listy

last, prev = -1, -1

while L: # dopoki lista nie jest pusta
  if i % k == 0: # usun element
    last, prev = L.pop(j), last
    #print(last)
  else: # lub przejdz dalej
    j += 1
    
  if j == len(L): # zawin liste w kolko
    j = 0
  
  i += 1 # podbij numer kroku

print(prev, last)
