class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dumphead = ListNode()
        result = dumphead
        p = l1
        q = l2
        while p or q:
            x = 0
            y = 0
            if p :
                x = p.val
            if q :
                y = q.val   
            temp = x + y + carry
            carry = temp//10
            temp = temp % 10
        
            result.next = ListNode(temp)
            result = result.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry > 0:
            result.next = ListNode(carry)
        
        return dumphead.next  