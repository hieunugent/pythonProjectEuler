class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '{':'}',
            '[':']',
            '(':')'
        }
        for i in s:
            if i in valid:
                stack.append(valid[i])
            elif not stack:
                stack.append('#')
            elif  stack.pop()!= i:
                return False
        return not stack