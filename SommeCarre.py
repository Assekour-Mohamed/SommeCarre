n = int(input("Enter a number: "))
s = 0
i = 0

while i <= n:
  if i % 2 != 0:
    s += i * i
  i += 1

print(s)
