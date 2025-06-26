class SparseVector:
    def __init__(self, nums: List[int]):
        self.lookup = {}
        for i ,val in enumerate(nums):
            if val != 0:
                self.lookup[i] = val

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.lookup:
            if i in vec.lookup:
                res+= self.lookup[i]*vec.lookup[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)