class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Construct the adjacency list for the tree
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # To count the valid components
        self.count = 0
        
        # DFS function to calculate the sum of the subtree rooted at each node
        def dfs(node, parent):
            subtree_sum = values[node]
            
            # Visit all the children (neighbors)
            for neighbor in graph[node]:
                if neighbor != parent:  # Avoid going back to the parent
                    subtree_sum += dfs(neighbor, node)
            
            # If the subtree sum is divisible by k, we can cut the edge to form a new component
            if subtree_sum % k == 0:
                self.count += 1
                return 0  # We return 0 to indicate this subtree is now a valid component
            return subtree_sum
        
        # Start DFS from the root node (node 0)
        dfs(0, -1)
        
        # The result is the total count of valid components
        return self.count
