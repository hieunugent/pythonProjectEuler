def rerange(A):
    for  i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i%2))
        
        
A =[1,2,3,4,5,6,7,8,9,10]
rerange(A)
print(A)