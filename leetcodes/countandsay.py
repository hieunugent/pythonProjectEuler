def countsay(n):
    if n == 1:
        return 1
    step =1
def readletter(n):
    count = 1
    result=""
  
    for i in range(1,len(n)):      
        if n[i] != n[i-1]:
            temp = str(count) + n[i-1]
            result += temp
            count = 1

        elif i == len(n)-1:
            
            count+=1
            temp = str(count) + n[i]
            result += temp
        else:
            count+=1
    return result

print(readletter("1112224"))        

