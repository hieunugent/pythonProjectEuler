from itertools import product
from turtle import down, st


def fibEvenSum():
    previous = 1
    current = 2
    nxt = previous + current
    sum = 2
    while nxt <= 4*(10**6):
        if nxt % 2 == 0:
            sum += nxt
        previous = current
        current = nxt
        nxt = previous+current

    return sum


def largestPalindrome():
    a = 1000

    def isPalindrome(num):
        string = str(num)
        r = len(string)-1
        l = 0
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
    result = 0
    while a > 99:
        for b in range(100, a):
            product = a * b
            if isPalindrome(product) and product > result:
                result = product
        a -= 1
    return result


def smallestMultiple():
    def canDivide(num):
        for i in range(1, 20):
            if num % i != 0:
                return False
        return True
    num = 2520
    while num < 2**31:
        if canDivide(num):
            return num
        else:
            num += 1


def sumSquareDiff(amount):
    def squareSum(amount):
        res = 0
        for i in range(1, amount+1):
            res += i**2
        return res

    def sumSquare(amount):
        res = 0
        for i in range(1, amount+1):
            res += i
        return res**2
    return sumSquare(amount) - squareSum(amount)


def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(1, num):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            return False
    return True


def buildPrime(value):
    count = 0
    num = 2
    while True:
        if isPrime(num):
            count += 1
        if count == value:
            return num
        num += 1


def LargestProductInSeries(data, numAdj):
    currValue=0
    def productOfString(value):
        product = 1
        for i in range(len(value)):
            product *= int(value[i])
        return product
    for i in range(len(data)):
        if i + numAdj < len(data):
            string = data[i:i+numAdj]
            currentProduct = productOfString(string) 
            if currentProduct > currValue:
                currValue = currentProduct
        else:
            break
    return currValue
 

data = ["7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"]

def specialPythagorean():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if( a+b+c == 1000) and (a**2 +b**2 == c**2):
                    return a*b*c
                if a+b+c > 1000:
                    break
    

def sumPrime(value):
    result = 0
    num = 2
    while True:
        if isPrime(num):
            if num < value:
                result += num
                print("Prime Num : " ,num)
                print("sum "  , result)
            else:
                return result
        num += 1    

def sum_primes(limit):
    primes = []
    for n in range(2, limit+1):
        # try dividing n with all primes less than sqrt(n):
        for p in primes:
            if n % p == 0: break     # if p divides n, stop the search
            if n < p*p:
               primes.append(n)      # if p > sqrt(n), mark n as prime and stop search
               break
        else: primes.append(n)       # fallback: we actually only get here for n == 2
    return sum(primes)
def dataPrepare():
    data = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    data= data.split(' ')
    newData =[]
    i = 0
    while i < len(data):
        newData.append(data[i:i+20])
        i = i+20
        
    return newData
def moveleftright(x,y,data):
    product= 1
    if y + 3 < 20:
        product =1
        for i in range(4):
            product *= int(data[x][y+i])
        return product
    else:
        return 0
def moveUpDown(x, y , data):
    product= 1
    if x + 3 < 20:
        product =1
        for i in range(4): 
            product *= int(data[x+i][y])
        return product
    else:
        return 0
    
    return max(product,product2)
def moveDiagonal(x, y , data):
    product= 1
    if x + 3 < 20 and y +3 < 20:
        product = 1
        for i in range(4):
            product *= int(data[x+i][y+i] )
        return product
    else:
        return 0
def moveReverseDiagonal(x, y, data):
    product = 1
    if x +3 <20 and y-3 >0:
        product = 1
        for i in range(4):
            product *= int(data[x+i][y-i])
        return product
    else:
        return 0 
def largest_product_grid(data):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            temp_result = max(moveleftright(i,j,data), moveUpDown(i,j,data),moveDiagonal(i,j,data), moveReverseDiagonal(i,j,data))
            if result < temp_result:
                result = temp_result
    print(result)
    
def generateTriangle(valuelimit):
    def checkdivison(num):
        result = 0
        start = num
        while start > 0:
            if num% start == 0:
                result +=1
            start-=1
        return result
    currNaturalNum = 1
    striangle = currNaturalNum
    while True:
        striangle += currNaturalNum
        currNaturalNum +=1
        if checkdivison(striangle) >= valuelimit:
            return striangle

print(generateTriangle(500))     