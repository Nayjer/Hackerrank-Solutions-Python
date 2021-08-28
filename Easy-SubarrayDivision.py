def birthday(s, d, m):
    squares = [1 for i in range(n-(m-2)) if sum(s[i:i+m]) == d]
    return sum(squares)
