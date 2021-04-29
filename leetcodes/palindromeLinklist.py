def isPalindrome(self, head: ListNode) -> bool:
    temp = head
    length = 0
    while temp != None:
            length += 1
            temp = temp.next
    if length <= 1:
            return True
    mid = length//2
    skipmid = False
    if length % 2 != 0:
            skipmid = True
    count = 1
    pointer = head
    reverse = ListNode(val=pointer.val, next=None)
    result = reverse
    while count < mid:
        count += 1
        pointer = pointer.next
        temp = ListNode(val=pointer.val, next=result)
        result = temp
    if skipmid:
            pointer = pointer.next
    pointer = pointer.next
    while pointer != None:
        if pointer.val != result.val:
            return False
        pointer = pointer.next
        result = result.next
    return True
