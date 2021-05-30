class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.min = float('inf')
        
              

    def push(self, val: int) -> None:
        stack = self.minstack
        minvalue = self.min
        stack.append(val)
        if minvalue > val:
            minvalue = val
        self.min = minvalue
        self.minstack = stack


    def pop(self) -> None:
        last = len(self.minstack)-1
        stack = self.minstack
        stack = stack[:last]
        minvalue = float('inf')
        for i in stack:
            if i < minvalue:
                minvalue = i
        self.min = minvalue
        self.minstack = stack
        
        

    def top(self) -> int:
        num = self.minstack
        last = len(self.minstack) - 1
        if len(num)>0:
            return num[last]
        else:
            return None

    def getMin(self) -> int:
        return self.min
>>>>>>> 7ba1e5af046175b3aed52d7066cfcdd684d35665
