import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


 
print("\n----- IMPORT DATASET -----")
df = pd.read_csv("employee_salary_dataset.csv")



print("\n----- BASIC DATA -----")
print("Total Number of Employees")
print(df["EmployeeID"].count())

print("\nTotal Columns & Column Names")
print(len(df.columns))
print(df.columns)

print("\nData Type")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())



print("\n----- GENERAL ANALYSIS -----")
print("Average Monthly Salary")
print(df["Monthly_Salary"].mean())

print("\nAverage Employee Age")
print(df["Age"].mean())

print("\nAverage Years of Experience")
print(df["Experience_Years"].mean())



print("\n----- SALARY ANALYSIS -----")
print("Overall Salary Distribution")
print(df["Monthly_Salary"].describe())

print("\nSalary Breakdown By Department")
salary_by_department = df.groupby('Department')['Monthly_Salary'].agg(['mean', 'max', 'min'])
print(salary_by_department)

print("\nHistogram Of Monthly Salary")
plt.hist(df['Monthly_Salary'])
plt.title("Monthly Salary Distribution")
plt.xlabel("Monthly Salary")
plt.ylabel("Number of Employees")
plt.show()

print("\nBox Plot of Salary")
plt.boxplot(df["Monthly_Salary"])
plt.title("Salary Boxplot")
plt.show()



print("\n----- EXPERIENCE ANALYSIS -----")
print("\nEmployee Count by Experience Years")
print(df["Experience_Years"].value_counts())

print("Average Salary by Experience Years")
print(df.groupby("Experience_Years")["Monthly_Salary"].mean())

print("\nHighest Paying Experience Years")
print(df.groupby("Experience_Years")["Monthly_Salary"].mean().sort_values(ascending=False))

print("\nHistogram Of Experience Distribution")
plt.hist(df["Experience_Years"])
plt.title("Experience Distribution")
plt.xlabel("Years of Experience")
plt.ylabel("Number of Employees")
plt.show()



print("\n----- EDUCATION ANALYSIS -----")
print("Employee Count by Education")
print(df["Education_Level"].value_counts())

print("\nAverage Salary by Education")
print(df.groupby("Education_Level")["Monthly_Salary"].mean())

print("\nHighest Paying Education Level")
print(df.groupby("Education_Level")["Monthly_Salary"].mean().sort_values(ascending=False))

print("\nBar Graph Of Education Level")
education = df.groupby("Education_Level")["Monthly_Salary"].mean()
plt.bar(education.index, education.values)
plt.title("Average Salary by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Average Salary")
plt.show()



print("\n----- DEPARTMENT ANALYSIS -----")
print("Total Payroll Cost")
print(df.groupby("Department")["Monthly_Salary"].sum())

print("\nEmployee Count")
print(df["Department"].value_counts())

print("\nAverage Salary by Department")
print(df.groupby("Department")["Monthly_Salary"].mean())

print("\nHighest Paying Department")
print(df.groupby("Department")["Monthly_Salary"].mean().idxmax())

print("\nBar Graph Of Department")
df.groupby("Department")["Monthly_Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()



print("\n----- GENDER ANALYSIS -----")
print("Gender Representation")
print(df["Gender"].value_counts())

print("\nAverage Salary by Gender")
print(df.groupby("Gender")["Monthly_Salary"].mean())

print("\nBar Graph Of Gender ")
df.groupby("Gender")["Monthly_Salary"].mean().plot(kind="bar")
plt.title("Average Salary by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Salary")
plt.show()



print("\n----- CITY ANALYSIS -----")
print("Employee Distribution by City ")
print(df["City"].value_counts())

print("\nAverage Salary by City ")
print(df.groupby("City")["Monthly_Salary"].mean())

print("\nHighest Paying City ")
print(df.groupby("City")["Monthly_Salary"].mean().idxmax())

print("\nBar Graph Of City ")
df.groupby("City")["Monthly_Salary"].mean().plot(kind="bar")
plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.show()



print("\n----- AGE ANALYSIS -----")
print("Average Age ")
print(df["Age"].mean())

print("\nYoungest Employee Age ")
print(df["Age"].min())

print("\nOldest Employee Age ")
print(df["Age"].max())

print("\nAverage Salary by Age ")
print(df.groupby("Age")["Monthly_Salary"].mean())

print("\nScatter Plot Of Age vs Salary ")
age_salary = df.groupby("Age")["Monthly_Salary"].mean()
plt.bar(age_salary.index, age_salary.values)
plt.title("Average Salary by Age")
plt.xlabel("Age")
plt.ylabel("Average Salary")
plt.show()



print("\n----- CORRELATION HEATMAP -----")
sns.heatmap(df[['Age', 'Experience_Years', 'Monthly_Salary']].corr(),annot=True)
plt.title("Correlation Heatmap")
plt.show()



print("\n----- EMPLOYEE SUMMARY TABLES -----")
print("\nDepartment vs Average Salary ")
print(df.groupby("Department")["Monthly_Salary"].mean())

print("\nExperience vs Average Salary ")
print(df.groupby("Experience_Years")["Monthly_Salary"].mean())

print("\nEducation vs Average Salary ")
print(df.groupby("Education_Level")["Monthly_Salary"].mean())

print("\nGender vs Average Salary ")
print(df.groupby("Gender")["Monthly_Salary"].mean())

print("\nCity vs Average Salary ")
print(df.groupby("City")["Monthly_Salary"].mean())

print("\nAge vs Average Salary ")
print(df.groupby("Age")["Monthly_Salary"].mean())