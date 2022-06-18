def isHappy(self, n: int) -> bool:
       def helper(num):
            arr = []
            arr += str(num)
            print(arr)
            result = 0
            for num in arr:
                result += int(num)**2
            return result
        result = helper(n)
        exist = []
        while True:
            if result in exist:
                return False
            elif result == 1:
                return True
            else:
                exist.append(result)
                result = helper(result)
