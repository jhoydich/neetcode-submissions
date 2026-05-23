class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        
        for idx, n in enumerate(nums):
            if n in d:
                return [d[n], idx]
            else:
                d[target-n] = idx
            