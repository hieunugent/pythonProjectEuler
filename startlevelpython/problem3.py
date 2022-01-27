def isPrime(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if (n % i == 0):
            return 0
    return 1

isPrime(4)

def fun(num):
    i = 2
    while i*i <= num:
        if num % i:
            i+=1
        else:
            num//=i
    return num
   

print(fun(600851475143))

def primeFactor(num):
    i = 2
    factor=[]
    while i*i <=num:
        if num %i:
            i+=1
        else:
            num//=i
            factor.append(i)
    if num > 1:
        factor.append(num)
    return factor

print(primeFactor(600851475143))