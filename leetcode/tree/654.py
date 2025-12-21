# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            # print(arr)
            max_value = max(arr)
            max_index = arr.index(max_value)

            node = TreeNode(max_value)
            node.left = build(arr[:max_index])
            node.right = build(arr[max_index + 1:])

            return node

        res = build(nums)
        return res

