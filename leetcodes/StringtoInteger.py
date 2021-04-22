def myAtoi(self, s: str) -> int:
    stillPrefix = True
    num = 0
    neg = False
    for i in s:
            if i == " " and stillPrefix:
                continue
            elif (i == " " or i == "-" or i == "+") and not stillPrefix:
                break
            elif i == '+':
                stillPrefix = False
                continue
            elif i == "-":
                neg = True
                stillPrefix = False
                continue
            elif i >= '0' and i <= '9':
                stillPrefix = False
                num = num*10+int(i)
            else:
                stillPrefix = False
                break
    if neg:
            num = num*-1
    if num < -2**31:
            num = -2**31
    if num > 2**31-1:
            num = 2**31-1
    return num
