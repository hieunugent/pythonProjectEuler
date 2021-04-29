def maxDepth(self, root: TreeNode) -> int:
    stack = []
    if root is None:
            return 0
    stack.append(root)
    level = 0
    while len(stack) > 0:
            temp = []
            while len(stack) > 0:
                node = stack.pop()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            stack = temp
            level += 1
    return level
