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


# find the possible max of palindrome


# consider if exits a factor of the num ber



def brute_force(n):
    largest_number = (10 ** n) - 1
    smallest_number = (10 ** (n-1))
    largest_palindrome = 0
    for outer_i in range (largest_number, smallest_number,-1):
        for inner_i in range (outer_i, smallest_number, -1):
            number = outer_i * inner_i
            if(isPalindrome(number) & (number > largest_palindrome)):
                largest_palindrome = number
                if(inner_i > smallest_number):
                    smallest_number = inner_i
                break
    return largest_palindrome


print(brute_force(3))

print(10**3)
print(10**2)