import  math
def ispalindrome(x : int)-> bool:
    if x <= 0:
        return x == 0
    numdigit = math.floor(math.log10(x))+1
    msk = 10**(numdigit-1)
    for i in range(numdigit//2):
        if x // msk !=  x % 10:
            return False
        x %= msk
        x //= 10
        msk //= 100
    return True

print(ispalindrome(12321))
print(ispalindrome(123321))
print(ispalindrome(123421))
print(ispalindrome(12323))


