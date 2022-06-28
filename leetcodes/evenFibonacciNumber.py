def fibEvenSum():
    previous = 1
    current =2
    nxt = previous +current
    sum = 2
    while nxt <= 4*(10**6):
        if nxt %2 ==0:
            sum +=nxt
        previous = current
        current = nxt
        nxt = previous+current
        
    return sum
print(fibEvenSum())    

def largestPalindrome():
    a = 1000
    def isPalindrome(num):
        string = str(num)   
        r = len(string)-1
        l = 0
        while l < r:
            if string[l] != string[r]:
                return False
            l+=1
            r-=1
        return True
    result = 0
    while a > 99:
        for b in range(100, a):
            product = a * b
            if isPalindrome(product) and product > result:
                result = product               
        a -=1
    return result           
print(largestPalindrome())
def smallestMultiple():
    num = 2520
    def canDivide(num):
        for i in range(1, 20):
            if num % i != 0:
                return False
        return True
    while True:
        if canDivide(num):
            return num
        else:
            num +=1
print(smallestMultiple())
    
