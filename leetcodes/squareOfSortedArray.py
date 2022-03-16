import enum


def sortedSquares(nums):
        def square_num(num):
            return num**2
        def merger_sort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                merger_sort(L)
                merger_sort(R)
                i=j=k=0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i +=1
                    else:
                        arr[k] = R[j]
                        j+=1
                    k +=1
                while i < len(L):
                    arr[k] =L[i]
                    k+=1
                    i+=1
                while j < len(R):
                    arr[k] = R[j]
                    k+=1
                    j+=1
            return arr
                    
        
        for (index, num) in enumerate(nums):
             nums[index] = square_num(num)
        
        return merger_sort(nums)
    
A = [-4, 1, 0, 3, 10]

B = sortedSquares(A)
print(B)