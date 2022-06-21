def mySqrt(self, x: int) -> int:
      square = []
       for i in range(46341):
            square.append(i*i)
        for i in range(1, 46341):
            if square[i-1] == x or square[i-1] < x and square[i] > x:
                return i-1
            elif square[i] == x:
                return i

        return len(square)-1
