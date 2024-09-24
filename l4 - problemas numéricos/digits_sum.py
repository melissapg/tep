tests_cases = int(input())

interesting = []
for i in range(tests_cases):
    n = int(input()) + 1
    
    max_interesting = n // 10
    
    interesting.append(0)
    interesting[i] = max_interesting

for i in interesting:
    print(i)
