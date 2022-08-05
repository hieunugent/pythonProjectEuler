def func(row,col):
    if row ==1 or col == 1:
        return 1
    return func(row-1, col) + func(row, col-1)

print(func(3, 7))