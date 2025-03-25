def selectEven(a):
    if len(a) == 0:
        return []
    if a[0]%2 ==0:
        return a[0].add(selectEven(a[1:len(a)]))
    else:
        return selectEven(a[1:len(a)])


my_arr = [1,2,3,4,5,6,7,8,9]
print(selectEven(my_arr))
