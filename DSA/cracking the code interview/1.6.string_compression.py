def compression(input_value):
    result= ""
    current =input_value[0]
    count = 1
    s = 1
    while s < len(input_value):
        if input_value[s] == current:
            count+=1
            s+=1
        else:
            result = result + current + str(count)
            current = input_value[s]
            count = 0
    result = result + current + str(count)
    if len(result) < len(input_value):
        return result
    else:
        return input_value





value = "abcdefg"
print(compression(value))