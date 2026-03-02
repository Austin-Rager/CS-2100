import random

def combinations(items, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(items)):
        for c in combinations(items[i+1:], n-1):
            result.append([items[i]] + c)
    return result

def combinations_repetition(items, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(items)):
        for c in combinations_repetition(items[i:], n-1):
            result.append([items[i]] + c)
    return result

def permutations(items, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(items)):
        remaining = items[:i] + items[i+1:]
        for p in permutations(remaining, n-1):
            result.append([items[i]] + p)
    return result

def permutations_repetition(items, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(len(items)):
        for p in permutations_repetition(items, n-1):
            result.append([items[i]] + p)
    return result

items = [1, 2, 3, 4, 5]

print(f"C(5,3) — {len(combinations(items, 3))} combinations:\n")
for c in combinations(items, 3):
    print(c)

print(f"CR(5,3) — {len(combinations_repetition(items, 3))} combinations with repetition:\n")
for c in combinations_repetition(items, 3):
    print(c)

print(f"P(5,3) — {len(permutations(items, 3))} permutations:\n")
for p in permutations(items, 3):
    print(p)

print(f"PR(5,3) — {len(permutations_repetition(items, 3))} permutations with repetition:")
for p in permutations_repetition(items, 3):
    print(p)