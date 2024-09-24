test_cases = int(input())

for _ in range(test_cases):
    n = int(input())

    x = ((n * (n-1) * (n-2) * (n-3))// 24) + n
    y = (4 * (x-n) + n * (n+1))//2
    print(y - x + 1)
