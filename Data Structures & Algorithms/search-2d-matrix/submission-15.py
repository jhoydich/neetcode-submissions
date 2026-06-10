class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.h = len(matrix)
        if self.h == 0:
            return False
        self.w = len(matrix[0])
        n_elements = self.h * self.w
        left, right = 0, n_elements - 1
        if matrix[0][0] == target:
            return True
        while right - left > 1:
            m = (right + left) // 2
            r, c = self.calc_coord(m)
            if matrix[r][c] < target:
                left = m
            else:
                right = m
        r, c = self.calc_coord(right)
        if matrix[r][c] == target:
            return True
        return False
    def calc_coord(self, idx):
        row = idx // self.w
        col = idx % self.w
        return [row, col]

     