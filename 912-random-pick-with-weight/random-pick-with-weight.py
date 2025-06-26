class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        psum = 0

        for weight in w:
            psum+=weight
            self.sums.append(psum)
        self.total = psum
        

    def pickIndex(self) -> int:
        ra = self.total * random.random()
        for i , psum in enumerate(self.sums):
            if ra < psum:
                return i

        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()