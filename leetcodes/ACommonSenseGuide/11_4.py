def func(string, index = 0):
    if index >= len(string):
        return -1
    if string[index]=='x':
        return index
    return func(string, index+1)
print(func("abcdefghijklmnopqrstuvwxyz"))