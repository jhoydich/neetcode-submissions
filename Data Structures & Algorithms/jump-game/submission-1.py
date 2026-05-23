class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1
        if len(nums) == 1:
            return True
        i = final - 1
        while i > -1:
            if nums[i] + i >= final:
                final = i
            i -= 1

        if final == 0:
            return True
        return False