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

def generatePermutations(elements):
    a = sorted(elements)
    all_perms = [a[:]]
    while nextPermutation1(a):
        all_perms.append(a[:])
    return all_perms

def main():
    elements = input("Enter elements separated by space: ").split()
    permutations = generatePermutations(elements)
    print("Permutations:")
    for perm in permutations:
        print(' '.join(perm))
    print(f"Total permutations: {len(permutations)}")

if __name__ == "__main__":
    main()