class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        rev = nums[::-1]
        forward_prod = [nums[0]]
        rev_prod = [rev[0]]
        # go through list once forwards and backwards
        for i in range(1, length):
            forward_prod.append(nums[i] * forward_prod[i-1])
            rev_prod.append(rev[i] * rev_prod[i-1])

        # reverse reverse!
        rev_prod = rev_prod[::-1]

        # combine result
    
        out = [rev_prod[1]]
        for i in range(1, length-1):
            out.append(forward_prod[i-1]*rev_prod[i+1])
        out.append(forward_prod[-2])

        return out

