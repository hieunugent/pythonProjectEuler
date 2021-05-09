def maxSubArray(self, nums: List[int]) -> int:
    length = len(nums)
    numsleft = [0]*length
    numsleft[0] = nums[0]
    maxnum = nums[0]
    for i in range(1, len(nums)):
            temp = nums[i] + numsleft[i-1]
            if temp > nums[i]:
                numsleft[i] = temp
            else:
                numsleft[i] = nums[i]
            if maxnum < numsleft[i]:
                maxnum = numsleft[i]
    return maxnum
