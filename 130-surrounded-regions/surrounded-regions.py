class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r>= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='E':
                    board[i][j]='O'
