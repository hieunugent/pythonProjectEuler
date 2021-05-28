def hammingDistance(self, x: int, y: int) -> int:
        def countdif(n):
            sum = 0
            while n!= 0:
                sum +=1
                n = n & (n-1)
            return sum 
        n = x ^ y 
        return countdif(n)