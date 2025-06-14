from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            # Base case: path is a complete permutation
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy of path
                return

            # Try each number that hasn't been used
            for i in range(len(nums)):
                if used[i]:
                    continue  # Skip if already in path

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack(path, used)

                # Un-choose (backtrack)
                path.pop()
                used[i] = False

        # Start backtracking with empty path and no numbers used
        backtrack([], [False] * len(nums))
        return result
