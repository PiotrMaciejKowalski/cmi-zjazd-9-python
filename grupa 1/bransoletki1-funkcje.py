
def divisors_sum(a):
  ad = 0
  for i in range(1, a):
    if a % i == 0:
      ad += i
  return ad


def are_amicable(a, b):
  return a == divisors_sum(b) and b == divisors_sum(a)


a = int(input())
b = int(input())

print(are_amicable(a, b))
