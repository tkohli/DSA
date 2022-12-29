class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        heap = []
        ans = []
        tasks.sort()
        curTime = tasks[0][0]
        for i in range(len(tasks)):
            while heap and curTime < tasks[i][0]:
                timeTaken, heapIndex = heapq.heappop(heap)
                ans.append(heapIndex)
                curTime += timeTaken
            if not heap and curTime < tasks[i][0]:
                curTime = tasks[i][0]
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
        while heap:
            timeTaken, heapIndex = heapq.heappop(heap)
            ans.append(heapIndex)
        print(heap)
        return ans
