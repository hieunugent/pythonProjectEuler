def encrypt(text, keys):
    key =  keys # 65 - 90  
    arr = text.upper()
    arr = list(arr)
    for idx, a in enumerate(arr):
        if ord(a) >= 65 and ord(a)<=90:
            a = ord(a)
            a = ((a+key)-65)%(90-65)+65
            arr[idx] = chr(a)
    arr = ''.join(arr)
    return arr
def decrypt(text, keys):
    key = keys
    arr = text.upper()
    arr = list(arr)
    for idx, a in enumerate(arr):
            if ord(a) >= 65 and ord(a)<=90:
                a = ord(a)
                a = ((a-key)-65)%(90-65)+65
                arr[idx] = chr(a)
    arr = ''.join(arr)
    return arr

def reverseCipher(text):
    l = len(text) -1
    res = ''
    
    while l >=0:
        res = res + text[l]
        l = l-1
    return res

test = "hello is the best?"
print(reverseCipher(test))