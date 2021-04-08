def squareEvent(num):
    for i in range (len(num)):
         if not num[i]%2:
             num[i] = num[i]*num[i]

num = [1,2,3,4,5,6,7,8,9]
squareEvent(num)

print(num)


def replaceElements(self, arr: List[int]) -> List[int]:
    right = arr[len(arr)-1]

    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1:
             arr[i] = -1
        else:
            current = arr[i]
            arr[i] = right
            right = current if current > right else right

    return arr
