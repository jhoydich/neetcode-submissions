class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        self.buildSums(nums, [], target, 0)
        return self.res

    def buildSums(self, nums: List[int], subset: List[int], target: int, i: int):
        s = sum(subset)
        if s >= target:
            if s == target:
                self.res.append(subset.copy())
            return
        
        for j in range(i, len(nums)):
            v = nums[j]
            subset.append(v)
            self.buildSums(nums, subset, target, j)
            subset.pop()        