   def divide(self, dividend: int, divisor: int) -> int:
        neg = 1
        if dividend < 0:
            neg = -1*neg
        if divisor < 0:
            neg = -1*neg
        
    
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if divisor<<i <= dividend:
                res += 1<<i
                dividend -= divisor<<i
        if res*neg > 2**31-1:
            return 2**31-1
        return res*neg