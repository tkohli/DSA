def taskAssignment(k, tasks):
    pairedTasks = []
    sortedTask = sorted(tasks) # need index as well
    taskDurationToIndices = getTaskDurationToIndices(tasks)
    print(taskDurationToIndices)


def getTaskDurationToIndices(tasks):
    taskDurationToIndices = {}
    for idx,task in enumerate(tasks):
        if task not in taskDurationToIndices:
            taskDurationToIndices[task] = []
        taskDurationToIndices[task].append(idx)
    return taskDurationToIndices

taskAssignment(3,[1, 3, 5, 3, 1, 4])