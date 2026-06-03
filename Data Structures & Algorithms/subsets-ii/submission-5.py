class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        self.res = []

        # TODO
        self.buildSubsets(nums, [], 0)
        return self.res
    
    def buildSubsets(self, nums, subset, i):
        self.res.append(subset.copy())
        if len(nums) == i:
            return
        
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            
            subset.append(nums[j])
            self.buildSubsets(nums, subset, j+1)
            subset.pop()