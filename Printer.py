class Printer:
    def __init__(self):
        pass

    def printProjectExcel(self, project, outputFile):
        outputFile = open(outputFile, "w")
        for task in project.getTasks().values():
            outputFile.write(str('Code: '))
            outputFile.write(str(task.getKey())+ '\n')
            if task.getDescription() and task.getDuration() is not None:
                outputFile.write(str(task.getDescription())+ ': ')
                outputFile.write(str(task.getDuration())+ '\n')
            outputFile.write("Predecessor tasks: ")
            for prevTask in task.getPredecessorTasks():
                outputFile.write(str(prevTask))
            for nextTask in task.getSuccessorTasks():
                outputFile.write(str(nextTask))
            outputFile.write("\n\n")
        outputFile.close()
         
    def printProjectSummary(self, project):
        taskList = project.getTaskList()
        print(f"Project Summary")
        print("================")
        for task in taskList:
            print(f"Task {task.getKey()}: {task.getDescription()}")
            print(f"Duration: {task.getDuration()} (Min: {task.getDurationValues()[0]}, Expected: {task.getDurationValues()[1]}, Max: {task.getDurationValues()[2]})")
            print(f"Predecessor Tasks: {','.join(task.getPredecessorTasks())}")
            print(f"Successor Tasks: {','.join(task.getSuccessorTasks())}")
            print(f"Early Dates: ({int(task.earlyStartDate)}, {int(task.getEarlyCompletionDate())})")
            print(f"Late Dates: ({int(task.lateStartDate)}, {int(task.lateCompletionDate)})")
            print(f"Critical Task: {'Yes' if task.criticalTask else 'No'}")
            print("================")
        print(f"Total project Duration: {int(project.calculateProjectDuration())}")
        
    def printProjectDurations(self, project):
        project.calculateAll('Minimum')
        print(f"Minimum project duration: {int(project.calculateProjectDuration())}")
        project.calculateAll('Expected')
        print(f"Expected project duration: {project.calculateProjectDuration()}")
        project.calculateAll('Maximum')
        print(f"Maximum project duration: {project.calculateProjectDuration()}")
         
    def printStatistics(self, statistics):
        print(f"Minimum project duration: {statistics.minimum_duration}")
        print(f"Maximum project duration: {statistics.maximum_duration}")
        print(f"Mean project duration: {statistics.mean_duration}")
        print(f"Standard deviation: {statistics.std_deviation}")
        print(f"10th percentile: {statistics.percentiles[0]}")
        print(f"20th percentile: {statistics.percentiles[1]}")
        print(f"30th percentile: {statistics.percentiles[2]}")
        print(f"40th percentile: {statistics.percentiles[3]}")
        print(f"50th percentile: {statistics.percentiles[4]}")
        print(f"60th percentile: {statistics.percentiles[5]}")
        print(f"70th percentile: {statistics.percentiles[6]}")
        print(f"80th percentile: {statistics.percentiles[7]}")
        print(f"90th percentile: {statistics.percentiles[8]}")
    
    def printProjectClassification(self, statistics):
        print(f"Number of successful projects: {statistics.successfullCount}")
        print(f"Number of acceptable projects: {statistics.acceptableCount}")
        print(f"Number of failed projects: {statistics.failedCount}")
        
    