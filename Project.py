# Imported modules
# ---------------------
from Task import *

class Project:
    def __init__(self, tasks):
        self.tasks = tasks
        self.earlyStartDate = 0
        self.lateStartDate = 0
        self.earlyCompletionDate = 0
        self.lateCompletionDate = 0
        self.Duration = 0
        self.taskList = []
        self.status = "unchecked"

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

    def getTasks(self):
        return self.tasks
        
    def setTasks(self, tasks):
        self.tasks = tasks
        
    def getTaskList(self):
        return self.taskList

    def createListFromDict(self):
        for task in self.tasks.values():
            self.taskList.append(task)
        return self.taskList
        
    def setDuration(self, value):
        for task in self.getTaskList():
            task.createDurationValue(value)
    
    def addAllSuccessors(self):
        for task in self.getTaskList():
            task.addSuccessors(self.getTaskList())
            
    def calculateEarlyDates(self):
        for task in self.getTaskList():
            task.calculateEarlyStartDate(self.getTaskList())
            task.calculateEarlyCompletionDate()
    
    def calculateLateDates(self):
        for task in reversed(self.getTaskList()):
            task.calculateLateCompletionDate(self.getTaskList())
            task.calculateLateStartDate()
    
    def calculateCriticalTasks(self):
        for task in self.getTaskList():
            task.setCriticalTasks()
    
    def getTaskDurations(self):
        durations = []
        for task in self.getTaskList():
            durations.append(task.getDuration())
        return durations
    
    def calculateAll(self, value):
        self.setDuration(value)
        self.calculateEarlyDates() 
        self.calculateLateDates()
        self.calculateCriticalTasks()
        self.calculateProjectDuration()
        
    def calculateProjectDuration(self):
        taskList = self.getTaskList()
        #return taskList[-1].getLateCompletionDate()
        return taskList[-1].getEarlyCompletionDate()
    
    def insertGate(self, specifiedTask):
        position = 0
        i = 0
        for task in self.taskList:
            if task.getKey() == specifiedTask:
                position = i+1
            i += 1

        gate = Task("IG", "This is the intermediate gate inserted", 0, self.taskList[0:position], self.taskList[position:])
        self.taskList.insert(position, gate)
    
    def getEarlyBeforeCompletionArray(self):
        gate = 0
        for task in self.getTaskList():
            if(task.getKey() == "IG"):
                gate = task
                
        earlyCompletionDatesBeforeGate = []
        predecessorTasks = gate.getPredecessorTasks()
        for task in predecessorTasks:
            earlyCompletionDateTask = task.getEarlyCompletionDate()
            earlyCompletionDatesBeforeGate.append(earlyCompletionDateTask)
        return earlyCompletionDatesBeforeGate