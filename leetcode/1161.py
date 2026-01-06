# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        levels = []

        while q:

            value = 0
            for _ in range(len(q)):
                tar = q.popleft()
                value += tar.val
                if tar.left:
                    q.append(tar.left)
                if tar.right:
                    q.append(tar.right)

            levels.append(value)

        print(levels)
        return levels.index(max(levels)) + 1
