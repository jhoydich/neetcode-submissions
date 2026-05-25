class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        v = digits[len(digits)-1] + 1
        carry = v // 10
        digits[len(digits)-1] = v % 10
        
        if carry == 0:
            return digits

        for i in range(len(digits)-2, -1, -1):
            v = digits[i] + carry
            carry = v // 10

            digits[i] = v % 10
            if carry == 0:
                break
        if carry != 0:
            digits.insert(0, 1)
        return digits