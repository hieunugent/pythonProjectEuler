def getmedian(array):
    if not len(array)%2:
       
        return (array[len(array)//2-1]+array[len(array)//2])/2
    return array[len(array)//2]


def median(array1, array2):
    if (len(array1)==1):
        return (array1[0]+array2[0])/2
    if (len(array2)==2):
        return (max(array1[0], array2[0])+ min(array1[1], array2[1]))/2
    median1 = getmedian(array1)
    median2 = getmedian(array2)
    if median1 == median2:
        return median1
    if median1 > median2:
        return median(array1[0:len(array1)//2 +1], array2[len(array2)//2:])
    return median(array1[len(array1)//2:], array2[0:len(array2)//2+1])


print (median([1,2,3,4], [5,6,7,8]))   
