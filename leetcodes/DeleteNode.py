def deleteNode(self, node):
    last = node
    while node.next != None:
        node.val, node.next.val = node.next.val, node.val
        last = node
        node = node.next

    last.next = None
