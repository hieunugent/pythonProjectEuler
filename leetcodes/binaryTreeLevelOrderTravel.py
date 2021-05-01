def levelOrder(self, root: TreeNode) -> List[List[int]]:
    stack = []
    stack.append(root)
    result = []
    while stack:
            temp = []
            tempstack = []
            while stack:
                tempNode = stack.pop(0)
                if tempNode == None:
                    continue
                temp.append(tempNode.val)
                tempstack.append(tempNode.left)
                tempstack.append(tempNode.right)
            stack = tempstack
            if temp:
                result.append(temp)
                print(temp)
    return result
