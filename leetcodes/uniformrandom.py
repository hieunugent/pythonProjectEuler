def uniform_random (upperBound : int , lowerBound : int)-> int:
    numofOutcome = upperBound-lowerBound+1
    while True:
        result= 0
        i = 0
        while(1<<i) < numofOutcome:
            result = result <<1
            i += 1
        if result < numofOutcome:
            break
    return result+ lowerBound
import random
print(random.randint(6,10))