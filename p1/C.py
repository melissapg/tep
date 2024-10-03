import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return sorted(divisors)


def get_lcm_cardinality(number):
    divisors = find_divisors(number)
    
    cardinality = 0
    for i in range(len(divisors)):
        for j in range(i, len(divisors)):
            a, b = divisors[i], divisors[j]
            if lcm(a, b) == number:
                cardinality += 1

    return cardinality


number = int(input())
while number != 0:
    lcm_cardinality = get_lcm_cardinality(number)
    print(number, lcm_cardinality)

    number = int(input())
