class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        self.steps = [0 for i in range(n)]
        self.steps[0] = 1
        for i in range(1, n):
            prev_c = self.steps[i-1]
            prev_2c = 1
            if i - 2 >= 0:
                prev_2c = self.steps[i-2]
            self.steps[i] = prev_c + prev_2c
        return self.steps[-1]
