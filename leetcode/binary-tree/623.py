# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        q = deque([root])
        if depth == 1:
            return TreeNode(val, left=root)

        cur_depth = 1
        while q:

            if cur_depth == depth - 1:
                break

            for i in range(len(q)):
                tar = q.popleft()
                if tar.left:
                    q.append(tar.left)
                if tar.right:
                    q.append(tar.right)

            cur_depth += 1

        def func(node):
            left, right = TreeNode(val, left=node.left), TreeNode(val, right=node.right)
            node.left = left
            node.right = right
            return node

        # print([node.val for node in q])
        for node in q:
            func(node)

        return root
