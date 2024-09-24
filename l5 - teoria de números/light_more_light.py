import math

while True:
  m = int(input())
  if m !=0:
    if math.isqrt(m)**2 == m:
      print('yes')
    else:
      print('no')
  else:
    break
