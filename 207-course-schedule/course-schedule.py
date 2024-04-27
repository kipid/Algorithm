class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = { crs: [] for crs in range(numCourses) }
        
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        completed = set()
        cycle = set()

        def dfs(crs):
            if crs in completed:
                return True
            
            if crs in cycle: 
                return False

            cycle.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            completed.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True