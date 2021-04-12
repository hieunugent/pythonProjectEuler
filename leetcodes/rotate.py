def rotate2(nums, k):
    n =  len(nums)
    k %=n
    start= count = 0
    while count < n:
        current , prev = start, nums[start]
        while True:
            next_idx = (current+k)%n
            nums[next_idx] , prev= prev, nums[next_idx]
            current = next_idx
            count +=1
            if start == current:
                break
        start+=1

def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashtable = defaultdict(int)
        result =[]
        if len(nums1) > len(nums2):
            for num in nums1:
                hashtable[num] +=1
            for num in nums2:
                if hashtable[num] > 0:
                    result.append(num)
                    hashtable[num] -=1
        else:
            for num in nums2:
                hashtable[num] +=1
            for num in nums1:
                if hashtable[num] > 0:
                    result.append(num)
                    hashtable[num] -=1

        
        
        return result 


def plusOne(self, digits: List[int]) -> List[int]:
    carry = 0
    n = len(digits)
    digits[n-1] += 1
    for i in range(n - 1, -1, -1):
            current = digits[i] + carry
            digits[i] = current % 10
            if current > 9:
                carry = 1
            else:
                carry = 0
    if carry == 1:
        return [1] + digits
    return digits

def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        # self.transpose(matrix)
def transpose(self, matrix):
        n = len(matrix)
        for i in range (n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
                
