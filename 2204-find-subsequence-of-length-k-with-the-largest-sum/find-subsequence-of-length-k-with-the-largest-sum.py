class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res=[]
        nums2= nums.copy()
        top_k = sorted(nums, reverse=True)[:k]
        count = Counter(top_k)
        
        # Step 3: Collect elements in original order, respecting count
        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
                if len(res) == k:
                    break
        return res


        