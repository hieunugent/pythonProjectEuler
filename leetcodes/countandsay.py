
def readletter(word):
    if len(word) == 1:
        return "11"
    currentWord = word[0]
    result = ""
    count = 1
    for i in range(1, len(word)):
        if currentWord == word[i]:
            count+=1
        elif currentWord != word[i]:
            result += str(count) +currentWord
            count = 1
            currentWord = word[i]
        if i == len(word)-1:
            result += str(count) + currentWord
    return result
def countsay(n):
    if n == 1:
        return "1"
    step = 1
    result = "1"
    while step < n:
        result = readletter(result)
        step +=1
    return result


print(countsay(4))  

