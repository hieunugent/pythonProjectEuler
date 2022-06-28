




sample_ball=[11,13,18,30,37,6,12,20,27,32,6,10,31,48,56,3,44,41,63,69,10,19,40,45,58,19,28,41,42,51,2,27,42,44,51,18,20,26,53,69,22,39,43,62,64,2, 10, 35, 44, 46, 14, 16, 36, 52, 60, 11, 41,  56, 57, 63, 27, 28, 51, 68, 69, 2, 39, 50,61, 66 ]
power_ball =[16, 4, 12, 13, 25, 7, 25, 7, 25, 5, 7, 4, 16, 2, 22, 15]



repeat_ball = [0]*71
for i in sample_ball:
    repeat_ball[i] += 1
repeat_mega = [0]*27
for i in power_ball:
    repeat_mega[i] += 1
print(repeat_mega)

def topMega(repeat_mega):
    result = []
    maxValue = max(repeat_mega)
    for i in range(len(repeat_mega)):
        if repeat_mega[i] == maxValue:
            result.append(i)
     
    return result


def top5num(arr):
    result = []
    while len(result) < 5:
        maxValue = max(arr)
        for i in range(len(arr)):
            if arr[i] == maxValue:
                result.append(i)
                arr[i] = 0
            if len(result) == 5:
                return result

    return result


def guessingValue(arrB, arrM):
    powerNumber = topMega(arrM)
    for i in range(len(powerNumber)): 
        print([top5num(arrB), powerNumber[i]])


guessingValue(repeat_ball, repeat_mega)
guessingValue(repeat_ball, repeat_mega)
