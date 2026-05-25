class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        self.grid = [[0 for i in range(len(text2) + 1)]for j in range(len(text1) + 1)]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                m_val = 0
            
                
                if text1[i] == text2[j]:
                    m_val = 1 + self.grid[i][j]
                else:
                    m_val = max(self.grid[i][j+1], self.grid[i+1][j])
                self.grid[i+1][j+1] = m_val


        return self.grid[-1][-1]