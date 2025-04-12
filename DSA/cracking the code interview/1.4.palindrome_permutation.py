def func(string):
    print(len(string))
    print(string.lower())
    hash_table={}
    l = len(string)
    odd_count = 0
    for i in string.lower():
        if i == " ":
            continue
        elif i not in hash_table:
            hash_table[i] = 1
            odd_count+=1
        else:
            hash_table[i] +=1
            if hash_table[i] % 2 ==0:
                odd_count -=1
            else:
                odd_count +=1
    return odd_count <= 1     
a = "Tact Coaa"
print(func(a))