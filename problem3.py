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
        print("True")
        return True
    return False

for i in range(2, 10):
    if(isPrime(i)& isInt(10/i)):
        print(i)
    else:
        print("")

isInt(4/4)


        


