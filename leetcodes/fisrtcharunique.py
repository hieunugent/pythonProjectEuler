def firstUniqChar(self, s: str) -> int:
    setS = set(s)
    count = {}
    for ch in setS:
            count[ch] = 0
    for ch in s:
            count[ch] = int(count[ch]) + 1

    for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
    return -1
