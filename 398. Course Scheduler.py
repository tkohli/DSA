class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # track all courses for visited
        toVisited = set()

        def dfs(course):
            if course in toVisited:
                return False
            if preMap[course] == []:
                return True

            toVisited.add(course)
            for child in preMap[course]:
                if not dfs(child):
                    return False
            toVisited.remove(course)
            preMap[course] = []  # so that all pre courses are matched
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
