class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False  # cycle found
            if visited[course] == 2:
                return True   # already checked
            
            visited[course] = 1
            
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True