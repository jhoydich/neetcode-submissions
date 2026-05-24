class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if len(grid) == 0:
            return
        
        self.h = len(grid)
        self.w = len(grid[0])

        treasure_locs = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure_locs.append([i,j])
        
        for loc in treasure_locs:
            
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in dirs:
                ci, cj = loc[0]+d[0], loc[1]+d[1]
                if ci >= 0 and ci < self.h and cj >= 0 and cj < self.w and grid[ci][cj] == 2147483647:
                    grid[ci][cj] = grid[loc[0]][loc[1]] + 1
                    treasure_locs.append([ci, cj])
