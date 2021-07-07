def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            if pA is not None:
                pA = pA.next
            else:
                pA = headB
            if pB is not None:
                pB = pB.next
            else:
                pB = headA
        return pA