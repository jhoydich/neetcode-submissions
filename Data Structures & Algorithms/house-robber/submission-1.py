class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        self.loot = [0 for i in range(len(nums))]
        self.loot[0] = nums[0]

        for i in range(1, len(nums)):
            cash = nums[i]
            oh, th = 0, 0
            if i - 2 >= 0:
                oh = self.loot[i-2]
            if i - 3 >= 0:
                th = self.loot[i-3]
            self.loot[i] = cash + max(oh, th)
        return max(self.loot[-1], self.loot[-2])
        