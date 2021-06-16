def threeSum(self, nums: List[int]) -> List[List[int]]:
     output = []
     nums.sort()
     for i in range(len(nums)-2):
          left = i+1
          right = len(nums)-1
          while (left < right):
               sumofthree = nums[i]+nums[left]+nums[right]
               if sumofthree == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in output:
                         output.append(temp)
                    left += 1
                    right -= 1
               elif sumofthree < 0:
                    left += 1
               elif sumofthree > 0:
                    right -= 1
     return output

          
