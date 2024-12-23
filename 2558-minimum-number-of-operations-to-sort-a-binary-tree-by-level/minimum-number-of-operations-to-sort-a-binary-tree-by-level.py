# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        total_swaps = 0

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total_swaps += self._get_min_swaps(level_values)
        return total_swaps

    def _get_min_swaps(self,level_values):
        swaps = 0
        target = sorted(level_values)
        pos = {val:idx for idx, val in enumerate(level_values)}

        for i in range(len(level_values)):
            if level_values[i] != target[i]:
                swaps +=1
                cur_pos = pos[target[i]]
                pos[level_values[i]] = cur_pos
                level_values[cur_pos] = level_values[i]

            

            
        return swaps