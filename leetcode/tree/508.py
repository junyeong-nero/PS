# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        counter = Counter()

        def dfs(cur):
            if not cur.left and not cur.right:
                counter[cur.val] += 1
                return cur.val

            value = cur.val
            if cur.left:
                value += dfs(cur.left)
            if cur.right:
                value += dfs(cur.right)

            counter[value] += 1
            return value

        dfs(root)
        # print(counter)

        res = []
        most_freq = max(counter.values())
        for key in counter:
            if counter[key] != most_freq:
                continue
            res.append(key)

        return res
