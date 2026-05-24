class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        self.fresh_fruit = 0
        self.mins = 0

        self.h = len(grid)
        self.w = len(grid[0])
        locs = []

        # count the fresh fruit, and locate the rotten
        for i in range(self.h):
            for j in range(self.w):
                if grid[i][j] == 1:
                    self.fresh_fruit += 1
                elif grid[i][j] == 2:
                    locs.append((i, j))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for loc in locs:
            for d in dirs:
                ci, cj = loc[0]+d[0], loc[1]+d[1]

                # we want a valid index where there is fresh fruit
                if ci >= 0 and ci < self.h and cj >= 0 and cj < self.w and grid[ci][cj] == 1:
                    self.fresh_fruit -= 1
                    m = grid[loc[0]][loc[1]]+1-2
                    if m > self.mins:
                        self.mins = m
                    grid[ci][cj] = grid[loc[0]][loc[1]]+1
                    locs.append((ci, cj))
        
        return -1 if self.fresh_fruit != 0 else self.mins