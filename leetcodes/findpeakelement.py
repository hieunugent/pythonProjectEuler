class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        current = nums[0]
        index = 0
        for i, value in enumerate(nums):
            if value > current:
                current = value
                index = i
        return index
