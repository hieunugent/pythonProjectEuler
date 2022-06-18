def titleToNumber(self, columnTitle: str) -> int:
     arr = []
      arr += columnTitle

       def LetterToNum(l):
            return ord(l) - ord("@")
        last = len(arr)-1
        baseLine = 0
        result = 0
        while last >= 0:
            if baseLine == 0:
                current = LetterToNum(arr[last])
            else:
                current = LetterToNum(arr[last]) * 26**baseLine
            last -= 1
            baseLine += 1
            result += current
        return result
