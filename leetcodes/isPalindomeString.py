print('a' <= 'z' and 'a'>= 'a')

new ="a"
new +="x"
print(new)


def isPalindrome(self, s: str) -> bool:
    s = s.lower()

    def removeextra(s):
            new = ''
            for c in s:
                if c >= 'a' and c <= 'z' or (c >= '0' and c <= '9'):
                    new = new + c
            return new

    def isPalindromecheck(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
    s = removeextra(s)

    return isPalindromecheck(s)
