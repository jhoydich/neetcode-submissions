import heapq
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        fleets = 0
        slowest = -1
        # make tuples
        data = []
        for i in range(len(position)):
            data.append((position[i], speed[i]))

        heapq.heapify_max(data)
        while len(data) != 0:
            furthest = heapq.heappop_max(data)
            toa = (target - furthest[0]) / furthest[1]
            if toa > slowest:
                slowest = toa
                fleets += 1
        return fleets