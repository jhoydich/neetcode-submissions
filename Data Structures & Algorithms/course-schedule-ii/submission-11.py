from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.adj_list = [[] for i in range(numCourses)]
        self.in_count = {}
        for i in range(numCourses):
            self.in_count[i] = 0
        self.n = numCourses
        
        for req in prerequisites:
            self.adj_list[req[1]].append(req[0])
            self.in_count[req[0]] +=  1
        print(self.adj_list)

        res = self.dfs()
        if res == True:
            
            return []
        
        return self.bfs()
        
        
    def bfs(self):
        Q = deque()
        courses = []
        for k, v in self.in_count.items():
            if v == 0:
                Q.append(k)
                courses.append(k)
        while Q:
            node = Q.popleft()
            for nbr in self.adj_list[node]:
                courses.append(nbr)
                Q.append(nbr)
        print(courses)
        return courses
    
    def dfs(self):
        visited = set()
        seen = set()
        def visit(node):
            if node in seen:
                return True
            if node in visited:
                return False
            visited.add(node)
            seen.add(node)

            for nbr in self.adj_list[node]:
                res = visit(nbr)
                if res == True:
                    return True
            seen.remove(node)
            return False
        for i in range(self.n):
            if i not in visited:
                res = visit(i)
                if res == True:
                    return True
        return False