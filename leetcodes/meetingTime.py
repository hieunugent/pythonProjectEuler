timeA = [[1,10],[12,13],[14, 15],[3, 20]]
timeB = [[1,2], [1,4],[1,7], [1,10]]


timeC = sorted(timeA, key=lambda x:x[0])
def meetingTime(times):
   for i in range(len(times)-2):
       current = times[i]
       next = times[i+1]
       if current[1] > next[0]:
           return False      
   return True 

print(meetingTime(timeB))