def merge_the_tools(string, k):
    n = int(len(string)/k)
    u_strings = ["".join(dict.fromkeys(string[0+k*i:k+k*i])) for i in range(n)]
    for i in u_strings:
        print(i)
