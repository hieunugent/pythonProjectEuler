def isSymmetric(self, root: TreeNode) -> bool:
    queue = []
    queue.append(root)
    queue.append(root)
    while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
    return True
