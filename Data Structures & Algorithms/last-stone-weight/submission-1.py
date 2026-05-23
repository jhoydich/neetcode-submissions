class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        
        

        while len(stones) >= 2:
            stones = sorted(stones)
            s_a = stones.pop(-1)
            s_b = stones.pop(-1)

            if s_a == s_b:
                continue
            elif s_a > s_b:
                stones.append(s_a-s_b)
            else:
                stones.append(s_b-s_a)
        
        if len(stones) == 0:
            return 0


        return stones[0]
        