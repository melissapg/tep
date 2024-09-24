import math

def prime_sieve(limit):
    is_not_prime = [False] * limit
    primes = []
    for candidate in range(2, limit):
        if not is_not_prime[candidate]:
            primes.append(candidate)
            for multiple in range(candidate * 2, limit, candidate):
                is_not_prime[multiple] = True
    return primes

def divides_factorial(factorial_n, divisor_m, primes):
    for prime in primes:
        if prime > divisor_m:
            break
        if divisor_m % prime == 0:
            prime_count_in_m = 0
            while divisor_m % prime == 0:
                prime_count_in_m += 1
                divisor_m //= prime
            prime_count_in_factorial = 0
            prime_power = prime
            while prime_power <= factorial_n:
                prime_count_in_factorial += factorial_n // prime_power
                prime_power *= prime
            if prime_count_in_factorial < prime_count_in_m:
                return False
    if divisor_m != 1 and factorial_n < divisor_m:
        return False
    return True

primes = prime_sieve(50000)

while True:
    try:
        factorial_n, divisor_m = map(int, input().split())
        if divides_factorial(factorial_n, divisor_m, primes):
            print(f"{divisor_m} divides {factorial_n}!")
        else:
            print(f"{divisor_m} does not divide {factorial_n}!")
    except EOFError:
        break
