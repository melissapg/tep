n_tests = int(input())
results = []

for _ in range(n_tests):
    n = input()
    length = len(n)
    min_steps = len(n)
    
    for i in range(length):
        for j in range(i + 1, length):
            if (n[i] + n[j]) in ['00', '25', '50', '75']:
                steps = (length - j - 1) + (j - i - 1)
                min_steps = min(min_steps, steps)
    
    results.append(min_steps)

for result in results:
    print(result)
