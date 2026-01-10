# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        parents = dict()

        def find_deepest_nodes(node):
            q = deque([node])
            levels = []

            while q:

                for i in range(len(q)):
                    tar = q.popleft()
                    levels.append(tar)
                    if tar.left:
                        q.append(tar.left)
                        parents[tar.left.val] = tar
                    if tar.right:
                        q.append(tar.right)
                        parents[tar.right.val] = tar

                if q:
                    levels.clear()

            return node, levels

        def find_common_ancestor(nodes):

            if len(nodes) == 1:
                return nodes[0]

            ancestors = set(nodes)
            while len(ancestors) > 1:
                ancestors = set(
                    [parents[node.val] for node in ancestors if node.val in parents]
                )

            return list(ancestors)[0]

        root, deepest = find_deepest_nodes(root)
        # print(deepest)

        res = find_common_ancestor(deepest)
        # print(res)

        return res
