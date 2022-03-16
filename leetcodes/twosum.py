def twosum(nums, target):
    keys=[]
    for num in nums:
        candidate = target - num
        if candidate in keys:
            return [candidate, num]
        else:
            keys.append(num)


A = [2,7,11,15]
target =9 
print(twosum(A, target))