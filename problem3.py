def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
    
if(isPrime(9)):
    print('prime numbeer')
else:
    print('not prime number')

def isInt(num):
    if(isinstance(num, int)):
        print(True)
    print(False)




def nextPrime(n):   
    for i in range(2, n):
        if(isPrime(i)):   
            divide = n /i
            if (isinstance(divide, int)):
                  print(divide)
            #     nextPrime(i , n/i)


nextPrime(13195)
        


