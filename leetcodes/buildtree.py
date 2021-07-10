class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def arraytotree(left, right):
            nonlocal preorder_index
            if left < right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index +=1


            root.left  = arraytotree(left, inorder_indexmap[root_value]-1)
            root.right = arraytotree(inorder_indexmap[root_value]+1, right)

            return root
        preorder_index = 0
        inorder_indexmap ={}
        for index, value in enumerate(inorder):
            inorder_indexmap[value] = index
        return arraytotree(0, len(preorder)-1)
