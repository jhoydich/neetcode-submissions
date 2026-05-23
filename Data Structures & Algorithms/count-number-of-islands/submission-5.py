class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        self.visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        self.num_islands = 0
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])
        # explore islands
        self.iterislands()
        return self.num_islands
    
    def explore(self, i, j):
        if i - 1 >= 0 and self.grid[i-1][j] == "1" and self.visited[i-1][j] == 0:
            self.visited[i-1][j] = 1
            self.explore(i-1,j)
        if i + 1 < self.h and self.grid[i+1][j] == "1" and self.visited[i+1][j] == 0:
            self.visited[i+1][j] = 1
            self.explore(i+1,j)
        if j - 1 >= 0 and self.grid[i][j-1] == "1" and self.visited[i][j-1] == 0:
            self.visited[i][j-1] = 1
            self.explore(i,j-1)
        if j + 1 < self.w and self.grid[i][j+1] == "1" and self.visited[i][j+1] == 0:
            self.visited[i][j+1] = 1
            self.explore(i,j+1)
        
        

    def iterislands(self):

        for i in range(self.h):
            for j in range(self.w):
                #print(i, j, self.grid[i][j], self.visited[i][j])
                if self.grid[i][j] == "1" and self.visited[i][j] == 0:
                    self.num_islands += 1
                    self.visited[i][j] = 1
                    self.explore(i, j)
                elif self.visited[i][j] == 0:
                    self.visited[i][j] = 1
    