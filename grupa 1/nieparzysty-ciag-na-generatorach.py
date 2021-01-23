
#input()

target = 1
result = 0
n = 0

for x in map(int, input().split()):
  if x != target:
    result += 1
  else:
    target += 2
  n += 1

if result == n:
  print('Błędny ciąg')
else:
  print(result)
