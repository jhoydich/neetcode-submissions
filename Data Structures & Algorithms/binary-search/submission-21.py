class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, len(nums)-1, 0, target)
    def bin_search(self,nums, high, low, target) -> int:
        print(high, low)
        if low > high:
           return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.bin_search(nums, mid-1, low, target)
        else:
            return self.bin_search(nums, high, mid+1, target)

        return -1