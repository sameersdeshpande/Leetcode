class Solution:

    def __init__(self, w: List[int]):
        self.sum=[]
        sums = 0
        for weight in w:
            sums+= weight
            self.sum.append(sums)
        self.totalsum = sums
        

    def pickIndex(self) -> int:
        rand = self.totalsum*random.random()
        for i,sums in enumerate(self.sum):
            if rand <=sums:
                return i
        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()