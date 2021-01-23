
n = int(input())
A = list(map(int, input().split()))

#print('n =', n)
#print('A =', A)

target = 1
result = 0

for x in A:
  if x != target:
    result += 1
  else:
    target += 2

if result == n:
  print('Błędny ciąg')
else:
  print(result)
