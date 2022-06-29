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
    


    
    



