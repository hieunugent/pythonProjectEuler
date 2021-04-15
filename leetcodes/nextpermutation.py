def next_permutation(perm):
    k = 0
    for i in range (len(perm)-2, -1, -1):
        if perm[i] < perm[i+1]:
            k = i
            break
    if k ==-1:
        return []
    for i in range (len(perm)-1, k, -1):
        if perm[i] > perm[k]:
            perm[i], perm[k] = perm[k], perm[i]
            break
    return perm 

perm =[6,2,4,5,3,1,0]
print(next_permutation(perm))
