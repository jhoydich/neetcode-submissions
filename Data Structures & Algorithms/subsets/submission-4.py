

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]

        self.buildSub(nums, [], 0)

        return self.res
    
    def buildSub(self, nums: List[int], subset: List[int], i: int):
        if i == len(nums):
            return
        subset.append(nums[i])
        
        self.res.append(subset.copy())
        self.buildSub(nums, subset, i+1)
        subset.pop()
        self.buildSub(nums, subset, i+1)
        