class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        newset = set(arr)
        res =[]
        max_i = max(arr)
        for i in range(1, max_i+k+1):
            if i not in newset:
                res.append(i)
        return res[k-1]
        