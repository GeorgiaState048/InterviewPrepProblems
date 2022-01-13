def countWays(n):
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2
    print(res)
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        print(res)
    print("-----------------------------")
    return res


# Driver code
n = 4
print(countWays(n))