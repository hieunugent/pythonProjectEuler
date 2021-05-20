class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        minstack = []
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        

    def pop(self) -> None:
        last = len(self.minstack)-1
        stack = self.minstack
        stack = stack[:last]
        self.minstack = stack
        
        

    def top(self) -> int:
        num = self.minstack
        if len(num)>0:
            return num[0]
        else:
            return None

    def getMin(self) -> int:
        last = len(self.minstack) - 1
        if last >= 0:
            return self.minstack[last]
        else:
            return None