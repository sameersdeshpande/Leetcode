class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()  # Sort the array first
        closest_sum = float('inf')  # Initialize with a large value
        
        # Loop through each element of the array
        for i in range(len(nums) - 2):
            # Avoid duplicate elements for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find the closest sum for each fixed element
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison with the target
                if current_sum < target:
                    left += 1  # We need a larger sum, move left pointer to the right
                elif current_sum > target:
                    right -= 1  # We need a smaller sum, move right pointer to the left
                else:
                    return current_sum  # Exact match, return the sum immediately
        
        return closest_sum  # Return the closest sum found

