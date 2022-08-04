array = [1,2,3,4,5,6,7,8,9]
def func(array, index=0):
    if index == len(array):
        return array
    array[index] = array[index]*2
    return func(array, index+1)    
print(func(array))