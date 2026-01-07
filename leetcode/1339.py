# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        history = []

        def func(root):
            if not root:
                return 0

            temp = root.val + func(root.left) + func(root.right)
            history.append(temp)
            return temp

        total = func(root)
        history = sorted(history)

        # print(history)
        i = bisect_left(history, total // 2)

        MOD = 10**9 + 7

        res = (total - history[i]) * history[i]
        res = max(res, (total - history[i - 1]) * history[i - 1])

        return res % MOD
