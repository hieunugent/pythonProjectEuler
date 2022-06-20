def power(x:float, y:float)-> float:
    result = 1.0
    power= y
    if y < 0:
        power = -power
        x = 1.0/x
    while power:
        if power &1:
            result *= x
        x = x *x
        power = power >> 1
    return result
    
