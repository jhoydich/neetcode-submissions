class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        rev = s[::-1]
        n = len(s)
        matched = [[0] * n for _ in range(n)]
        
        max_substr = 0
        idx = -1
        for i in range(n):
            for j in range(n):
                if s[i] == rev[j]:
                    val = matched[i-1][j-1] if i > 0 and j > 0 else 0
                    matched[i][j] = val + 1
                    length = val + 1
                    if length > max_substr and (i + 1 - length) == (n - 1 - j):
                        max_substr = length
                        idx = i
        
        return s[idx+1-max_substr : idx+1]