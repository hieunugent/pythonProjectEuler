def middleNode(self, head):
        def findListLenght(head):
            count=0
            if not head:
                return count
            while head.next:
                count+=1
                head = head.next
            return count+1
        def middleNodeHelper(head, mid):
            count = mid
            while count >0:
                head = head.next
                count-=1
            return head
        return middleNodeHelper(head, findListLenght(head)//2)        
    