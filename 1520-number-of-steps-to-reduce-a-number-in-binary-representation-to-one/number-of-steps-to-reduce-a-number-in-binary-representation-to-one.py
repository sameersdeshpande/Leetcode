class Solution:
    def numSteps(self, s: str) -> int:
        # Step 1: Convert the binary string to an integer
        num = int(s, 2)
        
        # Step 2: Initialize a variable to track the number of steps
        steps = 0
        
        # Step 3: Loop until the number becomes 1
        while num > 1:
            if num % 2 == 0:  # Even number
                num //= 2  # Divide by 2
            else:  # Odd number
                num += 1  # Add 1
            steps += 1  # Increment step count
        
        # Step 4: Return the number of steps
        return steps
