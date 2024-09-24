from math import floor

test_cases = int(input())

for _ in range(0, test_cases):
    l, r = list(map(int, input().split()))

    result = 0
    while l!=0 or r!=0:
        result += r-l
        l = int(floor(l/10))
        r = int(floor(r/10))

    print(result)
