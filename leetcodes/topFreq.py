class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def findtopKth(store):
                result = []
                return result

        nums = sorted(nums)

        store = {}
        i = 0
        while i < len(nums):
                curr = nums[i]
                count = 1
                if i == len(nums)-1:
                    store[curr] = count
                for j in range(i+1, len(nums)):
                    if nums[j] == curr:
                        count += 1
                    store[curr] = count
                i = i + count
        return findtopKth(store)
