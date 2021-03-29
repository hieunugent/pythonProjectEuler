def reverse(x : int )-> int:
    result = 0
    x_remaining = x
    while x_remaining:
        result = result*10 + x_remaining%10
        x_remaining //= 10
    return -result if x < 0 else result
    
print(reverse(12345))