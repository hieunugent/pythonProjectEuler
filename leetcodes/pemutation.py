def apply_pemutation(perm, A):
    for i in range (len(A)):
        while perm[i] != i:
             A[perm[i]], A[i] = A[i], A[perm[i]]
             perm[perm[i]], perm[i] = perm[i], perm[perm[i]]



A = [0,1,2,3,4,5,6]
perm =[6,3,4,5,2,1,0]

apply_pemutation(perm, A)
print(A)
print(perm)

# solve the same problem without 