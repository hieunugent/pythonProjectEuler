def rotate(nums, k):
    n =  len(nums)
    k %=n
    start= count = 0
    while count < n:
        current , prev = start, nums[start]
        while True:
            next_idx = (current+k)%n
            nums[next_idx] , prev= prev, nums[next_idx]
            current = next_idx
            count +=1
            if start == current:
                break
        start+=1

def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
