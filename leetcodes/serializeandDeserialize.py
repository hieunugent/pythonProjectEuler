#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = []
        sign =[]
        def helper(l, s, sign):
            if l == None:
                s+= "#"
                sign.append("False")
            else:
                if l.val < 0:
                    s.append(str((l.val)))
                    sign.append("True")
                else:
                    s.append(str(l.val))
                    sign.append("False")
                helper(l.left, s, sign)
                helper(l.right, s, sign)
                
        helper(root, string, sign)
        return "/".join(string)
                       
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tranfer = data.split("/")
        def buildTree(d): 
            val = d.pop(0)
            tr = TreeNode()
            if val == "#":
                tr = None
            else:
                tr.val = int(val)
                tr.left = buildTree(d)
                tr.right = buildTree(d)
            return tr
        return  buildTree(tranfer)
