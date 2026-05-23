class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, 0, len(nums) - 1, target)
    def bin_search(self, nums: List[int], low: int, high:int, target:int)-> int:
        if low > high:
            return -1

        # get the mid point
        m = (low + high) // 2

        # check if the mid point equals the target
        if nums[m] == target:
            return m
        
        # conditions to go right or left
        # normal conditions
        print(low, m, high)
        # go to the right as target is between mid and high and there's no inversion
        if nums[m] < target <= nums[high] or target <= nums[high] < nums[m] or nums[high] <= nums[m] <= target:
            return self.bin_search(nums, m+1, high, target)
        # go to left as target is between low and mid
        elif nums[low] <= target < nums[m] or target <= nums[m] <= nums[low] or nums[m] <= target <= nums[low]:
            return self.bin_search(nums, low, m-1, target)
        return -1