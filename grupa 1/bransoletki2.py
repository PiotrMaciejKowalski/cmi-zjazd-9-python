
def divisors_sum(a):
  ad = 1
  i = 2
  while i*i < a:
    if a % i == 0:
      ad += i
      ad += a // i
    i += 1
  if i*i == a:
    ad += i
  return ad


def find_amicable(a):
  b = divisors_sum(a)
  if a == divisors_sum(b):
    return b
  else:
    return 0


results = []

for a in range(2, 100001):
  b = find_amicable(a)
  if b != 0:
    results.append((a, b))


test = """1184 i 1210
2620 i 2924
5020 i 5564
6232 i 6368
10744 i 10856
12285 i 14595
17296 i 18416
63020 i 76084
66928 i 66992
67095 i 71145
69615 i 87633"""

for line in test.split('\n'):
  w = line.split()
  a, b = int(w[0]), int(w[2])
  results.index((a, b))

print('Wypisanie tej linii oznacza powodzenie testu.')
