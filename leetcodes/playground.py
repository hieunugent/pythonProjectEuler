print([1]+ [0]*10)
A = [1,6,3,4,5,2,7]
B = A
print(B)
C = list(A)
print(C)
E=A[:]

print(A[4:0:-2])


A[0], A[len(A)-1]= A[len(A)-1], A[0]
print(A)