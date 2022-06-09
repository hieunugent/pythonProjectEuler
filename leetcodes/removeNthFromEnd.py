def removeNthFromEnd(self, head, n):

    current = head
    length = 1
    while current.next != None:
            length += 1
            current = current.next
    current = head
    n = length - n + 1

    count = 1
    if n == 1:
            head = head.next
            return head
    while count < n-1:
            count += 1
            current = current.next
    if current.next.next != None:
            current.next = current.next.next
    else:
            current.next = None
    return head
def removeNthFromEnd(self, head, n):
        def findListLenght(head):
            if not head:
                return 0
            count=1
            while head.next:
                count+=1
                head = head.next
            return count
        def removeNthHelper(head, pos, n):
            temp = head
            count = 1
            if pos == 1:
                head = head.next
                return head
            while count < pos - 1 and temp.next:
                temp = temp.next
                count +=1
            if temp.next.next != None:
                 temp.next = temp.next.next
            else:
                temp.next = None
            return head
        # if findListLenght(head) <=2:
        #     temp = head
        #     if n == 1:
        #         if findListLenght(head) == 1:
        #             return None
        #         temp.next = None
        #         return head
        #     elif n == 2:
        #         head = head.next
        #         return head
        return removeNthHelper(head, findListLenght(head)-n+1, n)