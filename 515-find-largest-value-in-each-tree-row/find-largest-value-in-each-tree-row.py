# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
                level_size = len(queue)  # Number of nodes at the current level
                level_max = float('-inf')  # Start with the smallest possible value
                
                # Process all nodes at the current level
                for _ in range(level_size):
                    node = queue.popleft()  # Dequeue the front node
                    level_max = max(level_max, node.val)  # Update the max value for this level
                    
                    # Enqueue the left and right children if they exist
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                # After processing the current level, add the max value to the result list
                result.append(level_max)
            
        return result