def firstBadVersion(self, n):
    def findfirstbad(start, end):
            mid = (end-start)//2 + start
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                return findfirstbad(start, mid)
            else:
                return findfirstbad(mid, end)

    return findfirstbad(0, n+1)
def isBadVersion(num):
    A = [False, False, False, False, False, False, True, True, True]
    return A[num]
    