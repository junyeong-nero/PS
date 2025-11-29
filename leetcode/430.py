"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":

        def connect(cur):
            prev = cur
            while cur:
                if cur.child:
                    node = connect(cur.child)
                    node.next = cur.next
                    temp = cur.next
                    cur.child.prev = cur
                    cur.next = cur.child
                    cur.child = None
                    if temp:
                        temp.prev = node
                    prev = node
                    cur = temp
                else:
                    prev = cur
                    cur = cur.next

            return prev

        connect(head)
        return head
