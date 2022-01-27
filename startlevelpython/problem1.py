b = 1000
i=0
a=0


def isMultipleof5(n):
    while(n > 0):
        n=n-5
    if(n==0):
        return 1
    return 0
def isMultipleof3(n):
    while(n > 0):
        n=n-3
    if(n==0):
        return 1
    return 0

while i < b:
    if isMultipleof3(i)| isMultipleof5(i):
        a=a+i
    i +=1
print(a)