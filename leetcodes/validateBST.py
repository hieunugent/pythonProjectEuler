def isValidBST(self, root: TreeNode) -> bool:
    if not root:
            return True
    stack = [(root, -math.inf, math.inf)]
    while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
    return True
