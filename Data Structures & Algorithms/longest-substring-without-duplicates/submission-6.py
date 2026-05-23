class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # check if our string is length 1 or 0
        length = len(s)
        if length <= 1:
            return length

        # create our hashtable
        window_set = set()

        # initialize our set and variables
        i, j = 0, 1
        window_set.add(s[i])
        maxLen = 0

        # iterate until j gets to the end
        while j < length:
            while s[j] in window_set:
                window_set.remove(s[i])
                i += 1
                if i == j:
                    break
            
            window_set.add(s[j])
            print(i, j)
            if j - i + 1 > maxLen:
                maxLen = j-i + 1

            j += 1
        return maxLen
        
        
                

            

            