class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create map
        d = dict()
        
        # iterate over strings, check if sorted version is in map
        for s in strs:
            temp_s = "".join(sorted(s))
            if temp_s in d:
                d[temp_s].append(s)
            else:
                d[temp_s] = [s]
        output = []
        for k in d:
            output.append(d[k])
        return output
        