class Solution:
    def getLucky(self, s: str, k: int) -> int:
        timetransform = 0

        def convertStrToInt(s):
            nums = []
            for c in s:
                code = ord(c) - ord('a') + 1
                if code > 9:
                    temp1 = code//10
                    temp2 = code % 10
                    nums.append(temp1)
                    nums.append(temp2)
                else:
                    nums.append(code)
            return nums
        nums = convertStrToInt(s)

        def dotranform(nums):
            nonlocal result
            result = 0
            for i in nums:
                result += i
#             break the result to the nums array
            temp = []
            tempnum = result
            while tempnum > 0:
                i = tempnum % 10
                tempnum = tempnum//10
                temp.append(i)
            nums = temp
            return nums
        result = 0
        while timetransform < k:
            nums = dotranform(nums)
            timetransform += 1
        return result
