def rotateArray(nums, k):
    n = len(nums)
    k %= n
    start = 0
    count = 0
    while count < n:
        currentIndex = start
        prevnumber = nums[start]
        while True:
            # swap number and the rotate position
            next_idx = (currentIndex+k)%n 
            nums[next_idx], prevnumber = prevnumber, nums[next_idx]
            currentIndex = next_idx
            count +=1
            if start ==currentIndex:
                break
        start +=1
    return nums
A = [1,2,3,4,5,6,7,8]
k = 5
print(rotateArray(A, k))
