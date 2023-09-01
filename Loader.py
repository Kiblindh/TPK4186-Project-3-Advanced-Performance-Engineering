# Imported modules
# ---------------------
import openpyxl
from Task import *
from Project import *

class Loader:
    def __init__(self):
        pass

    def ExcelLoader(self, fileName):
        book = openpyxl.load_workbook(fileName)
        sheet = book.active
        tasks = {}
        for row in sheet:
            if row[0].value == "Task":
                key = row[1].value
                description = row[2].value
                duration = row[3].value
                predecessorTasks = row[4].value
                predecessorTasks = predecessorTasks.split(",")
                task = Task(key, description, duration, predecessorTasks)
                tasks[key] = task
            if (row[0].value == "Gate") and (row[1].value == "End" or row[1].value == "Completion"):
                key = row[1].value
                description = None
                duration = None
                predecessorTasks = row[4].value
                predecessorTasks = predecessorTasks.split(",")
                task = Task(key, description, duration, predecessorTasks)
                task.setLastTask()
                tasks[key] = task
        project = Project(tasks)
        project.createListFromDict()
        project.addAllSuccessors()
        return project

