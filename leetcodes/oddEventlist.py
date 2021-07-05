def oddEvenList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
            return head
    first = head
    second = head.next
    dump = second
    while first.next and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next
    first.next = dump
    return head
