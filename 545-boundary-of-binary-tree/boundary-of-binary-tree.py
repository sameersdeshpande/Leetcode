# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        # Helper function to collect left boundary (excluding the leaves)
        def collectLeftBoundary(node):
            if not node:
                return
            if node.left:
                result.append(node.val)
                collectLeftBoundary(node.left)
            elif node.right:  # if there's no left child but there's a right child
                result.append(node.val)
                collectLeftBoundary(node.right)

        # Helper function to collect leaves (we don't include root)
        def collectLeaves(node):
            if not node:
                return
            if not node.left and not node.right:  # it's a leaf node
                result.append(node.val)
            collectLeaves(node.left)
            collectLeaves(node.right)

        # Helper function to collect right boundary (reverse order)
        def collectRightBoundary(node):
            if not node:
                return
            if node.right:
                collectRightBoundary(node.right)
                result.append(node.val)
            elif node.left:  # if there's no right child but there's a left child
                collectRightBoundary(node.left)
                result.append(node.val)

        # Collect root
        result.append(root.val)

        # Collect left boundary (excluding the root and leaves)
        if root.left:
            collectLeftBoundary(root.left)

        # Collect leaves (excluding the root)
        collectLeaves(root.left)
        collectLeaves(root.right)

        # Collect right boundary (excluding the root and leaves, in reverse order)
        if root.right:
            collectRightBoundary(root.right)

        return result
