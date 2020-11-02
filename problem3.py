def isPrime(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True



def fun(num):
    if (num > 1):
        for i in range(2, num ):
            if (num % i)==0:
                 fun(num//i)
            print(i)
            
                
fun(45)

a = 3*3*5*5       


