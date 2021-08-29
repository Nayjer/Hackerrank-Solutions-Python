def maxMin(k, arr):
    arr.sort()
    unfairnesses = []
    for u in range(n-k+1):
        unfairnesses.append(arr[u+k-1]-arr[u])
    return min(unfairnesses)
