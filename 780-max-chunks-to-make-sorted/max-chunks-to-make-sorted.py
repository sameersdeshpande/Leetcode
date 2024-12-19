class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxnumber = -1
        chuck_count = 0

        for i in range(len(arr)):
            maxnumber = max(maxnumber, arr[i])

            if maxnumber == i:
                chuck_count+=1
        return chuck_count