class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.adj_list = {}

        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in self.adj_list:
                self.adj_list[u] = [v]
            else:
                self.adj_list[u].append(v)
            if v not in self.adj_list:
                self.adj_list[v] = [u]
            else:
                self.adj_list[v].append(u)
        
        self.seen_nodes = set()
        dfs_count = 0
        for node in self.adj_list.keys():
            if node not in self.seen_nodes:
                dfs_count += 1
                self.seen_nodes.add(node)
                # do DFS
                self.DFS(node)
        return dfs_count + n - len(self.seen_nodes)
        
    def DFS(self, node):
        for n in self.adj_list[node]:
            if n not in self.seen_nodes:
                self.seen_nodes.add(n)
                self.DFS(n)
        
        