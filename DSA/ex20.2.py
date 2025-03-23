arr = [1,2,3,4,6,7,9,0,8]
arr2 = [2,3,0,6,1,5]
arr3 = [8,2,3,9,4,7,5,0,6]
def missing_one(arr):
    arr = sorted(arr)
    for i,item in enumerate(arr):
        if i != item:
            return i
print(missing_one(arr))