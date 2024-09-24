n_tests = int(input())

final_output = []

for _ in range(n_tests):
    votes = list(map(int, input().split()))
    a, b, c = votes
    
    votes_needed_a = max(0, max(b, c) - a + 1)
    votes_needed_b = max(0, max(a, c) - b + 1)
    votes_needed_c = max(0, max(a, b) - c + 1)
    
    final_output.append((votes_needed_a, votes_needed_b, votes_needed_c))

for i in final_output:
    print(' '.join(map(str, i)))
