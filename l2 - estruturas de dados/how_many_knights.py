results = []

while True:
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    
    if n == 0 and m == 0:
        break
    
    if n < m:
        n, m = m, n  ,
    
    if m == 1:
        ans = n
    elif m == 2:
        ans = 2 * (n // 4 * 2 + min(n % 4, 2))
    else:
        ans = (n * m + 1) // 2
    
    results.append(f"{ans} knights may be placed on a {inp[0]} row {inp[1]} column board.")

for result in results:
    print(result)
