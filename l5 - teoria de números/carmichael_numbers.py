def is_prime(n):
    a = [2, 3, 5, 170]
    for i in a:
        if not pow(i, n, n) == i:
            return False
    return True

def prime_sieve(n):
    size = n // 2
    sieve = [1] * size
    limit = int(n ** 0.5)

    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val::val] = [0] * tmp

    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

primes = set(prime_sieve(65000))

while True:
    n = int(input())

    if n == 0:
        break
    if (n not in primes) and is_prime(n):
        print(f"The number {n} is a Carmichael number.")
    else:
        print(f"{n} is normal.")
