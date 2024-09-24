t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort()
    if n == 1:
        if a[0] > 1:
            results.append("NO")
        else:
            results.append("YES")
        continue
    if a[-2] + 1 < a[-1]:
        results.append("NO")
    else:
        results.append("YES")

for result in results:
    print(result)
