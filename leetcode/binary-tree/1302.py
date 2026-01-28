# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        level_sum = 0

        while q:

            level_sum = 0
            for i in range(len(q)):
                tar = q.popleft()
                level_sum += tar.val

                if tar.left:
                    q.append(tar.left)
                if tar.right:
                    q.append(tar.right)

        return level_sum
