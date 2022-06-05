class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearchIndex(nums, target):
            right = len(nums)-1
            left = 0
            while left<= right:
                pivot = (left+right)//2
                if nums[pivot] > target:
                     right = pivot -1
                elif nums[pivot]< target:
                    left = pivot+1
                else:
                    return pivot
            return -1
        def theMinPosible(nums, target):
            right = len(nums)-1
            left = 0
            while left <= right:
                pivot = (left+right)//2
                if nums[pivot] <target:
                    if pivot+1 <len(nums) and nums[pivot+1] > target:
                        return pivot+1
                    elif pivot+1 >=len(nums):
                        return pivot+1
                    else:
                        left = pivot+1
                elif nums[pivot] >target:
                    right = pivot-1
            return -1
        def firstGreaterTarget(nums, target):
            right = len(nums)-1
            left = 0
            while right > left:
                center = (right+left)//2
                if nums[center] < target and nums[center+ 1] > target:
                    return center + 1
                elif nums[center] > target:
                    right = center
                elif nums[center] < target and nums[center+1] < target:
                    left = center +1
                    
        if nums[0]>target:
            return 0
        elif nums[len(nums)-1] < target:
            return len(nums)
        elif binarySearchIndex(nums, target) >=0:
            return binarySearchIndex(nums, target)
        else:
            return firstGreaterTarget(nums, target)
