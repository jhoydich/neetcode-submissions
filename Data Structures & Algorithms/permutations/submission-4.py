class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        # TODO: call funcion
        self.find_perms(nums, [])
        return self.res

    def find_perms(self, nums, subset):
        if len(nums) == 0:
            self.res.append(subset.copy())
            return
        
        for i in range(len(nums)):
            s = subset.copy()
            s.append(nums[i])
            n = nums[:i]
            if i+1 < len(nums):
                n += nums[i+1:]
            self.find_perms(n, s)
