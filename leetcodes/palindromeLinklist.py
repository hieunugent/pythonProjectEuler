def isPalindrome(head):
    temp = head
    length = 0
    while temp != None:
            length +=1
            temp =temp.next
    mid = length//2
    skipmid = False
    if length %2 != 0:
            skipmid = True
    count = 0
    pointer = head
    reverse =[]
    while count < mid:
            count +=1
            current = ListNode(val =pointer.val, next = None)
            current.next = reverse
            reverse = current
            pointer = pointer.next
    if skipmid:
            pointer = pointer.next
    pointer = pointer.next
       
    while pointer!= None:
            if pointer.val != reverse.val:
                return False
            pointer = pointer.nextS
            reverse = reverse.next
    return True
