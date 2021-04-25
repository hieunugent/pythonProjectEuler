def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
      
    if n == 0:
        return nums1
    current = 0
    for i in range(n):
        if nums1[i] > nums2[current]:
            nums1[i], nums2[current] = nums2[current], nums1[i]
        nums2.sort()
    for i in range(n):
        nums1[m+i], nums2[i] = nums2[i], nums1[m+i]
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val >= l2.val:
            result = ListNode(val = l2.val, next = None)
            l2 = l2.next
        else:
            result = ListNode(val = l1.val, next = None)
            l1 = l1.next
        head = result
        while l1!= None and l2!= None:
            if l1.val <= l2.val:
                temp = ListNode(val= l1.val, next = None)
                l1 = l1.next
            else:
                temp = ListNode(val = l2.val, next = None)
                l2 = l2.next
            result.next = temp
            result = result.next
        if l1 ==None:
            result.next = l2
        elif l2 == None:
            result.next = l1
            print(result)
            
        return head