def lengthOfLongestSubstring(s):
        currentMax = 0
        for i in range(len(s)):
            result = []
            result.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in result:
                    result.append(s[j])
                else:
                    if len(result) > currentMax:
                        currentMax = len(result)
                    break
            if len(result) > currentMax:
                 currentMax = len(result)
        return currentMax