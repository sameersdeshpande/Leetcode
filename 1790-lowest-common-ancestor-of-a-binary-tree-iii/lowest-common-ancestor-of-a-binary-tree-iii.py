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
        ancestors = set()
        
        # Track all ancestors of p (including p itself)
        while p:
            ancestors.add(p)
            p = p.parent
        
        # Move up from q until we find an ancestor in p's set
        while q not in ancestors:
            q = q.parent
        
        return q