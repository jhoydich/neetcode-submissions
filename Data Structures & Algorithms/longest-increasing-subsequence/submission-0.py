class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums
        lis = [0 for i in range(len_nums)]
        lis[0] = 1
        max_lis = 1

        for i in range(1, len_nums):
            cur_max = 1
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if lis[j] + 1 > cur_max:
                    cur_max = lis[j] + 1
            lis[i] = cur_max
            if cur_max > max_lis:
                max_lis = cur_max

        return max_lis # think about this



