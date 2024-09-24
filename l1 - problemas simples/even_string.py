num_cases = int(input())
results = []

for _ in range(num_cases):
    text = input().strip()
    seen_chars = set()
    removed_chars = 0
    
    for char in text:
        if char in seen_chars:
            removed_chars += 2
            seen_chars.clear()
        else:
            seen_chars.add(char)
    
    remaining_chars = len(text) - removed_chars
    results.append(remaining_chars)

for result in results:
    print(result)
