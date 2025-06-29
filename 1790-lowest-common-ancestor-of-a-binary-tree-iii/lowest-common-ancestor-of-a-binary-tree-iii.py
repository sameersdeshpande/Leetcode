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

        a = p
        b = q

        while a!=b:
            a = q if a is None else a.parent
            b = p if b is None else b.parent
        
        return a
