# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        d = dict()

        def func(cur, depth):
            nonlocal d
            if not cur:
                return depth
            
            right = func(cur.left, depth + 1)
            left = func(cur.right, depth + 1)
            if right == left:
                d[right] = cur
            return max(right, left)

        max_depth = func(root, 0)
        return d[max_depth]


