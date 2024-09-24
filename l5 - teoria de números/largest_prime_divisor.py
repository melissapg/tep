def largestPrimeDivisor(n):
    n = abs(n)  
    prime_divisor = -1
    prime_count = 0
    i = 2

    while i * i <= n:
        while n % i == 0:
            if i != prime_divisor:
                prime_divisor = i
                prime_count += 1
            n //= i  
        i += 1

    if n > 1:  
        prime_divisor = n
        prime_count += 1

    return int(prime_divisor) if prime_count > 1 else -1

numbers = []
n = int(input())

while n != 0:
    numbers.append(n)
    n = int(input())

for number in numbers:
    print(largestPrimeDivisor(number))
