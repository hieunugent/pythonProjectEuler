# print([1]+ [0]*10)
A = [1,6,3,4,5,2,7]
B = A
# print(B)
C = list(A)
# /print(C)
E=A[:]

# print(A[4:0:-2])


A[0], A[len(A)-1]= A[len(A)-1], A[0]

class BST: 
    def __init__(self, val): 
        self.val = val
        self.right = None
        self.left = None
def insert(root, key):
    if root is None: 
        return BST(key)
    else: 
        if root.val == key: 
            return root
        elif root.val < key: 
            root.right= insert(root.right, key)
        else: 
            root.left = insert(root.left, key)
    return root

A = [100,20,500,10 , 30 ,400, 600]
tree = BST(100)
for a in A: 
    tree = insert(tree, a)

result = []
curr_depth_node = [tree]
while curr_depth_node: 
    result.append([curr.val for curr in curr_depth_node])
    curr_depth_node = [child for curr in curr_depth_node 
                for child in (curr.left, curr.right) if child]
# print(result)
# implement the queue by stack, we using 2 stack
#  to implement a queue FIFO, stack LIFO
#  



