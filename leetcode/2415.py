from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        level = 0

        while q:
            n = len(q)
            # Collect values of the current level if it is an odd level
            if level % 2 == 1:
                values = [node.val for node in q]
                # Reverse the values and reassign to nodes
                for i in range(n):
                    q[i].val = values[-(i + 1)]

            # Add the next level of nodes to the queue
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return root
