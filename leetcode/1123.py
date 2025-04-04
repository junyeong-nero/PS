# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        d = []
        cur_depth = -1
        nodes = {}

        def dfs(cur, his, depth):
            nonlocal cur_depth, d
            nodes[cur.val] = cur
            
            if not cur.left and not cur.right:
                # leaf node
                # print(cur.val, his)
                if cur_depth < depth:
                    cur_depth = depth
                    d = his[:] + [cur.val]
                elif cur_depth == depth:
                    temp = []
                    p = set(his)
                    for i in range(len(d) - 1, -1, -1):
                        value = d[i]
                        if value in p:
                            temp.append(value)
                    d = temp[::-1]
                return

            his.append(cur.val)
            if cur.left:
                dfs(cur.left, his, depth + 1)
            
            if cur.right:
                dfs(cur.right, his, depth + 1)
            his.pop()

        dfs(root, [], 0)
        
        # print(d)
        # print(cur_depth)
        # print(nodes)

        return nodes[d[-1]]



