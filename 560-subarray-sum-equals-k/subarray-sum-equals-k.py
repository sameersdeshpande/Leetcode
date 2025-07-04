class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0

        prefix_sum_count = defaultdict(int)

        prefix_sum_count[0] = 1

        for i , num in enumerate(nums):
            current_sum += num

            if current_sum - k in prefix_sum_count:
                count+= prefix_sum_count[current_sum-k]
            
            prefix_sum_count[current_sum]+=1
        return count

        

        