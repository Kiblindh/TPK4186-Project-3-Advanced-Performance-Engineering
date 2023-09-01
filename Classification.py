import math
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics


class Classification:
    def __init__(self, fileName):
        self.fileName = fileName

    def decisionTree(self, X, y, type):

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        if type == "dtc":
            # Create the decision tree classifier object
            dtc = DecisionTreeClassifier(max_iter = 500, random_state=0)
            # Train the classifier using the training data
            dtc.fit(X_train, y_train)
            # Make predictions on the test data
            y_pred = dtc.predict(X_test)
            # Evaluate the accuracy of the classifier
            accuracy = accuracy_score(y_test, y_pred)
            y_test = self.convertLabels(y_test)
            y_pred = self.convertLabels(y_pred)
            self.printConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, sys.stdout)
            self.exportConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, self.fileName)
            print("Accuracy: ", accuracy)
        
        elif type == "rfc":
            rfc = RandomForestClassifier(max_iter = 500, random_state=0)
            rfc.fit(X_train, y_train)
            y_pred = rfc.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            y_test = self.convertLabels(y_test)
            y_pred = self.convertLabels(y_pred)
            self.printConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, sys.stdout)
            self.exportConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, self.fileName)
            print("Accuracy: ", accuracy)
        
        elif type == "mlp":
            mlp = MLPClassifier(max_iter = 500, random_state=0)
            mlp.fit(X_train, y_train)
            y_pred = mlp.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            y_test = self.convertLabels(y_test)
            y_pred = self.convertLabels(y_pred)
            self.printConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, sys.stdout)
            self.exportConfusionMatrix(["Successful", "Acceptable", "Failed"], y_test, y_pred, self.fileName)
            print("Accuracy: ", accuracy)
        
        else:
            print("Classification type is invalid. Must be: 'dtc', 'rfc' or 'mlp' ")
            return None
    
    def convertLabels(self, labels):
        for i in range(len(labels)):
            if labels[i]=="Successful":
                labels[i] = 0
            elif labels[i]=="Acceptable":
                labels[i] = 1
            elif labels[i]=="Failed":
                labels[i] = 2
            else:
                print("Invalid label")
                return None
        return labels

    def printConfusionMatrix(self, labels, actualLabels, predictedLabels, output):
        numberOfLabels = len(labels)
        counts = [[0 for _ in range(0, numberOfLabels)] for _ in range(0, numberOfLabels)]
        for i in range(0, len(actualLabels)):
            counts[int(actualLabels[i])][int(predictedLabels[i])] += 1
        for column in range(0, numberOfLabels):
            output.write("\t\t\t{0:s}".format(labels[column]))
        output.write("\n")
        for row in range(0, numberOfLabels):
            output.write("{0:s}".format(labels[row]))
            for column in range(0, numberOfLabels):
                output.write("\t\t\t{0:d}".format(counts[row][column]))
            output.write("\n")

    def exportConfusionMatrix(self, labels, actualLabels, predictedLabels, fileName):
        output = open(fileName, "w")
        self.printConfusionMatrix(labels, actualLabels, predictedLabels, output)
        output.close()