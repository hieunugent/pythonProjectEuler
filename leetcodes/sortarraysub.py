def sortedarray(subNums):
    start = 0
    end = len(subNums)-1
    for i in range(len(subNums)):
        for j in range(i+1, len(subNums)):
            if subNums[i][0] > subNums[j][0]:
                subNums[i], subNums[j] = subNums[j], subNums[i]
            
array = [[3,5], [5,6], [7,8], [0,1]]
print(array)
sortedarray(array)
print(array)

