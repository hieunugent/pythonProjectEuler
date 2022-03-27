def middleNode(head):
    mid = head
    counts = head
    midvalue = 1
    while counts.next != None:
            midvalue += 1
            counts = counts.next
    midvalue = midvalue//2
    while midvalue > 0:
            mid = mid.next
            midvalue -= 1
    return mid
