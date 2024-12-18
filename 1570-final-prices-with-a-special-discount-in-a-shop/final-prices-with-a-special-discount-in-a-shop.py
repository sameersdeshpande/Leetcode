class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # Stack to store indices of prices
        stack = []
        # Result array to store final prices
        result = prices[:]
        
        # Traverse the list from right to left
        for i in range(len(prices) - 1, -1, -1):
            # Pop elements from the stack that are greater than prices[i]
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            
            # If stack is not empty, apply the discount
            if stack:
                result[i] = prices[i] - prices[stack[-1]]
            
            # Push current index onto the stack
            stack.append(i)
        
        return result
