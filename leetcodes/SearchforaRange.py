class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        for i, value in enumerate(nums):
            if value == target and start == -1:
                start = i
                end = i
            elif value == target and start != -1:
                end = i
        return [start, end]
