class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # Memoization dictionary to store intermediate results
        
        def dfs(index, current_sum):
            # Base case: if we've processed all numbers, check if the sum matches the target
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Check if the current state has been computed before
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Explore both the + and - options for the current number
            positive = dfs(index + 1, current_sum + nums[index])
            negative = dfs(index + 1, current_sum - nums[index])
            
            # Memoize and return the result for the current state (index, current_sum)
            memo[(index, current_sum)] = positive + negative
            return memo[(index, current_sum)]
        
        return dfs(0, 0)
