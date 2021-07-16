class Solution:       
    def connect(self, root: 'Node') -> 'Node':
        def getnextright(p: 'Node')->'Node':
            current = p.next
            while current != None:
                if current.left != None:
                    return current.left
                if current.right != None:
                    return current.right
                current = current.next
            return None
        if not root:
            return 
        root.next = None
        p = root
        while p != None:
            q = p
            while q != None:
                if q.left:
                    if q.right:
                        q.left.next = q.right
                    else:
                        q.left.next = getnextright(q)
                if q.right:
                    q.right.next = getnextright(q)
                q = q.next
            if p.left:
                p = p.left
            elif p.right:
                p = p.right
            else:
                p = getnextright(p)
        return root