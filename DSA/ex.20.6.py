sers = [1,15,3,19,4,5,36,6,7,78,8,9,90,99,33,23]
def consecutive (item):
    hash_table ={}
    for i in item:
        hash_table[i] = True
    # check if there is any previous number before the current number
    max_consecutive = 0
    for i in item:
        if i-1 not in hash_table:
            current_consecutive =1
            while i+1 in hash_table:
                i +=1
                current_consecutive +=1
                if current_consecutive >max_consecutive:
                    max_consecutive=current_consecutive
    return max_consecutive
print(consecutive(sers))            
            

