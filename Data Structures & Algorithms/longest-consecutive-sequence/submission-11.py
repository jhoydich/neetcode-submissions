class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return len(nums)
        
        s = set()
        for num in nums:
            s.add(num)
        sorted_nums = sorted(s)
        longest_streak = 1
        
        curr_streak = 1
        #print(sorted_nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                print(sorted_nums[i], sorted_nums[i-1])
                curr_streak += 1
            else:
                if curr_streak > longest_streak:
                    longest_streak = curr_streak
                curr_streak = 1
                
        if curr_streak > longest_streak:
            longest_streak = curr_streak
        return longest_streak
        