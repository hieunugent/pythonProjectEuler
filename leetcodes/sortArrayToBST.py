def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def sorttoBST(nums):
            if not nums:
                return None
            mid = (len(nums))//2
            root = TreeNode(nums[mid])
            root.left = sorttoBST(nums[:mid])
            root.right = sorttoBST(nums[mid+1:])
            return root
    return sorttoBST(nums)
