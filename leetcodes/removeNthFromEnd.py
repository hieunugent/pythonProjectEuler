def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

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
