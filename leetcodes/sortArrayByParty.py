def sortArrayByParity(self, A: List[int]) -> List[int]:
    fistodd = 0
    lasteven = len(A)-1
    for num in A:
        if num % 2 == 0:
            fistodd += 1
        else:
            break
    for num in A[::-1]:
        if num % 2 == 0:
             break
        lasteven -= 1

    while fistodd < lasteven:
        if A[fistodd] %2 != 0 and A[lasteven]%2 == 0:
                A[fistodd], A[lasteven] = A[lasteven], A[fistodd]
                fistodd += 1
                lasteven -= 1
        elif A[lasteven] % 2 != 0:
                lasteven -= 1
        elif A[fistodd] % 2 == 0:
                fistodd += 1
    return A

def thirdMax(self, nums: List[int]) -> int:
    if len(nums)<2:
        return nums[0]
    nums.sort(reverse =True)
    count = 1
    currentmax = 0
    for i  in range (1, len(nums)):
        if nums[i] != nums[i-1] and count<=3:
            count+=1
            if count == 3:
                currentmax = i
    return nums[currentmax]
