def hammingWeight(self, n: int) -> int:
    sum = 0
    while n != 0:
            sum += 1
            n = n & (n-1)
    return sum
print(hammingWeight(10))  