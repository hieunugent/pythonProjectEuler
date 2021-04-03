def findNumbers(nums):
    def evenDigits(num):
            count = 1
            while num//10:
                count += 1
                num = num//10
            return count % 2 == 0

    if len(nums) == 0:
        return 0
    eventCount = 0
    for i in range(0, len(nums)):
        if evenDigits(nums[i]):
            eventCount += 1
    return eventCount
