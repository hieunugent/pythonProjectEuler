temp = [98.0,97.1,99.0,98.7,98.6,97.4,97.5,98.3,97.5,97.2,97.9,98.7,98.9]
def temp_order(temp):
    # build hash_table for temp look up
    hash_table = {}
    for t in temp:
        if t in hash_table:
            hash_table[t] += 1
        else:
            hash_table[t] = 1
    current_temp = 970
    result_sorted=[]
    while current_temp < 990:
        if current_temp/10.0 in hash_table:
            for i in range(hash_table[current_temp/10.0]):
                result_sorted.append(current_temp/10.0)
        current_temp+=1
    return result_sorted
print(temp_order(temp))