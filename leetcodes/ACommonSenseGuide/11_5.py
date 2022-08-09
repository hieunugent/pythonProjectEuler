def func(row,col):
    if row ==1 or col == 1:
        return 1
    return func(row-1, col) + func(row, col-1)

def max(array):
    if len(array)==1:
        return array[0]
    if array[0]> max(array[1:len(array)-1]):
        return array[0]
    else:
        return max(array[1:len(array)-1])
print(max([1,2,3,4,55]))