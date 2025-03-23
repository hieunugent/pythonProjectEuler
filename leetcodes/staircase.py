numSteps = int(input("Please enter number of steps of the stair you want to calculate how many possible path:" ))
def numofpath(n):
    if n <0: 
        return 0
    elif n == 1 or n == 0:
        return 1
    else: 
        return numofpath(n-3) + numofpath(n-3) + numofpath(n-1)


value = numofpath(numSteps)
print(value)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            