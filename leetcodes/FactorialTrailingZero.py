  def trailingZeroes(self, n: int) -> int:
       def factorial(num):
            result = 1
            while num > 1:
                result *= num
                num -= 1
            return result
        result = str(factorial(n))
        print(result)
        countZero = 0
        res = 0
        for num in result:
            if num == '0' and countZero >= 1:
                countZero += 1
            elif num == '0':
                countZero = 1
            else:
                countZero = 0
            if countZero > res:
                res = countZero
        return res
