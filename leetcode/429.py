"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:

        if not root:
            return []

        q = deque([root])
        levels = []
        while q:
            levels.append([])
            for i in range(len(q)):
                tar = q.popleft()
                levels[-1].append(tar.val)
                q.extend(tar.children)

        return levels
