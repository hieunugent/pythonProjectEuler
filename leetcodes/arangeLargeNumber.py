

class LargestNumbers:
    def __init__(self, nums):
        self.nums = nums               
    def findLargeNum(self):
            def leftGreaterRight (a, b):
                aStr = str(a)
                bStr = str(b)
                aIdx= 0
                bIdx = 0
                while aIdx < len(aStr) and bIdx < len(bStr):
                    if aStr[aIdx] > bStr[bIdx]:
                        return True
                    elif  aStr[aIdx] < bStr[bIdx]:
                        return False
                    aIdx+=1
                    bIdx+=1
                while bIdx < len(bStr):
                    if bStr[bIdx] > '0':
                        return False
                    else:
                        bIdx +=1
                while aIdx < len(aStr):
                    if aStr[aIdx] >'0':
                        return True
                    else:
                        aIdx +=1          
                return True if len(aStr) < len(bStr) else False
        
            def arangeThis(nums):   
                for i in range(len(nums)):
                    for j in range(i+1, len(nums)):
                        if  not leftGreaterRight(nums[i], nums[j]):
                            nums[i], nums[j] = nums[j], nums[i]           
            arangeThis(self.nums)
            result=""
            for num in self.nums:
                result +=str(num)
            return result

myArrange = LargestNumbers(nums=[3,20,34,5,9])
print(myArrange.findLargeNum())



    


  