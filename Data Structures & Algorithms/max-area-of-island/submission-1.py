class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        self.maxArea = 0
        self.grid = grid
        self.w = len(self.grid[0])
        self.h = len(self.grid)
        self.iter_islands()
        return self.maxArea

    def explore(self, i, j):
        dirs = [[-1, 0], [1,0], [0,-1], [0,1]]
        szCount = 1
        for d in dirs:
            ci, cj = d[0], d[1]
            if i+ci >= 0 and i+ci < self.h and j+cj >= 0 and j+cj < self.w and self.grid[i+ci][j+cj] == 1:
                self.grid[i+ci][j+cj] = 0
                szCount += self.explore(i+ci, j+cj)

        return szCount

    def iter_islands(self):    
        # iter over the map
        for i in range(0, self.h):
            for j in range(self.w):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    sz = self.explore(i, j)
                    if sz > self.maxArea:
                        self.maxArea = sz

    