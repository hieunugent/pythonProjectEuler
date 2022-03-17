def twosum(nums, target):
    keys=[]
    for num in nums:
        candidate = target - num
        if candidate in keys:
            one = nums.index(candidate)
            two = nums.index(num)
            return [one, two]
        else:
            keys.append(num)


A = [2,7,11,15]
target =9 
print(twosum(A, target))