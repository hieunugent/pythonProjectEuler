def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]
A ="12345"
print(A[0:3]=="123")


def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0:
            return 0

    n = len(haystack)
    for i in range(n):
        temp = haystack[i:i+len(needle)]
        if temp == needle:
            return i
    return -1
