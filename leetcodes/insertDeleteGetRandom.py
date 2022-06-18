class RandomizedSet:
    
    def __init__(self):
        self.value=[]
        
        

    def insert(self, val: int) -> bool:
        if val in self.value:
            return False
        else:
            self.value.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.value:
            return False
        else:
            self.value.remove(val)
            return True
        

    def getRandom(self) -> int:
        import random
        index = random.randint(0, len(self.value)-1)
        return self.value[index]