import re
from unittest import result


def functionCheck(value, arr1, arr2):
    result = []
    secondResult = []
    maxvalue = 0
    for i in range (len(arr1)):
        target = value - arr1[i][1]
        for j in range(len(arr2)):
            if target == arr2[j][1]:
                result.append([arr1[i][0], arr2[j][0]])
            elif target > arr2[j][1]:
                sum = arr1[i][1] +arr2[j][1]
                if sum > maxvalue:
                    maxvalue = sum
                    secondResult.append([arr1[i][0], arr2[j][0]])
    if result:
        return result
    if secondResult:
        return [secondResult[-1]]
    else:
        return [[]]

        

value = 1
arr1 = [[1,2],[2,4],[3,1]]
arr2 = [[1,4],[2,5],[3,1]]
print(functionCheck(value, arr1, arr2))