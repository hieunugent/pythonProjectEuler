def increatestriplet(nums):
    for i in range(len(nums)):
        stack = [nums[i]]
        count = 1
        for j in range(i+1, len(nums)):
            if stack[-1] < nums[j]:
                stack.append(nums[j])
            elif stack[0] < nums[j]:
                stack.pop()
                stack.append(nums[j])
        if len(stack) >= 3:
            return True
    return False
    
