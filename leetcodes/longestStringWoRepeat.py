 def lengthOfLongestSubstring(self, s):
        longStr = 0
        for i in range( len(s)-1):
            array=[]
            array.append(s[i])
            for j in range(i , len(s)-1):
                if s[j] in array:
                    if len(array) > longStr:
                        longStr = len(array)
                    break
                else:
                    array.append(s[j])
                    
        return longStr