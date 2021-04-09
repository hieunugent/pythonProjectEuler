def sortArrayByParity(self, A: List[int]) -> List[int]:
    fistodd = 0
    lasteven = len(A)-1
    for num in A:
        if num % 2 == 0:
            fistodd += 1
        else:
            break
    for num in A[::-1]:
        if num % 2 == 0:
             break
        lasteven -= 1

    while fistodd < lasteven:
        if A[fistodd] %2 != 0 and A[lasteven]%2 == 0:
                A[fistodd], A[lasteven] = A[lasteven], A[fistodd]
                fistodd += 1
                lasteven -= 1
        elif A[lasteven] % 2 != 0:
                lasteven -= 1
        elif A[fistodd] % 2 == 0:
                fistodd += 1
    return A
