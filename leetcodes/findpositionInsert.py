class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        found = -1
        while left <= right:
            pivot = (right-left)//2 + left
            if target > nums[pivot]:
                left = pivot + 1
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                return pivot
        return left
