def fib(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)
    
def fib_until(num):
    curr = 0
    while fib(curr) <= num:
        print(fib(curr))
        curr += 1
    
fib_until(100)
    
