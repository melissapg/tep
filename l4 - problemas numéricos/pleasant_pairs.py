test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))

    pairs = [None] * ((2*n)+1)
    for i in range(n):
        pairs[a[i]] = i + 1

    result = 0
    for i in range(1, (2*n)+1):
        for j in range(i+1, ((2*n) // i) + 1):
            if pairs[i] != None and pairs[j] != None:
                if (pairs[i] + pairs[j]) == i*j:
                    result += 1

    print(result)
