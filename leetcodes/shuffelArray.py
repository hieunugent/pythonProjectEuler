class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = list(nums)
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.origin
        self.origin = list(self.origin)
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.nums)
        
        for i in range(len(self.nums)):
            remove_index = random.randrange(len(nums))
            self.nums[i] = nums.pop(remove_index)
            
        return self.nums
        