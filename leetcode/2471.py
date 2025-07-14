# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        res = 0

        def count_swap(arr):
            res = 0
            mp = {x: i for i, x in enumerate(sorted(arr))}
            visited = [0] * len(arr)
            for i in range(len(arr)):
                cnt = 0
                while not visited[i] and i != mp[arr[i]]:
                    visited[i] = 1
                    cnt += 1
                    i = mp[arr[i]]
                res += max(0, cnt - 1)
            return res

        while q:

            n = len(q)
            arr = []
            for i in range(n):
                tar = q.popleft()
                arr.append(tar.val)
                if tar.left:
                    q.append(tar.left)
                if tar.right:
                    q.append(tar.right)

            res += count_swap(arr)

        return res
