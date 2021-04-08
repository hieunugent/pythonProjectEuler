def removeDuplicates(self, nums: List[int]) -> int:
    noDupNums = []
    length = 0
    for num in nums:
            if num not in noDupNums:
                noDupNums.append(num)
                nums[length] = num
                length += 1
    return length


def removeDuplicates2(self, nums: List[int]) -> int:
    if len(nums) == 0:
         return 0
    current = nums[0]
    length = 0
    for i in range(1, len(nums)):
        if nums[i] != current:
                length += 1
                nums[length] = nums[i]
                current = nums[i]
    return length+1
