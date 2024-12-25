class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # its a bruteforce
        # n = len(nums)
        # for i in range (0, n-1):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False

        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)

            if len(seen)>k:
                seen.remove(nums[i-k])
        return False