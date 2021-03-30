
def dutch_flag (p , A):
    pivot = A[p]
    smaller, equal, larger = 0, 0 , len(A)
    
    while equal < larger:
        if A[equal]<pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller+1, equal+1
        elif A[equal]==pivot:
            equal+=1
        else:
            larger -=1
            A[equal], A[larger]= A[larger], A[equal]
    
A = [1,3,2,1,2,3,3,2,4]

dutch_flag(2, A)
print(A)