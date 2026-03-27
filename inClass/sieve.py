def sieve(size):
    array = [True] * size
    array[0] = False
    array[1] = False

    i = 2
    while i * i < size:
        if array[i]:
            for j in range(i * i, size, i):
                array[j] = False
        i += 1

    return array

primes = sieve(50)
print([i for i, is_prime in enumerate(primes) if is_prime])
