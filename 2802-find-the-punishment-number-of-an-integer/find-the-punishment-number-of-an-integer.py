class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        # Helper function to check if a number can be partitioned to sum to the original number
        def can_partition(num: int, target: int) -> bool:
            num_str = str(num)
            length = len(num_str)
            
            # Try all possible ways to partition num_str into substrings
            # We will use a recursive approach to generate all partition sums
            def dfs(idx, current_sum):
                if idx == length:
                    return current_sum == target
                
                # Try all possible partitions starting from idx
                value = 0
                for i in range(idx, length):
                    value = value * 10 + int(num_str[i])  # Add the digit to the current substring
                    if current_sum + value > target:
                        break  # If sum exceeds target, no need to check further
                    if dfs(i + 1, current_sum + value):  # Continue to the next substring
                        return True
                return False
            
            # Start dfs from index 0 and initial sum 0
            return dfs(0, 0)
        
        total = 0
        
        for i in range(1, n + 1):
            square = i * i
            if can_partition(square, i):
                total += square
        
        return total
