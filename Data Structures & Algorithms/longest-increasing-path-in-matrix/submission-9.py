class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        self.matrix = matrix
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.grid = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        self.m_path = 0

        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] == -1:
                    self.DFS(i,j)
        
        return self.m_path

    def DFS(self, i, j):
        self.grid[i][j] = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        paths = [1]
        for d in dirs:
            ci, cd = i+d[0], j+d[1]
            
            if ci >= 0 and cd >= 0 and ci < self.h and cd < self.w and self.matrix[ci][cd] > self.matrix[i][j]:
                if self.grid[ci][cd] == -1:
                    
                    self.DFS(ci, cd)
                paths.append(self.grid[ci][cd]+1)
        mp = max(paths)
        if mp > self.m_path:
            self.m_path = mp
        self.grid[i][j] = mp 