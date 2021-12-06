def taskAssignment(k, tasks):
    pairedTasks = []
    sortedTask = sorted(tasks) # need index as well
    taskDurationToIndices = getTaskDurationToIndices(tasks)
    for idx in range(k):
        task1Duration = sortedTask[idx]
        taskDuration = taskDurationToIndices[task1Duration]
        task1Index = taskDuration.pop()
        task2Duration = sortedTask[len(tasks)-1-idx]
        task2Duration = taskDurationToIndices[task2Duration]
        task2Index = task2Duration.pop()

        pairedTasks.append([task1Index,task2Index])
    return pairedTasks

def getTaskDurationToIndices(tasks):
    taskDurationToIndices = {}
    for idx,task in enumerate(tasks):
        if task not in taskDurationToIndices:
            taskDurationToIndices[task] = []
        taskDurationToIndices[task].append(idx)
    return taskDurationToIndices

taskAssignment(3,[1, 3, 5, 3, 1, 4])