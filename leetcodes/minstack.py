class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        

    def push(self, val: int) -> None:
        stack = self.minstack
        if not stack:
            stack.append(val)
        else:
            for i in range(len(stack)):
                 if stack[i] < val:
                    stack = stack[:i] +[val] +stack[i:]
                    break
        
        self.minstack = stack
        print (stack) 
        
        

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