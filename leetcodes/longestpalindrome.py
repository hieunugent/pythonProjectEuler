def longestPalindrome(self, s: str) -> str:
       def expandaroundcenter(s, left, right):
            L = left
            R = right
            while L >= 0 and R < len(s) and s[R] == s[L]:
                L -= 1
                R += 1
            return R-L-1
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expandaroundcenter(s, i , i + 1)
            len2 = expandaroundcenter(s, i, i )
            lenmax = max(len1, len2)
            if lenmax > end - start:
                start = i - (lenmax-1)//2
                end = i + lenmax//2
        return s[start:end+1]