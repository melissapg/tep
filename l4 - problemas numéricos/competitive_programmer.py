def is_red(number):
    digits = list(map(int, number))
    sum_digits = sum(digits)
    has_zero = digits.count(0) > 0
    even_count = sum(1 for d in digits if d % 2 == 0)

    # To be divisible by 60, we need at least one 0,
    # the sum of digits must be divisible by 3, 
    # and there should be at least two even digits (one of them being 0).
    if has_zero and sum_digits % 3 == 0 and even_count >= 2:
        return "red"
    else:
        return "cyan"

n = int(input())  # number of grandmasters
for _ in range(n):
    y_i = input().strip()
    print(is_red(y_i))
