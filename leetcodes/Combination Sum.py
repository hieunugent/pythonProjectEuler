class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.findNumbers(res, candidates, [], target, 0)
        print(candidates)
        

        return res
    def findNumbers(self, ans, arr, temp, sum, index):
        if sum == 0:
            ans.append(temp)
            return
        for i in range(index, len(arr)):
            if sum - arr[i] >= 0:
                self.findNumbers(ans, arr, temp + [arr[i]], sum - arr[i], i)
            else:
                break


combinationsum = Solution()
print(combinationsum.combinationSum([2,3,6,7], 7))

