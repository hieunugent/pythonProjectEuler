def duplicateZero(arr):
    possible = 0
    length = len(arr)-1
    for left in range (length +1):
        if left > length - possible:
            break
        if arr[left] == 0:
            if left == length - possible:
                arr[length] = 0
                length -= 1
                break
            possible +=1
    last = length- possible
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i+possible] = 0
            possible -= 1
            arr[i+possible] = 0
        else:
            arr[i+possible] = arr[i]
    print(arr)


A = [1,0,1,2,4,5,7,7,8,6]    
duplicateZero(A)