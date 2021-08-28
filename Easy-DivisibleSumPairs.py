def divisibleSumPairs(n, k, ar):
    pairs = [(i,j) for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j]) % k == 0]
    return len(pairs)
