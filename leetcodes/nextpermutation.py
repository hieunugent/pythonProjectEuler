def next_permutation(perm):
    k = len(perm)-2
    for k in range (len(perm)-2, -1, -1):
        if perm[k] <= perm[k+1]:
            break
    if k ==-1:
        return []
    for i in range (k+1, -1, -1):
        if perm[i] > perm[k]:
            perm[i], perm[k] = perm[k], perm[i]
            break
    return perm 

perm =[4,3,2,1,2,1]
print(next_permutation(perm))
