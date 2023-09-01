# Imported modules
# ---------------------
import random
import numpy as np
from Task import *
from Project import *

class Statistics:
    def __init__(self, project):
        self.project = project

    def randomDurationsOfProjectTasks(self, r):
        projectTasks = self.project.getTaskList()
        newTasks = []
        for task in projectTasks:
            sampleDuration = 0
            a = task.getDurationValues()[0]
            e = task.getDurationValues()[1] * r
            b = task.getDurationValues()[2]
            if(e < a):
                a = e
                sampleDuration = random.triangular(a, b, a)
            elif(e > b):
                b = e
                sampleDuration = random.triangular(a, b, b)
            else:
                sampleDuration = random.triangular(a, b, e)
            newTask = Task(task.getKey(), task.getDescription(), sampleDuration, task.getPredecessorTasks(), task.getSuccessorTasks())
            newTask.setDurationValues(sampleDuration)
            newTasks.append(newTask)
        newProject = Project(newTasks)
        newProject.taskList = newTasks
        newProject.calculateAll("Expected")
        return newProject

    def getRandomProjects(self, num_samples, r = 1):
        randomProjects = []
        random_r = False
        riskFactors = [0.8, 1.0, 1.2, 1.4]
        if r == 'random':
            random_r = True
        for _ in range(num_samples):
            if random_r == True:
                r = random.choice(riskFactors)
            randomProject = self.randomDurationsOfProjectTasks(r)
            randomProjects.append(randomProject)
        return randomProjects
    
    def getProjectDurations(self, randomProjects):
        randomProjectDurationList = []
        for project in randomProjects:
            projectDuration = project.calculateProjectDuration()
            randomProjectDurationList.append(projectDuration)
        return randomProjectDurationList
    
    def calculateStatistics(self, randomProjects, value='Expected'):
        self.successfullCount = 0
        self.acceptableCount = 0
        self.failedCount = 0
        self.project.calculateAll(value)
        expectedProjectDuration = self.project.calculateProjectDuration()
        for project in randomProjects:
            projectDuration = project.calculateProjectDuration()
            percentage = 100 * float(projectDuration)/float(expectedProjectDuration)
            if(percentage < 105):
                self.successfullCount += 1
                project.setStatus("Successful")
            elif(105 <= percentage < 115):
                self.acceptableCount += 1
                project.setStatus("Acceptable")
            else:
                self.failedCount += 1
                project.setStatus("Failed")
        projectDurations = self.getProjectDurations(randomProjects)
        self.minimum_duration = min(projectDurations)
        self.maximum_duration = max(projectDurations)
        self.mean_duration = np.mean(projectDurations)
        self.std_deviation = np.std(projectDurations)
        self.percentiles = np.percentile(np.array(projectDurations), np.arange(0, 100, 10))
        
    def insertGatesInRandomProjects(self, specifiedTask, randomProjects):
        lengthTasksOfProject = len(randomProjects[0].getTaskList())
        for project in randomProjects:
            project.insertGate(specifiedTask)
        lengthTasksOfProject2 = len(randomProjects[0].getTaskList())
        if(lengthTasksOfProject2 - lengthTasksOfProject == 1):
            print("The gates were added")
        else:
            print("The function was unsuccessfull")
    
    def getArrayBeforeGate2(self, randomProject):
        beforeDates = []
        for project in randomProject:
            beforeGate = project.getEarlyBeforeCompletionArray()
            beforeDates.append(beforeGate)
        #return beforeDates
        return np.array(beforeDates)