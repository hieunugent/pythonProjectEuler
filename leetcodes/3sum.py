def threeSum(self, nums: List[int]) -> List[List[int]]:
     result = []
     for i in range (len(nums)):
          currenttarget = 0 -nums[i]
          existnum = {}
          
