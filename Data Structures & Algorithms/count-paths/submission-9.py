class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        self.res = [[-1 for i in range(n)] for j in range(m)]
        self.res[-1][-1] = 1
        locs = [(m-1, n-1)]
        dirs = [(-1, 0), (0, -1)]

        for loc in locs:
            
            if loc[0] + 1 < m:
                self.res[loc[0]][loc[1]] += self.res[loc[0]+1][loc[1]]
            if loc[1] + 1 < n:
                self.res[loc[0]][loc[1]] += self.res[loc[0]][loc[1]+1] 

            for d in dirs:
                ci, cd = d[0] + loc[0], d[1] + loc[1]
                if ci >= 0 and cd >= 0 and self.res[ci][cd] == -1:
                    self.res[ci][cd] = 0
                    locs.append((ci, cd))
        print(self.res)
        return self.res[0][0]
    