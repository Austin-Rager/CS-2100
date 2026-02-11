def nextPermutation1(a):
    n = len(a)
    j = n - 2
    while j >= 0 and a[j] >= a[j + 1]:
        j -= 1
    if j < 0:
        return False
    
    k = n - 1
    while a[j] >= a[k]:
        k -= 1

    a[j], a[k] = a[k], a[j]

    r = n - 1
    s = j + 1
    while r > s:
        a[r], a[s] = a[s], a[r]
        r -= 1
        s += 1

    return True

def next_r_combination(a, n):
    r = len(a)
    i = r - 1
    while i >= 0 and a[i] == n - r + i + 1:
        i -= 1
    if i < 0:
        return False
    a[i] += 1
    for j in range(i + 1, r):
        a[j] = a[j - 1] + 1
    return True

def generatePermutations(elements):
    a = sorted(elements)
    all_perms = [a[:]]
    while nextPermutation1(a):
        all_perms.append(a[:])
    return all_perms

def generateAllCombinations(n, r):
    if r > n or r < 0:
        return []
    
    a = list(range(1, r + 1))
    allCombinations = [a[:]]

    while next_r_combination(a, n):
        allCombinations.append(a[:])
    
    return allCombinations

def main():
    elements = input("Enter elements separated by space: ").split()
    permutations = generatePermutations(elements)
    print("Permutations:")
    for perm in permutations:
        print(' '.join(perm))
    print(f"Total permutations: {len(permutations)}")

    n = int(input("Enter n for combinations: "))
    r = int(input("Enter r for combinations: "))
    combinations = generateAllCombinations(n, r)
    print("Combinations:")
    for comb in combinations:
        print(' '.join(map(str, comb)))
    print(f"Total combinations: {len(combinations)}")

if __name__ == "__main__":
    main()