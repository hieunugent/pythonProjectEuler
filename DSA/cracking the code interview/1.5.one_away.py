def one_away(v1, v2):
    # check insert
    # check remove
    print("pair value is " + "{"+ v1+ ", "+ v2 +"}")
    if len(v1) > len(v2):
        v1, v2 = v2 , v1
    if len(v1) != len(v2):
        j,i= 0,0
        count = 0
        while i < len(v1) and j < len(v2) :
            if v1[i] != v1[j]:
                count+=1
                j+=1
            else:
                i+=1
                j+=1
            if count > 1:
                print ("number of count is " + str(count))
                return False
        if count < 1 :
            print ("number of count is " + str(count))
            return True 
            
    # check replace
    else:
        count = 0
        for i in range(len(v1)):
            if v1[i] != v2[i]:
                count +=1
            if count > 1:
                print ("number of count is " + str(count))
                return False
        if count <= 1:
            print ("number of count is " +  str(count))
            return True
    return False





print(one_away("value","vale"))
print(one_away("value","valuu"))
print(one_away("value","zaluu"))
print( one_away("value","values")) 
print(one_away("pale","ple"))
print(one_away("pale","bake"))