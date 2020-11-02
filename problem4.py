def isPalindrome(n):
    temp=n
    rev=0
    while(n > 0):
        dig= n%10
        rev= rev*10 +dig
        n=n//10
    if(temp == rev):
        return True
    else:
        return False


def fun(a, b):
    temp = 0
    for i in range(999,1):
        for j in range(999,1):
            if palindrome(i*j):
                temp = max(temp, j*j)
    return temp

print(fun(999,999))

start = 999*999
while (not isPalindrome(start)):
    start-=1

print(start)



