def topologicalSort(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job, dep)
    orderedJobs = []
    nodeWithNoPreq = list((filter(
        lambda node: node.preReq == 0, graph.node
    )))
    while len(nodeWithNoPreq):
        node = nodeWithNoPreq.pop()
        orderedJobs.append(node.job)
        removeDeps(node, nodeWithNoPreq)
    edge = any(node.preReq for node in graph.node)
    return [] if edge else orderedJobs


def removeDeps(node, nodeWithNoPreq):
    while len(node.dep):
        dep = node.dep.pop()
        dep.preReq -= 1
        if dep.preReq == 0:
            nodeWithNoPreq.append(dep)


class JobGraph:
    def __init__(self, jobs):
        self.node = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.dep.append(depNode)
        depNode.preReq += 1

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.node.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job) -> None:
        self.job = job
        self.dep = []
        self.preReq = 0
