
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


def are_amicable(a, b):
  return a == divisors_sum(b) and b == divisors_sum(a)


a = int(input())
b = int(input())

print(are_amicable(a, b))
