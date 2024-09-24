t = int(input())
results = []

for _ in range(t):
    s = input().strip()
    total_0 = s.count('0')
    total_1 = s.count('1')
    
    current_0 = 0
    current_1 = 0
    max_removed = 0
    
    for char in s:
        if char == '0':
            current_0 += 1
        else:
            current_1 += 1
        if current_0 < current_1:
            max_removed = max(max_removed, current_0)
        elif current_1 < current_0:
            max_removed = max(max_removed, current_1)
    
    results.append(max_removed)

for result in results:
    print(result)
