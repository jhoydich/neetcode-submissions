class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.steps = [0 for i in range(len(cost))]

        for i in range(2, len(cost)):
            self.steps[i] = min(self.steps[i-1]+cost[i-1], self.steps[i-2]+cost[i-2])

        return min(self.steps[-1]+cost[-1], self.steps[-2]+cost[-2])

        