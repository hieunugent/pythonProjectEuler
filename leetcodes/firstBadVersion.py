class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1 and isBadVersion(1):
        #     return n

        start = 0
        end = n-1
        found = n
        while start <= end:
            mid = (end - start)//2 + start
            if isBadVersion(mid):
                if found > mid:
                    found = mid
                end = mid-1
            else:
                start = mid+1
        return found
