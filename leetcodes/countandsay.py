def countsay(n):
    if n == 1:
        return 1
    step =1
def readletter(n):
    count = 1
    result=""
    current=n[0]
    for i in range(1,len(n)):      
        if n[i] != current:
            temp = str(count) + current
            result += temp
            count = 1
            current = n[i]
        elif i == len(n)-1:
            current = n[i]
            count+=1
            temp = str(count) + current
            result += temp
        else:
            count+=1
   
    return result

print(readletter("1112224"))        

