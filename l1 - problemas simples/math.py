n = int(input())

if n == 0:
    print(4)
else:
    print((
           1 +
           2**((n - 1) % 4 + 1) + 
           3**((n - 1) % 4 + 1) + 
           4**((n - 1) % 2 + 1)) % 5)
