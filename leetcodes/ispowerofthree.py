   def isPowerOfThree(self, n: int) -> bool:
        x = math.log(n, 3)
        if x - int(x) == 0:
            return True
        else:
            return False
            