class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k
        

    def add(self, val: int) -> int:
        nums = self.nums
        nums.append(val)
        nums = sorted(nums, reverse = True)
        self.nums = nums
        k = self.k-1
        return nums[k]
