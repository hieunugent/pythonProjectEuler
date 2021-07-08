def inorderTraversal(self, root: TreeNode) -> List[int]:
#        left root right
    def helper(root, res):
        if root is not None:
            if root.left is not None:
                helper(root.left, res)
            res.append(root.val)
            if root.right is not None:
                helper(root.right, res)
    res = []
    helper(root, res)
    return res


def inorderTraversal2(self, root: TreeNode) -> List[int]:
    result = []
    stack =[]
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left  
        current = stack.pop()
        result.append(current.val)
        current= current.right
    return result
