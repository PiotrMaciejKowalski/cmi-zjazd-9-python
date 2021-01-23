
a = int(input())
b = int(input())

ad = 0
for i in range(1, a):
  if a % i == 0:
    ad += i

bd = 0
for i in range(1, b):
  if b % i == 0:
    bd += i

if b == ad and a == bd:
  ans = True
else:
  ans = False

print(ans)
