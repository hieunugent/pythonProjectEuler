#!/usr/bin/python3
def checkIfExist(self, arr: List[int]) -> bool:
    store = []
    for num in arr:
            if not num in store:
                if num % 2 == 0:
                    store.append(num//2)
                store.append(num*2)
            else:
                return True
    return False
