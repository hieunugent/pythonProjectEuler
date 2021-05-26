    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 :
            return False
        while not n == 0 and n >= 3:
            n = n % 3
        if n == 0:
            return True
        return False
            