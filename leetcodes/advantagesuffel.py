
def advantageCount( A, B):
    sortedA = sorted(A)
    sortedB = sorted(B)
        
    assigned = {b:[] for b in B} 
    remaining =[]
        
    j = 0
    for a in sortedA:
        if a > sortedB[j]:
            assigned[sortedB[j]].append(a)
            j +=1
        else:
            remaining.append(a)
    return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]
    
print(advantageCount([1,2,3,4,5,6], [1,2,3,4,5,7]))