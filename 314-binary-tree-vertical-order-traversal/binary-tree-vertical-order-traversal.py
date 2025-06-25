# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        colum = defaultdict(list)


        queue = deque([(root,0)])

        while queue:
            node,col = queue.popleft()
            if node:
                colum[col].append(node.val)
                queue.append((node.left, col-1))
                queue.append((node.right,col+1))
            
        sorted_columns = sorted(colum.keys())

        return [colum[col] for col in sorted_columns]



        