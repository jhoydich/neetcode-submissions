class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l_t = len(temperatures)

        if l_t == 1:
            return [0]
        res = [0 for i in range(l_t)] 
        for i in range(l_t - 2, -1, -1):
            
                
            check_idx = i + 1
            while check_idx < l_t and temperatures[check_idx] <= temperatures[i]:
                if res[check_idx] == 0:
                    check_idx = l_t
                    break
                check_idx += res[check_idx]
            if check_idx < l_t:
                res[i] = check_idx - i
            
        return res
                
            

            