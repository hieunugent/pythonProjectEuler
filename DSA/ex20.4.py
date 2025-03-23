arr=[-10,6,8,1,3,-6,9]

def func(a):
    a = sorted(a)
    if len(a)>2:
        product_last = a[0] *a[1]
        product_end = a[-1] + a[-2]
        return product_last if product_last>product_end else product_end
    return -1


print(func(arr))