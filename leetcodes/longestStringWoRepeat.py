def lengthOfLongestSubstring(self, s: str) -> int:
        longStr = 0:
        for i in range(len(s)-1):
            if s.charAt(i) != s.charAt(i-1):
                longStr +=1
            