def removeElement(self, nums: List[int], val: int) -> int:
       last = len(nums)-1
       while last >= 0:
            if nums[last] != val:
                break
            last -= 1

       for i in range(len(nums)):
            if last < i:
                break
            if nums[i] == val:
                if nums[last] != val:
                    nums[i], nums[last] = nums[last], nums[i]
                    last -= 1
                while last >= 0:
                    if nums[last] != val:
                        break
                    last -= 1

       return last+1
