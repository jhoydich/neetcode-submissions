class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.adjacencyList = {}
        self.checked_nodes = set()
        
        self.searching = set()

        for req in prerequisites:
            
            c = req[0]
            pre = req[1]
            if pre not in self.adjacencyList:
                self.adjacencyList[pre] =[c]
            else:
                self.adjacencyList[pre].append(c)

  
     
        for cl in self.adjacencyList.keys():
            
            if cl in self.checked_nodes:
                continue
            
            res = self.DFS(cl)
            if res:
                return False

        return True
    
    def DFS(self, cl):
            
            if cl in self.searching:
                return True
            
            self.checked_nodes.add(cl)
            
            if cl not in self.adjacencyList:
                return False
            cls = self.adjacencyList[cl]
            self.searching.add(cl)
            for c in cls:
                
                  
                res = self.DFS(c)
                if res:
                    return True
            self.searching.remove(cl)
            return False
        