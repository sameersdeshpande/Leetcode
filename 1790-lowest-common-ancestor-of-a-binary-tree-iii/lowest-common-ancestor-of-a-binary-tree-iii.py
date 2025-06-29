"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # ancestors = set()
        # while p:
        #     ancestors.add(p)
        #     p = p.parent
        # while q not in ancestors:
        #     q = q.parent
        # return q

        a, b = p, q
        while a != b:
            a = q if a is None else a.parent
            b = p if b is None else b.parent
        return a