class Solution:
   def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*len(nums)
        maxNum = 1
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and LIS[i] < LIS[j]+1:
                    LIS[i] = LIS[j]+1
                    if maxNum <= LIS[i]:
                        maxNum = LIS[i]
        return maxNum
        
     