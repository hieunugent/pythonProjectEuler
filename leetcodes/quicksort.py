from typing import List


def quicksort(nums: List[int]) -> List[int]:
    def quicksortP(nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []  
        if len(nums)==1:
            return nums
        for i in range(len(nums)-1):
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        leftLen = len(left)
        rightlen = len(right)
        print("left")
        print(left)
        print("pivot")
        print(pivot)
        print("right")
        print(right)
        print("/n")
        if leftLen == 0 :
            return [pivot] + quicksortP(right, right[rightlen-1])
        if rightlen == 0:
            return  quicksortP(left, left[leftLen-1]) + [pivot]
        return quicksortP(left, left[leftLen-1]) + [pivot] + quicksortP(right, right[rightlen-1])
    end = nums[len(nums)-1]
    return quicksortP(nums, end)

A = [0,9,8,7,6,1,4,3,2,5]
print(quicksort(A))
