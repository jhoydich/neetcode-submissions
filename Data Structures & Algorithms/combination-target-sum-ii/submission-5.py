class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates = sorted(candidates)
        self.buildSum([], candidates, target, 0, 0)
        return self.res

    def buildSum(self, subset, candidates, target, summation, i):
        

        if summation >= target:
            if summation == target:
                self.res.append(subset.copy())
            return
        
        for j in range(i, len(candidates)):
            if j > i and candidates[j-1] == candidates[j]:
                continue
            v = candidates[j]
            
            subset.append(v)
            self.buildSum(subset, candidates, target, summation+v, j+1)
            subset.pop()

            