# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queque = [root]
        level = 0

        while queque:
            level_size = len(queque)
            current_level = []

            for _ in range (level_size):
                node = queque.pop(0)
                current_level.append(node)
                if node.left:
                    queque.append(node.left)

                
                if node.right:
                    queque.append(node.right)
                
            if level % 2 == 1:
                values = [node.val for node in current_level]
                values.reverse()  # Reverse the values at this level
                for i, node in enumerate(current_level):
                    node.val = values[i]
            
            # Move to the next level
            level += 1
        
        return root



           

            