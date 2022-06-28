from traceback import print_tb
from unittest import result


sample_ball=[1,7,11,25,56,8,13,18,32,42,20,36,53,56,69,30,37,38,42,58,3,12,14,18,32,4,34,40,41,53,11,16,22,48,59,6,15,41,63,64,3,14,40,53,54,3,5,6,63,68,33,40,59,60,56,9,7,21,24,41,65,11,41,43,44,65,15,19,20,61,70,16,21,33,52,70,15,19,27,35,57,9,11,34,49,66,5,7,19,46,69,7,28,29,58,59,2,9,33,47,53]
mega_ball = [14,20,16,22,4,3,11,24,8,25,22,24,13,9,10,17,15,2,10,24]
repeat_ball = [0]*71

repeat_ball = [0]*71
for i in sample_ball:
    repeat_ball[i] += 1
    
    
repeat_mega = [0]*26
for i in mega_ball:
    repeat_mega[i] += 1

print(repeat_ball)
print(repeat_mega)
top_mega = 0
max_repeat = 0
for i, num in enumerate(repeat_mega):
    if num > max_repeat:
        top_mega = i-1
print(top_mega)
def top5num(arr):
    import numpy as np
    
    value = np.array(arr)
    result =[]
    while True:
        searched = max(arr)
        li = np.where(value == searched)[0]
        for  i  in range (len(arr)):
            if arr[i]== searched:
                arr[i]= 0
        while li is not None:
            result.append(li.pop())
        if len(result)== 5:
            break
    return result
    
print(top5num(repeat_ball))   
        
