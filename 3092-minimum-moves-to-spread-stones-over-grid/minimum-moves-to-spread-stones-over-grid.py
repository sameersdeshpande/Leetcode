class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        answ,zeros,d = 100,[],[]
        for r in range(3):
            for c in range(3):
                if grid[r][c]==0:
                    zeros.append((r,c))
                elif grid[r][c]>1:
                    d+=[(r,c)]*(grid[r][c]-1)
                    
        for p in itertools.permutations(d):
            actual=0   
            for (r,c),(R,C) in zip(zeros,p):
                actual+=abs(R-r)+abs(C-c)
            answ=min(answ,actual)
                    
        return answ      