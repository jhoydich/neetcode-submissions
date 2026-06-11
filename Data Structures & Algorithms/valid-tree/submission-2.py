class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        self.adj_list = [[]for i in range(n)]
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
        self.cycle = False
        num_visited = self.dfs()
        if num_visited != n or self.cycle == True:
            return False
        return True

    def dfs(self):
        seen = set()
        self.num_visited = 0

        def visit(node, parent):
            
            if self.cycle == True:
                return
            
            seen.add(node)
            self.num_visited += 1
            for nbr in self.adj_list[node]:
                if nbr == parent:
                    continue
                if nbr in seen:
                    self.cycle = True
                    return
                visit(nbr, node)
        
        visit(0, None)
        return self.num_visited
                
