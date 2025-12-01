# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def get_height(cur):
            if not cur:
                return 0
            return 1 + max(get_height(cur.left), get_height(cur.right))

        height = get_height(root) - 1
        n = 2 ** (height + 1) - 1
        print(height)

        res = [["" for _ in range(n)] for _ in range(height + 1)]
        print(res)

        def draw(cur):
            q = deque([(cur, 0, (n - 1) / 2)])
            while q:
                tar, row, column = q.popleft()
                res[int(row)][int(column)] = str(tar.val)

                if tar.left:
                    q.append((tar.left, row + 1, column - 2 ** (height - row - 1)))
                if tar.right:
                    q.append((tar.right, row + 1, column + 2 ** (height - row - 1)))

        draw(root)
        return res
