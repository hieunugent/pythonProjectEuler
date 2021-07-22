class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(s, result):
            if len(s) == 0:
                results.append(result)
                return
            for i in range(len(s)):
                f = s[i]
                left = s[0:i]
                right = s[i+1:]
                rest = left + right
                backtrack(rest, result+[f])
        result = []
        backtrack(nums, result)
        return results
   