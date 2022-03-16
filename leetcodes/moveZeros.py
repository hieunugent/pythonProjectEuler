def moveZeros(nums):
    left = 0
    right = len(nums)-1
    while not nums[right]:
        right -=1
    
    while left < right:
        if not nums[left]:
            nums[left], nums[right] = nums[right], nums[left]
            right-=1
        left +=1
            
    return nums

def  moveZerosRe(nums):
    for i  in range (len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if nums[j] != 0:
                     nums[i], nums[j] = nums[j], nums[i]
                     break
                
    
        
    
    
nums = [0,0,0,0,0,1,0,0,2,0,3,0,0]
moveZerosRe(nums)
print (nums)