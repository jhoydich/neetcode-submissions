import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.graph = {}
        self.checked_nodes = 0
        self.n = n
        self.k = k
        self.max_time = 0
        for i in range(1, n+1):
            self.graph[i] = {}
        for time in times:
            u, v, t = time[0], time[1], time[2]
            self.graph[u][v] = t

        self.dijkstra()

        if self.checked_nodes != n:
            return -1
        
        return self.max_time
    
    def dijkstra(self):

        costs = {}
        for i in range(1, self.n + 1):
            costs[i] = float('inf')
        

        min_heap = [(0, self.k)]
        it = 0
        while len(min_heap) > 0:
            weight, node = heapq.heappop(min_heap)
            if it < 10:
                print(weight, node)
                it += 1
            if weight < costs[node]:
                costs[node] = weight
                self.checked_nodes += 1
                if weight > self.max_time:
                    self.max_time = weight
                
                for n, w in self.graph[node].items():
                    heapq.heappush(min_heap, (weight + w, n))
        return
            

