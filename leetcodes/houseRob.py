def rob(self, nums: List[int]) -> int:
    last = len(nums)-1
    if len(nums) < 2:
        if len(nums) == 1:
            return nums[0]
    for i in range (2, len(nums)):
        temp= 0
        if i-3 >=0:
            temp = nums[i]+nums[i-3]
        temp2 = nums[i] +nums[i-2]
        if temp2 > temp:
            nums[i] = temp2
        else:
            nums[i] = temp
        
    return nums[last] if nums[last] > nums[last-1] else nums[last-1]