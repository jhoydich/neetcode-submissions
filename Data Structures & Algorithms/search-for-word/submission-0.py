class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.h = len(board)
        self.w = len(board[0])
        self.word = word
        self.visited = [[0 for i in range(self.w)] for j in range(self.h)]

        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] == word[0]:
                    res = self.DFS(i, j, 1)
                    if res == True:
                        return True
        

        return False
            


    def DFS(self, i, j, idx) -> bool:
        if idx == len(self.word):
            return True
        self.visited[i][j] = 1
        
        s_v = self.word[idx]
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for d in dirs:
            ci, cj = i + d[0] , j + d[1]
            if ci < 0 or ci == self.h or cj < 0 or cj == self.w or self.visited[ci][cj] == 1:
                continue
            
            if self.board[ci][cj] == s_v:
                res = self.DFS(ci, cj, idx + 1)
                if res == True:
                    return True

        self.visited[i][j] = 0
        return False