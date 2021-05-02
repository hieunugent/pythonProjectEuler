def delete_duplicate(A):
    if not A:
        return []
    write_idx = 1
    for i in range (1, len(A)):
        if A[write_idx-1] != A[i]:
            A[write_idx] = A[i]
            write_idx += 1
    A = A[:write_idx]
    return A
    
A= [1,2,3, 3, 4, 4, 5, 6, 6, 6, 7 ,8, 9]
A= delete_duplicate(A)
B = [123,134]



def delete_key(A, key):
    indexkeep = 0
    for i in range(0, len(A)):
        if A[i] != key:
            A[indexkeep]=A[i]
            indexkeep+=1
    A = A[:indexkeep]
    return A
print(delete_key(A, 6))

# append the List with m times and these must be min(2, m )
def append_time(A, m):
    if not A:
        return []

    minAppear = min(2,m)
    if minAppear ==1 :
        return delete_duplicate(A)
    else:
        A = delete_duplicate(A)
        for i in range(0, len(A)):
            A.append(A[i])
    return sorted(A)
        
            
B= [1,2,3, 3, 4, 4, 5, 6, 6, 6, 7 ,8, 9]      
print (append_time(B, 2))
    