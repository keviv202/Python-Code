def countPrimes(n):
    if n < 3:
        return 0
    "Return all primes <= n."
    # np1 = n + 1
    s = [True] * n
    s[0] = s[1] = False
    sqrtn = int(round(n ** 0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i * i: n: i] = False * len(range(i * i, n, i))
    return s.count(True)


countPrimes(9)
