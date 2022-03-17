def reverseWords(self, s: str) -> str:
       def revStr(s):
            return s[::-1]
        result = ""
        arr = s.split(" ")
        for word in arr:
            result += word[::-1]+" "
        return result[:len(result)-1]
