  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not len(strs):
            return ""
    word = strs[0]
    for w in strs:
        if len(word) > len(w):
                word = w

    for current in strs:
            temp = ""
            for i in range(len(word)):
                if word[i] != current[i]:
                    break
                temp += word[i]
            if len(temp) == 0:
                return temp
            if len(temp) < len(word):
                word = temp
    return word
