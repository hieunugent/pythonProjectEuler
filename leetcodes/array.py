def twoSum(self, nums: List[int], target: int) -> List[int]:
        psi =[]
        for i, num in enumerate(nums):
            if num in psi:
                 for j in range(i):
                        if nums[j]== target-num:
                            return [j, i]
            psi.append(target-num)
        return[]