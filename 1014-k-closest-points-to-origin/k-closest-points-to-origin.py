class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points.sort(key = self.sqaure)

        return points[:k]

    def sqaure(self,point):
        return point[0]**2 + point[1]**2
        