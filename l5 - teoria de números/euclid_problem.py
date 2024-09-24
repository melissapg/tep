def euclid(a, b):
  if b == 0:
    return 1, 0, a
  x1, y1, d = euclid(b, a % b)
  x = y1
  y = x1 - (a // b) * y1
  return x, y, d

while True:
  try:
    a, b = map(int, input().split())
    x, y, d = euclid(a, b)
    print(x, y, d)
  except EOFError:
    break
