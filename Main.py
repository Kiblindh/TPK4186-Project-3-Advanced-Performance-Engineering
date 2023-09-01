# TPK4186 - 2023 - Assignment 4 - Group 11 - Sipan Omar, Kim-Iver Brevik Blindheimsvik & Morten Husby Sande

# 1. Imported modules
# ------------------------------------------
import sys
from Loader import *
from Printer import *
from Task import *
from Statistics import *
from Regression import Regression
from Classification import Classification

# 2. Global variables
# --------------------------------------------

loader = Loader()
printer = Printer()

# 3. Main
# --------------------------------------------

# --------------------------------------------
# Task 1 - Data structures to encode PERT diagrams
# --------------------------------------------

#The data structures are listed in the Task.py file under the Task class

# --------------------------------------------
# Task 2 - Load projects from Excel spreadsheets
# --------------------------------------------

villa = loader.ExcelLoader("files/Villa.xlsx")
warehouse = loader.ExcelLoader("files/Warehouse.xlsx")

'''printer.printProjectExcel(villa, "files/villa.txt")
printer.printProjectExcel(warehouse, "files/warehouse.txt")'''

# --------------------------------------------
# Task 3 - Calculator
# --------------------------------------------

'''villa.calculateAll('Expected')  #Type in the duration type 'Minimum', 'Expected' or 'Maximum'
warehouse.calculateAll('Expected') 

printer.printProjectSummary(villa)
printer.printProjectSummary(warehouse)

printer.printProjectDurations(villa) #Calculate the shortest, the expected and the longest duration of a project.
printer.printProjectDurations(warehouse)'''

# --------------------------------------------
# Task 4 - Statistics
# --------------------------------------------

'''villaStat = Statistics(villa)
thousandProjects = villaStat.getRandomProjects(1000, 'random') # r can be a number or 'random' which choses randomly from the list of risk factors
villaStat.calculateStatistics(thousandProjects)

print("--------")
printer.printStatistics(villaStat)
printer.printProjectClassification(villaStat)'''

# --------------------------------------------
# Task 5 - Classification methods
# --------------------------------------------

'''statisticHelper = Statistics(villa)
thousandProjects = statisticHelper.getRandomProjects(1000, 'random')
statisticHelper.insertGatesInRandomProjects("C.1", thousandProjects)
statisticHelper.calculateStatistics(thousandProjects)
kernel = "mlp"
beforeDates2 = statisticHelper.getArrayBeforeGate2(thousandProjects)

y = []
for project in thousandProjects:
    status = project.getStatus()
    y.append(status)

X_array = beforeDates2
y_array = np.array(y)

classificator = Classification("files/ClassificationResults.csv")
classificator.decisionTree(X_array, y_array, kernel)'''


# --------------------------------------------
# Task 6 - Regression methods
# --------------------------------------------

'''statisticHelper = Statistics(villa)
kernel = "lin"
thousandProjects = statisticHelper.getRandomProjects(1000, "random")
statisticHelper.insertGatesInRandomProjects("C.1", thousandProjects)
projectDurations = statisticHelper.getProjectDurations(thousandProjects)
beforeDates2 = statisticHelper.getArrayBeforeGate2(thousandProjects)

X_array = beforeDates2
y = np.array(projectDurations)

regressor = Regression()
y_pred, y_test = regressor.regressionModel(X_array, y, kernel)

regressor.printRegResult(y_test, y_pred, sys.stdout, kernel)
regressor.exportRegResults(y_test, y_pred, kernel, "files/RegressionResults.csv")
regressor.plottDiffBetweenPredAndActual(y_pred, y_test, kernel)
'''

