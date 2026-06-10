class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return left

        while right - left > 1:
            m = (right + left) // 2
            bef = self.isBefore(target, left, right, m)
            if bef:
                left = m
            else:
                right = m
        
        if nums[right] == target:
            return right
        return -1
    

    def isBefore(self, target, left, right, mid):
        if self.nums[left] <= target <= self.nums[mid]:
            return False
        elif self.nums[mid] < self.nums[left] <= target:
            return False
        elif target <= self.nums[mid] < self.nums[left]:
            return False
        return True