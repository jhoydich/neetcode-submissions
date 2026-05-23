class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.bin_search(nums, 0, len(nums)-1)
    
    def bin_search(self, nums, low, high) ->int:
        print(low, high)
        if low > high:
            return nums[high]
        
        m = (low + high) // 2
        if nums[m] < nums[m-1]:
            return nums[m]
        if nums[low] > nums[m]:
            return self.bin_search(nums, low, m-1)
        elif  nums[m] > nums[high]:
            return self.bin_search(nums, m+1, high)
        return nums[low]
        


