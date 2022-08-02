
from itertools import product
from math import ceil
from os import curdir
from sys import maxsize
from turtle import down, st
from unittest import result



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
    
def generateTriangle(limits):
    def checkDivision(num):
        result = 0
        start = num
        while start > 0:
            if num% start == 0:
                result +=1
            start-=1
        return result
    target = int(limits)
    limit = (target//2)**2
    answer = None

    def is_even(n):
        if n %2 ==0:
            return True
        else:
            return False  
    print(limit)
    n = 1
    while True:
        if is_even(n):
            n_divisors = checkDivision(n//2)*checkDivision(n+1)
        else:
            n_divisors = checkDivision(n)*checkDivision((n+1)//2)
        if n_divisors > target:
            answer = n*(n+1)//2
            break
        n +=1
    return answer

def problem13():
    data13 = "37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"
    def dataForm(data):
        result = []
        for i in range(100):
            result.append(int(data[i*50:i*50+50]))
        return result
    def LargeSum(data):
        value = 0
        for i in data:
            value += i
        return str(value)[0:10]
    print(LargeSum(dataForm(data13)))

def problem14():
    def generateNext(num):
        if num == 1:
            return num
        elif num%2 == 0:
            return num//2
        else:
            return num*3 +1
    def generateCollatzSeq(start, d):
        try:
            return d[start]
        except KeyError:
            result = []
            result.append(start)
            while start != 1:
                start = generateNext(start)
                result.append(start)
            d[start] = len(result)
            return d[start]
   
    upper_bound = 1000000
    d={1:1}
    for i in range(1, upper_bound):
        d[i] = generateCollatzSeq(i, d)
    v = list(d.values())
    k = list(d.keys())
    result = k[v.index(max(v))]
    return result

# there is two ways to go for step, down or right
# as long as the ways is not matching with others will count one
# assume that this is square grid
# at the node [i,j]  randomly the total ways can reach there is sum of top node and left node

def problem15(target):
    def isBoundary(i, j):
        if i == 0 or j == 0:
            return True
        else:
            return False
    grid = [[1 for x in range(target+1)] for x in range(target+1)]
    for i in range(0, target+1):
        for j in range(0, target+1):
            if isBoundary(i,j):
                  grid[i][j] = 1  
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
           
    return grid[target][target]
def problem16(power):
    sum = 0
    num = 2<<power-1
    while num//10> 0:
        sum += num%10
        num = num//10
    if num > 0:
        sum += num
    return sum
        
def problem17(limit):
    nums = []
    for i in range(1, 1000+1):
        nums.append(i)
    def convertWord(num):
        dict ={0:"",  1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        dictPhase2 = {0: "",  1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        dictPhase3 ={2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
        thousand = "thousand"
        hundred = "hundred"
        value = []
        if num == 1000:
          value.append(dict[1])
          value.append(thousand)  
        else:
            if num//100 > 0:
                value.append(dict[num//100])
                value.append(hundred)
            if num > 100 and num%100>0:
                value.append("and")
            if num%100>0 and num >=10:
                if num %100 < 20 :
                    value.append(dictPhase2[num%20])
                else:
                    value.append(dictPhase3[(num%100)//10])
                    if (num % 100) % 10 != 0:
                        value.append(dict[(num%100)%10])
            if num%10 >0 and num < 10:
                value.append(dict[num])   
        return value
    def calculateLetter(words):
        result = 0
        for i in words:
            result +=len(i)
        return result
    def solve(limit):
        result = 0
        for i in range (1, limit+1):
            result += calculateLetter(convertWord(i))
        print(result)
    print(convertWord(limit))
    print(calculateLetter(convertWord(limit)))
    solve(limit)
from time import process_time
def problem18():
    data = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
    ]
    i = len(data)-1
    while i > 0:
        for j in range(1, len(data[i])):
            data[i-1][j-1] += max(data[i][j], data[i][j-1]) 
        i -=1               
    print( data[0][0])    
class  Date(object):
    def __init__(self, day: int, month: int , year: int):
        assert isinstance(day, int),"day must be integer"
        assert isinstance(month,  int), "Month must be Integer"
        assert isinstance(year, int), " Year must be Integer"
        assert 1 <= day <= 31, " day must be in range[1, 31]"
        assert 1 <= month <= 12 , "month must be in [1, 12]"
        assert 0 <= year <=9999, "year must be in [0,9999]"
        
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)
    
    def __le__(self, other:'Date'):
        if isinstance(other, Date):
            if self.year < other.year:
                return True
            elif self.year == other.year and self.month < other.month:
                return True
            elif self.month == other.month and self.day < other.day:
                return True
        return False   
    def __add__(self, other:int):
        if not isinstance(other, int):
            raise TypeError("Unsupported operand type(s) for +")
        rv = Date(self.day, self.month, self.year)
        if rv.day + other > Date.days_of_month(rv.month, rv.year):
            other -= Date.days_of_month(rv.month, rv.year) -rv.day
            rv.day = 0
            rv.month +=1
        if rv.month > 12:
            rv.month = 1
            rv.year +=1
        rv.day += other
        return rv
        
    @staticmethod
    def isLeapYear(year):
        return ((year%4)==0) and (((year%100)!=0) or ((year%400)==0))
    @staticmethod
    def days_of_month(month, year):
        standard_days = [31, 28,31, 30, 31, 30, 31, 31,30, 31, 30, 31 ]
        if month == 2 and Date.isLeapYear(year):
            return 29
        else:
            return standard_days[month-1]
        
def problem19():   
    lower_bound = Date(1,1,1901)
    upper_bound = Date(31,12, 2000)
    current_date = Date(1, 1, 1900)
    answer = 0
    
    current_date +=6
    while current_date <= lower_bound:
        current_date +=7
    while current_date <=upper_bound:
        if current_date.day==1:
            answer+=1
        current_date+=7
    return answer
    
    
def problem20():
    def factorial(num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * factorial(num-1)
    def sumFactorial(num):
        sum = 0
        while num > 0:
            sum += num%10
            num = num//10
        return sum
    fac = factorial(100)
    return sumFactorial(fac)
    
            
def problem21():
    def d(num):
        result = []
        for i in range(1, num):
            if num%i== 0:
                result.append(i)
        return sum(result)
    d_val= {}
    for i in range(1, 10000):
        d_val[i] = d(i)
   
    amicable_number = set()
    for n , d_n in d_val.items():
        if d_n in d_val and d_val[d_n] == n and n != d_n:
                    amicable_number.add(n)
                    amicable_number.add(d_n)             
    print(sum(amicable_number))

 
aphabet = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
aphabet = aphabet.split(", ")
namepages = open("leetcodes/names.txt")
names = []
for line in namepages:
    names = line.replace('"', '').split(',')

      

def score(name):
    result = 0
    for i in name:
       result += aphabet.index(i)+1
    return result


def problem22(names):
    sum = 0
    names.sort()
    for pos, name in enumerate(names):
        sum += (pos+1)*score(name)
    print(sum)
def problem23():
    def sumDivisor(num):
        sum = 0
        for i in range(1, num):
            if num%i == 0:
                sum+= i
        return sum
            
    def abundantNum(limit):
        allAbundant = []
        answer = 0
        for i in range(1, limit):
            if sumDivisor(i) > i:
                allAbundant.append(i)
            if not any((i -a in allAbundant) for a in allAbundant):
                answer +=i
        print(answer)
    abundantNum(28123)

def problem25():
    from itertools import permutations
    perm = permutations([0,1,2,3,4,5,6,7,8,9])
    count = 1
    for i in list(perm):
        if count >= 1000000:
            print(i)
            break
        count+=1
def permutation():
    global value
    value = []
    def helpPermutation(array, size):
        if size == 1:
            print(array)
            value.append(array)
            return 
        for i in range(size):
            helpPermutation(array, size-1)
            if size&1:
                array[0], array[size-1] = array[size-1], array[0]
            else:
                array[i], array[size-1] = array[size-1], array[i]
    a = [0,1,2]
    n = len(a)
   
    helpPermutation(a, n)
    print(value)
def problem25():
    def numDigits(num):
        count = 1
        while num//10 > 0:
            num  = num//10
            count+=1
        return count 
    fib = [1,1]
    def fibGenerate(fib):
        n = len(fib)   
        fib.append(fib[n-1]+fib[n-2])
        return fib
    while numDigits(fib[-1])< 1000:
        fib = fibGenerate(fib)
        
    print( len(fib))
def problem26():
    def fractionToDecimal(numerator,denominator):
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        result_list = [sign, str(quotient), '.']
        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder*10, abs(denominator))
            result_list.append(str(quotient))
        idx = remainders.index(remainder)
        result_list.insert(idx + 3, '(')
        result_list.append(')')
        result = ''.join(result_list).replace('(0)', '').rstrip('.')
        return result
    value = []
    currentMax = ""
    index = 0
    for i in range(2, 1000):
        num = fractionToDecimal(1, i)
        if "(" in num and ")" in num:
            value.append(num)
            if len(currentMax) < len(num):
                currentMax = num
                index = i
    print(index)
def problem27():
    def isPrime(num):
        for i in range(2,num):
            if num%i ==0:
                return False
        return True
        
    def primeGenerate(limit):
        result=[]
        for i in range(2, limit+1):
            if isPrime(i):
                result.append(i)
        return result
    def find_n_prime(p, a, b):
        n = 1
        while isPrime(n**2+a*n+b):
            n+=1
        return n
    def solve():
        range_limit = 1000
        primes = primeGenerate(range_limit)
        max_n_prime = 0
        for b, p in product(primes, repeat=2):
            a = p-b-1
            new_n_prime = find_n_prime(a, b)
            if new_n_prime > max_n_prime:
                max_n_prime = new_n_prime
                best = a, b
                print(best)
                print(a*b)
        a, b = best
        answer = a*b
        print( answer)
    solve()
   
def factorial(n, i=1, product=1):
    if n < i:
        return product
    factorial(n, i+1, product*i)

print(factorial(6, 1, 1))

