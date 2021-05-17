class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        minstack = []
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        

    def pop(self) -> None:
        last = self.minstack[len(self.minstack)-1]
        newStack = self.minstack[:len(self.minstack)-2]
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        