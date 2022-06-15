class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            def matches(s1map, s2map):
                for i in range(26):
                    if s1map[i] != s2map[i]:
                        return False
                return True
            if len(s1) > len(s2):
                return False
            s1map = [0]*26
            s2map = [0]*26
            for i in range(len(s1)):
                s1map[ord(s1[i])-ord('a')] += 1
                s2map[ord(s2[i])-ord('a')] += 1
            for i in range(len(s2) - len(s1)):
                if (matches(s1map, s2map)):
                    return True
                s2map[ord(s2[i + len(s1)]) - ord('a')] += 1
                s2map[ord(s2[i])  - ord('a')] -= 1
            return matches(s1map, s2map)
