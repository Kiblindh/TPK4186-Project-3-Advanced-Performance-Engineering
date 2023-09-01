class Task:
    def __init__(self, key, description, duration, predecessorTasks=None, successorTasks=None):
        self.earlyStartDate = None
        self.lateStartDate = 0
        self.earlyCompletionDate = None
        self.lateCompletionDate = None
        self.key = key
        self.description = description
        self.duration = duration
        self.predecessorTasks = predecessorTasks if predecessorTasks else []
        self.successorTasks = successorTasks if successorTasks else []
        self.lastTask = False
        self.firstTask = False
        self.criticalTask = self.setCriticalTasks()
        self.durationValue = None

    def getKey(self):
        return self.key
    
    def setKey(self, key):
        self.key = key
    
    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration
    
    def setDurationValues(self, duration):
        self.duration = "(" + str(duration) + "," + str(duration) + "," + str(duration) +")"

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description
        
    def getEarlyCompletionDate(self):
        return self.earlyCompletionDate
    
    def setLastTask(self):
        self.lastTask = True
        
    def getLastTask(self):
        return self.lastTask
    
    #Duration 
    def getDurationValues(self): #Outputs [MinimumValue, ExpectedValue, MaximumValue]
        if self.duration is None:
            return [0,0,0]
        durations = self.duration.strip('()').split(',')
        durations = [float(d) for d in durations]
        return durations
    
    def createDurationValue(self, duration):
        if duration == 'Minimum':
            value = 0
            self.durationValue = value
        elif duration == 'Expected':
            value = 1
            self.durationValue = value
        elif duration == 'Maximum':
            value = 2
            self.durationValue = value
        else:
            print("Error: Duration value not recognised. It must be 'Minimum', 'Expected' or 'Maximum'!!!")
            return None
        
    #Critical Tasks
    def setCriticalTasks(self):
        if self.earlyStartDate == self.lateStartDate:
            self.criticalTask = True
        else:
            self.criticalTask = False
            
    #Predecessor Tasks
    def getPredecessorTasks(self):
        return self.predecessorTasks

    def setPredecessorTasks(self, predecessorTasks):
        self.predecessorTasks = predecessorTasks
        
    def addPredecessorTask(self, predecessorTask):
        self.predecessorTasks.append(predecessorTask)
   
    #Successor Tasks
    def getSuccessorTasks(self):
        return self.successorTasks

    def setSuccessorTasks(self, successorTasks):
        self.successorTasks = successorTasks

    def addSuccessorTask(self, successorTask):
        self.successorTasks.append(successorTask)

    def addSuccessors(self, taskList):
            for predecessorTask in self.getPredecessorTasks():
                if predecessorTask != 'Start' and predecessorTask != 'End':
                    predecessorTask = predecessorTask.replace(" ", "")
                    for task in taskList:
                        if task.getKey() == predecessorTask:
                            task.addSuccessorTask(self.getKey())
                            break
                    else:
                        print(f"Error: Predecessor task {predecessorTask} not found for task {self.getKey()}")
                  
    #Early Start And Completion Dates 
    def getEarlyCompletionDate(self):
        return self.earlyCompletionDate
    
    def getEarlyStartDate(self):
        return self.earlyStartDate

    def calculateEarlyStartDate(self, taskList):
        if self.firstTask:
            self.earlyStartDate = 0
        else:
            earlyStartDate = 0
            for predecessor in self.predecessorTasks:
                predecessor = predecessor.replace(" ", "")
                if predecessor != 'Start':
                    for task in taskList:
                        if task.getKey() == predecessor and task.earlyStartDate is not None:
                            earlyStart = task.earlyStartDate + task.getDurationValues()[self.durationValue]
                            if earlyStart > earlyStartDate:
                                earlyStartDate = earlyStart
                            break
                    else:
                        print(f"Error: Predecessor task {predecessor} not found for task {self.getKey()}")
            self.earlyStartDate = earlyStartDate

    def calculateEarlyCompletionDate(self):
        if self.earlyStartDate is not None:
            self.earlyCompletionDate = self.earlyStartDate + self.getDurationValues()[self.durationValue]
        else:
            print(f"Error: Cannot calculate Early Completion Date without a Early Start Date for task {self.getKey()}")

    # Late Start and Completion Dates     
    def getLateCompletionDate(self):
        return self.lateCompletionDate
    
    def getLateStartDate(self):
        return self.lateStartDate
    
    def calculateLateCompletionDate(self, taskList):
        if self.lastTask:
            self.lateCompletionDate = self.earlyCompletionDate
        else:
            lateCompletionDate = float('-inf')
            for successor in self.getSuccessorTasks():
                for task in taskList:
                    if task.getKey() == successor:
                        if task.lateStartDate is not None:
                            lateCompletion = task.lateStartDate
                            if lateCompletion > lateCompletionDate:
                                    self.lateCompletionDate = lateCompletion
                        else:
                            print(f"Error: Cannot calculate Late Completion Date without a Late Start Date for task {task.getKey()}")

    def calculateLateStartDate(self):
        if self.lateCompletionDate is not None:
            self.lateStartDate = self.lateCompletionDate - self.getDurationValues()[self.durationValue]
        #else:
            #print(f"Error: Cannot calculate Late Start Date without a Late Completion Date for task {self.getKey()}")
            #Kommentert ut siden vi får en bug med at late dates er negative når vi regner ut prosjektets late dates
    




#This code is for trying to fix the Villa.xlsx error for J.1, J.2 and J.3            
'''            
    def calculateLateCompletionDate(self, taskList):
        if self.lastTask:
            self.lateCompletionDate = self.earlyCompletionDate
        else:
            lateCompletionDate = float('inf')
            for successor in self.getSuccessorTasks():
                found = False
                for task in taskList:
                    if task.getKey() == successor:
                        found = True
                        if task.lateStartDate is None:
                            task.calculateLateStartDate()
                        lateCompletion = task.lateStartDate
                        if lateCompletion < lateCompletionDate:
                            lateCompletionDate = lateCompletion
                        break
                if not found:
                    print(f"Error: Successor task {successor} not found for task {self.getKey()}")
            self.lateCompletionDate = lateCompletionDate
            
            
    def calculateEarlyStartDate(self, taskList):
        if self.firstTask:
            self.earlyStartDate = 0
        else:
            maxEarlyStartDate = 0
            for predecessor in self.predecessorTasks:
                predecessor = predecessor.replace(" ", "")
                if predecessor != 'Start':
                    found = False
                    for task in taskList:
                        if task.getKey() == predecessor:
                            if task.earlyStartDate is None:
                                task.calculateEarlyStartDate(taskList)
                            earlyStart = task.earlyStartDate + task.getDurationValues()[self.durationValue]
                            if earlyStart > maxEarlyStartDate:
                                maxEarlyStartDate = earlyStart
                            found = True
                            break
                    if not found:
                        print(f"Error: Predecessor task {predecessor} not found for task {self.getKey()}")
            self.earlyStartDate = maxEarlyStartDate
        return self.earlyStartDate
'''