class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i= 0
        length = len(nums)
        sol = []
        while i < length:
            if i > 0:
                while i < length and nums[i] == nums[i-1]:
                    i += 1
            if i == length:
                break
            j = i + 1
            k = length - 1
            target = nums[i]
            
            while j < k:
                v = -1 * (nums[j] + nums[k])
                if v == target:
                    sol.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<length and nums[j] == nums[j-1]:
                        j += 1
                elif v < target:
                    k -= 1
                    while k>=0 and nums[k] == nums[k+1]:
                        k -= 1
                    
                elif v > target:
                    j += 1
                    while j<length and nums[j] == nums[j-1]:
                        j += 1
                
            i += 1
        return sol
                

        