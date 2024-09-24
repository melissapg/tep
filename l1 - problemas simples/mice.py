t = int(input())

results = []

for _ in range(t):
    n, k = map(int, input().strip().split())
    mice_positions = list(map(int, input().strip().split()))
    mice_positions.sort(reverse=True)
    
    saved_mice = 0
    cat_position = 0
    
    for mouse_position in mice_positions:
        if mouse_position > cat_position:
            saved_mice += 1
            cat_position += (n - mouse_position)
        else:
            break
    
    results.append(saved_mice)

for result in results:
    print(result)
