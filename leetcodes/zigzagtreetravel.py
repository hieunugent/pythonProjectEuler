def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = []
        result = []
        if root :
            stack.append(root)
        oddlevel = False
        while stack:
            tempstack = []
            tempresult = []
            while stack:
                current = stack.pop()
                if oddlevel:
                    if current.right: tempstack.append(current.right)
                    if current.left: tempstack.append(current.left)
                else:
                    if current.left: tempstack.append(current.left)
                    if current.right: tempstack.append(current.right)
                tempresult.append(current.val)
            stack = tempstack
            oddlevel = not oddlevel
            print(oddlevel)
            result.append(tempresult)
        return result