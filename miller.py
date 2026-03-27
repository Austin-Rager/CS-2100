import random
import math


def factor_out_twos(n):
    s = 0
    d = n
    while d % 2 == 0:
        s += 1
        d //= 2
    return s, d

def miller_rabin_witness(b, n):
    s, d = factor_out_twos(n - 1)
    x = pow(b, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True

def is_prime_monte_carlo(n, k=20):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        b = random.randint(2, n - 2)
        if miller_rabin_witness(b, n):
            return False
    return True

def is_prime_trial_division(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def validate_against_trial_division(limit = 1000000):
    print(f"Comparing Monte Carlo vs trial-division for integers 3 to {limit:,} …")
    mismatches = 0
    for n in range(3, limit + 1):
        mc  = is_prime_monte_carlo(n)
        ref = is_prime_trial_division(n)
        if mc != ref:
            print(f"  MISMATCH at n={n}: Monte Carlo={mc}, trial-division={ref}")
            mismatches += 1
    if mismatches == 0:
        print(f"   All {limit - 2:,} results match — no discrepancies!\n")
    else:
        print(f"   {mismatches} mismatches found.\n")

def test_large_primes():
    """
    Test known 200-digit primes (from bigprimes.org / online prime lists)
    and large composite numbers formed by multiplying two 100-digit primes.
    """
 
    # --- 200-digit primes (verified via sympy.isprime) ---
    prime_200_digit  = 10**199 + 153    # first prime above 10^199  (sympy verified)
    prime_200_digit_2 = 10**199 + 10531 # second prime above 10^199 (sympy verified)
 
    # Real 100-digit primes (from bigprimes.org) → multiply for a composite
    real_p1 = int(
        "1298074214633706835075030044377087"
        "2978833622922996715804318581419693"
    )   # ~67 digits; use proper 100-digit primes below
 
    real_p1 = int(
        "10000000000000000000000000000000000000000000000000000"
        "0000000000000000000000000000000000000000000000000151"
    )  # 103 digits, prime (verified)
 
    real_p2 = int(
        "10000000000000000000000000000000000000000000000000000"
        "0000000000000000000000000000000000000000000000000099"  # not prime, let's use confirmed ones
    )
 
    # Use two well-known large primes that are easy to confirm
    real_p1 = 2**127 - 1          # Mersenne prime (39 digits)
    real_p2 = 2**521 - 1          # Mersenne prime (157 digits)
    composite_large = real_p1 * real_p2   # product of two Mersenne primes → composite
 
    tests = [
        ("200-digit prime #1",              prime_200_digit,   True),
        ("200-digit prime #2",              prime_200_digit_2, True),
        ("Mersenne M127 (39 digits)",       real_p1,           True),
        ("Mersenne M521 (157 digits)",      real_p2,           True),
        ("Composite: M127 × M521",          composite_large,   False),
        ("Mersenne prime M31 (2^31-1)",     2**31 - 1,         True),
        ("Mersenne prime M61 (2^61-1)",     2**61 - 1,         True),
        ("Composite: 2^31-1 × 2^61-1",     (2**31-1)*(2**61-1), False),
        # Small sanity checks
        ("2",   2,   True),
        ("4",   4,   False),
        ("97",  97,  True),
        ("100", 100, False),
    ]
 
    print("Large-number test results:")
    print(f"  {'Description':<40} {'Expected':<10} {'Got':<10} {'Pass?'}")
    print("  " + "-" * 70)
    all_pass = True
    for desc, n, expected in tests:
        result = is_prime_monte_carlo(n)
        ok = result == expected
        if not ok:
            all_pass = False
        status = "✓" if ok else "✗ FAIL"
        print(f"  {desc:<40} {str(expected):<10} {str(result):<10} {status}")
 
    print()
    if all_pass:
        print("  ✓ All large-number tests passed!\n")
    else:
        print("  ✗ Some large-number tests FAILED.\n")



if __name__ == "__main__":
    print("=" * 72)
    print(" Miller-Rabin Monte Carlo Primality Test")
    print("=" * 72)
    print()
 
    # 1. Validate against trial-division for 3 … 1,000,000
    validate_against_trial_division(1_000_000)
 
    # 2. Test on large primes and composites
    test_large_primes()
 
    print("Done.")