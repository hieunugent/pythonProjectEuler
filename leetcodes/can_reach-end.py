def can_reach_end(A):
    reachpos = 0
    last_index = len(A)
    i = 0
    while i <= reachpos and reachpos< last_index:
        reachpos = max(reachpos, A[i]+i)
        i +=1
    return reachpos >= last_index


A =[2,3,4,1,0,0,0,0,1,1,1,3 ]    
print(can_reach_end(A))


def reach_end (A):
    f = 0
    last_index = len(A)
    i = 0
    while i <= f and f < last_index:
        f = max(f, A[i]+i)
        i+=1
    return f >= last_index
A =[2,3,4,1,0,0,0,0,1,1,1,3 ]    
print(reach_end(A))