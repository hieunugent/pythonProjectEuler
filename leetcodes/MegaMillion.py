

sample_ball=[1,7,11,25,56,8,13,18,32,42,20,36,53,56,69,30,37,38,42,58,3,12,14,18,32,4,34,40,41,53,11,16,22,48,59,6,15,41,63,64,3,14,40,53,54,3,5,6,63,68,33,40,59,60,56,9,7,21,24,41,65,11,41,43,44,65,15,19,20,61,70,16,21,33,52,70,15,19,27,35,57,9,11,34,49,66,5,7,19,46,69,7,28,29,58,59,2,9,33,47,53]
mega_ball = [14,20,16,22,4,3,11,24,8,25,22,24,13,9,10,17,15,2,10,24]

repeat_ball = [0]*71
for i in sample_ball:
    repeat_ball[i] += 1 
repeat_mega = [0]*26
for i in mega_ball:
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
    while len(result)<5:
        maxValue = max(arr)
        for i in range(len(arr)):
            if arr[i] == maxValue:
                result.append(i)
                arr[i] = 0
            if len(result)==5:
                return result
                
    return result
    
def guessingValue (arrB, arrM):
    powerNumber = topMega(arrM)
    for i in range(len(powerNumber)): 
        print([top5num(arrB), powerNumber[i]])
        

guessingValue(repeat_ball, repeat_mega)
guessingValue(repeat_ball, repeat_mega)


