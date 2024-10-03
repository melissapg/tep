def minimum_movements_between_strings(phrase, original_phrase):
    min_moves = 0
    one_diff = 0
    zero_to_one = 0
    one_to_zero = 0

    for i in range(len(phrase)):
        if phrase[i] != original_phrase[i]:
            min_moves += 1
        if phrase[i] == '?' and original_phrase[i] == '1':
            one_diff -= 1
        elif phrase[i] == '0' and original_phrase[i] == '1':
            zero_to_one += 1
            one_diff -= 1
        elif phrase[i] == '1' and original_phrase[i] == '0':
            one_to_zero += 1
            one_diff += 1

    # não há como fazer mudanças
    if (one_diff > 0):
        return -1
    
    # retorna os movimentos minimos para se chegar no resultado
    return (min_moves - min(one_to_zero, zero_to_one))


for i in range(int(input())):
    phrase = str(input())
    original_phrase = str(input())

    print(f"Case {i+1}: {minimum_movements_between_strings(phrase, original_phrase)}")
