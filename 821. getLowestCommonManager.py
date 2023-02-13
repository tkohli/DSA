"""
    This recursion function returns two values in Tuple: (given below) 
    return (    Manager if exists, # OrgChart or None
         Reports count that are found in the subree having this 
         node as a root # 0 or 1 or 2   )
    Make reportCount = 0
    First, if `node` itself is `reportOne` or `reportTwo`, we increment `reportsCount` to be 1
    Second, iterate each directionReport and pass them in the next DFS calls. 
    If manager is already found, simple return it as we want to find the lowest common manager. 
    add the `count` from the subcalls to `reportsCount` 
    if `reportsCount` becomes 2, that means the current node is the lowest common manager. So return it
    Lastly, we know that there's no manager found. (either from its subtree or node itself) . So simple return `(None, reportsCount)`

"""

def getLowestCommonManager(topManager, reportOne, reportTwo):
    
    def dfs(node):
        reportCount = 0

        if node is reportOne or node is reportTwo:
            reportCount += 1

        for neigh in node.directReports:
            managerIfExists, count = dfs(neigh)
            if managerIfExists:
                return (managerIfExists,2)
            reportCount+=count
            if reportCount==2:
                return (node,2)



        return (None,reportCount)

    manager,count = dfs(topManager)
    return manager

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
