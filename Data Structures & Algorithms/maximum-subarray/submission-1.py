class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        return self.d_and_c(0, len(nums)-1)
    def d_and_c(self,l, r):
        if l == r:
            return self.nums[l]
        m = (l+r) //2
        right = self.d_and_c(m+1, r)
        left = self.d_and_c(l, m)

        r_max = self.nums[m+1]
        v = r_max
        for i in range(m+2, r+1):
            v += self.nums[i]
            if v > r_max:
                r_max = v
        l_max = self.nums[m]
        v = l_max
        for i in range(m-1, l-1, -1):
            v += self.nums[i]
            if v > l_max:
                l_max = v
        return max(right, left, r_max + l_max)