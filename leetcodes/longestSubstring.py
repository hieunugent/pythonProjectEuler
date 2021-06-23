class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def firstappear(strs, c):
            res = 0
            for i, l in enumerate(strs):
                if l == c:
                    res = i
                    break
            return res
        maxlength = 0
        stack = []
        for c in s:
            if c not in stack:
                stack.append(c)
            else:
                if len(stack) > maxlength:
                    maxlength = len(stack)
                n = firstappear(stack, c)+1
                stack = stack[n:]
                stack.append(c)
        if len(stack) > maxlength:
            maxlength = len(stack)

        return maxlength
