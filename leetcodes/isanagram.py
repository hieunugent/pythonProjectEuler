def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    setS = set(s)
    setT = set(t)
    dict1 = {}
    dict2 = {}
    for ch1 in setS:
        dict1[ch1] = 0
    for ch in s:
        num = int(dict1[ch])+1
        dict1[ch] = num

    for ch in t:
        if ch not in dict1:
            return False
        if int(dict1[ch]) <= 0:
            return False
        num = int(dict1[ch])-1
        dict1[ch] = num
    return True
