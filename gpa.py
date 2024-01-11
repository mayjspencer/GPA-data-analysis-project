import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Define grade weights
grade_weights = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
ap_weights = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 1.0, 'F': 0.0}

def getAllStudents():
    dfAll = df[['Name','Schoolname', 'City', 'State']]
    print(dfAll)

def getAllState(stateName):
    dfState = df[['Name','Schoolname', 'City', 'State']]
    print(dfState[dfState['State'] == stateName])

def getAllSchool(schoolName):
    dfSchool = df[['Name','Schoolname', 'City', 'State']]
    print(dfSchool[dfSchool['Schoolname'] == schoolName])

def main():
    while True:
        print("\nChoose an option:\n")
        print("A - View All Students\n")
        print("B - View State\n")
        print("C - View School\n")
        print("D - Exit\n")

        choice = input("Enter your choice (A / B / C / D): ")

        if choice == "A":
            getAllStudents()
        elif choice == "B":
            state = input("What StaDte would you like to view: \n")
            getAllState(state)
        elif choice == "C":
            school = input("What School would you like to view: \n")
            getAllSchool(school)
        elif choice == "D":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
