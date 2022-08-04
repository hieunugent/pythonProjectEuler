def func(array):
    if len(array) == 0:
        return 0
    return len(array[0])+ func(array[1:])
print(func(["ab", "c","def", "ghij"]))