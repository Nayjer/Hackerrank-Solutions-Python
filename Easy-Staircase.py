def staircase(n):
    lines = [""+" "*(n-i-1)+"#"*(i+1) for i in range(n)]
    return lines 
