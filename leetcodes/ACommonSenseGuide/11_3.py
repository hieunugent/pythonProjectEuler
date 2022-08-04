def triangularNumber(n):
    if n == 1:
        return 1
    return n + triangularNumber(n-1)
print(triangularNumber(7))