def getMinimumCost(k, c):
    c.sort()
    c.reverse() 
    splitted_lists = [sum(c[i*k:i*k+k]) for i in range(n-k+1)]
    SUM = 0
    for i in range(0, len(splitted_lists)):
        SUM += splitted_lists[i]*(i+1)
    return SUM
