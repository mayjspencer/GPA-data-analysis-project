import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Define grade weights
grade_weights = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
ap_weights = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 1.0, 'F': 0.0}




#returns gpa of student at given row
def calculate_unweighted_gpa(row):
    grades = [grade_weights.get(row['Grade1'], 0), grade_weights.get(row['Grade2'], 0),
              grade_weights.get(row['Grade3'], 0), grade_weights.get(row['Grade4'], 0),
              grade_weights.get(row['Grade5'], 0)]
    return np.mean(grades)

#returns weighted gpa of student at given row
def calculate_weighted_gpa(row):
    grades = [ap_weights.get(row['Grade1'], 0), ap_weights.get(row['Grade2'], 0),
              ap_weights.get(row['Grade3'], 0), ap_weights.get(row['Grade4'], 0),
              ap_weights.get(row['Grade5'], 0)]
    return np.mean(grades)





# Prints all students with given Unweighted GPA or higher, sorted by GPA
def getStudentsByUnweightedGPA(min_gpa):
    df['UnweightedGPA'] = df.apply(calculate_unweighted_gpa, axis=1)
    filtered_students = df[df['UnweightedGPA'] >= min_gpa].sort_values(by='UnweightedGPA', ascending=False)
    print(filtered_students[['Name', 'State', 'UnweightedGPA']])

# Prints all students with given Weighted GPA or higher, sorted by GPA
def getStudentsByWeightedGPA(min_gpa):
    df['WeightedGPA'] = df.apply(calculate_weighted_gpa, axis=1)
    filtered_students = df[df['WeightedGPA'] >= min_gpa].sort_values(by='WeightedGPA', ascending=False)
    print(filtered_students[['Name', 'State', 'WeightedGPA']])





def getAllStudents():
    dfAll = df[['Name','Schoolname', 'City', 'State']]
    print(dfAll)






def getAllState(stateName):
    # Calculate unweighted GPA before filtering
    df['UnweightedGPA'] = df.apply(calculate_unweighted_gpa, axis=1)

    # Check if 'State' column exists in the DataFrame
    if 'State' in df.columns:
        dfState = df[['Name', 'Schoolname', 'City', 'State', 'UnweightedGPA']]
        filtered_df = dfState[dfState['State'] == stateName]
        print(filtered_df)
    else:
        print("Error: 'State' column not found in the DataFrame.")





def getAllSchool(schoolName):
    dfSchool = df[['Name','Schoolname', 'City', 'State']]
    print(dfSchool[dfSchool['Schoolname'] == schoolName])



def getAllData():
    print(df)



def plotUnweightedGPADistribution():
    df['UnweightedGPA'] = df.apply(calculate_unweighted_gpa, axis=1)
    plt.figure(figsize=(10, 6))
    plt.hist(df['UnweightedGPA'], bins=20, color='Red', edgecolor='black')
    plt.xlabel('Unweighted GPA')
    plt.ylabel('Frequency')
    plt.title('Distribution of Unweighted GPAs')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()




def main():
    while True:
        print("\nChoose an option:\n")
        print("A - View All Students\n")
        print("B - View State\n")
        print("C - View School\n")
        print("D - View All Data\n")
        print("E - Plot all GPAs\n")
        print("F - Filter Unweighted GPA\n")
        print("G - Filter Weighted GPA\n")
        print("EXIT - Exit\n")

        choice = input("Enter your choice (A / B / C...): ")

        if choice == "A":
            getAllStudents()
        elif choice == "B":
            state = input("What State would you like to view: \n")
            getAllState(state)
        elif choice == "C":
            school = input("What School would you like to view: \n")
            getAllSchool(school)
        elif choice == "D":
            getAllData()
        elif choice == "E":
            plotUnweightedGPADistribution()
        elif choice == "EXIT":
            print("Exiting the program. Goodbye!")
            break
        elif choice == "F":
            gpa = float(input("View Unweighted GPA at or above: \n"))  # Convert to float
            getStudentsByUnweightedGPA(gpa)
        elif choice == "G":
            gpa = float(input("View Weighted GPA at or above: \n"))  # Convert to float
            getStudentsByWeightedGPA(gpa)
        else:
            print("Invalid choice. Please try again.")


main()
