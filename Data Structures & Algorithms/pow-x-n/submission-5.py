class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = x
        if n == 0:
            return 1
        elif n > 0:
            for i in range(n-1):
                x = x * num
        else:
            for i in range((-1*n)+1):
                x = x / num
                print(x)
        return x