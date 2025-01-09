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

        def collectLeft(node):
            if not node:
                return
            if node.left:
                result.append(node.val)
                collectLeft(node.left)
            elif node.right:
                result.append(node.val)
                collectLeft(node.right)

        def collectLeaf(node):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            collectLeaf(node.left)
            collectLeaf(node.right)

        def collectRight(node):
            if not node:
                return
            if node.right:
                collectRight(node.right)
                result.append(node.val)
            elif node.left:
                collectRight(node.left)
                result.append(node.val)
        result.append(root.val)

        if root.left:
            collectLeft(root.left)
        
        collectLeaf(root.left)
        collectLeaf(root.right)

        if root.right:
            collectRight(root.right)
            
        return result