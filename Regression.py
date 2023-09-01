# Imported packages and modules:
# --------------------------------

import math
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics

# Class definition:
# ---------------------------------
class Regression:
    def __init__(self):
        pass

    def regressionModel(self, X, y, kernel):
        # Split into training and test sets:
        # -------------------------------------
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Fit model for regression
        # -------------------------------------
        if kernel == "rbf": # RBF (Radial Basis Function):
            svr_rbf = SVR(kernel="rbf", C=100, gamma=1e-8, epsilon=0.1)
            svr_rbf.fit(X_train, y_train) 
            y_pred = svr_rbf.predict(X_test)
            return y_pred, y_test
        
        elif kernel == "lin": # Linear:
            svr_lin = SVR(kernel="linear", C=100, gamma="auto")
            svr_lin.fit(X_train, y_train) 
            y_pred = svr_lin.predict(X_test)
            return y_pred, y_test
        
        elif kernel == "sig": # Sigmoid:
            svr_poly = SVR(kernel="sigmoid", C=100, gamma="scale")
            svr_poly.fit(X_train, y_train)
            y_pred = svr_poly.predict(X_test)
            return y_pred, y_test
        else:
            print("Wrong kernel. Must be: 'rbf', 'lin' or 'sig' ")
            return None


    def printRegResult(self, y_test, y_pred, output, kernel):
        if kernel == "rbf":
            output.write("Actual duration\tPredicted duration for Radial Basis Function\n")
        if kernel == "lin":
            output.write("Actual duration\tPredicted duration for Linear Regression\n")
        if kernel == "sig":
            output.write("Actual duration\tPredicted duration for Sigmoid Regression\n")
        
        for i in range(0, len(y_test)):
            output.write("{0:g}\t{1:g}\n".format(round(y_test[i], 0), round(y_pred[i], 0)))
        
        output.write("MAE\t{0:g}\n".format(metrics.mean_absolute_error(y_test, y_pred)))
        output.write("RMSE\t{0:g}\n".format(math.sqrt(metrics.mean_squared_error(y_test, y_pred))))
        output.write("R^2\t{0:g}\n".format(metrics.r2_score(y_test, y_pred)))
    
    def exportRegResults(self, actualRewards, predictedRewards, kernel, fileName):
        output = open(fileName, "w")
        self.printRegResult(actualRewards, predictedRewards, output, kernel)
        output.close()

    def plottDiffBetweenPredAndActual(self, y_pred, y_test, kernel):
        listOfDiffs = []
        x_axis = []
        for i in range(len(y_test)):
            diff = y_test[i]-y_pred[i]
            listOfDiffs.append(diff)
            x_axis.append(i)
        
        if kernel == "rbf":
            plt.title(label="Difference between y_test values and y_pred values for rbf method", fontweight="bold")
        elif kernel == "lin":
            plt.title(label="Difference between y_test values and y_pred values for linear method", fontweight="bold")
        elif kernel == "sig":
            plt.title(label="Difference between y_test values and y_pred values for sigmoid method", fontweight="bold")
        else:
            print("Wrong kernel input")
            return None
        
        plt.plot(x_axis, listOfDiffs, color="RED")
        plt.xlabel("Indexes for the predicated and test values")
        plt.ylabel("Value of difference. +: y_test > y_pred")
        plt.grid()
        plt.show()
        