import pandas as pd

df = pd.read_csv("dataset4.csv")
print("Original DataFrame:")
print(df)

#Filter employees from Pune
pune_employees = df[df['City'] == 'Pune']
print("Employees from Pune:")
print(pune_employees)

#Calculate the average salary
average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)

#Count employees by gender
gender_counts = df['Gender'].value_counts()
print("Employee Gender Counts:")
print(gender_counts)

#Sort employees by salary in descending order
sorted_df = df.sort_values('Salary', ascending=False)
print("Employees Sorted by Salary:")
print(sorted_df)

#Group employees by designation and calculate the average salary for each group
designation_salary = df.groupby('Designation')['Salary'].mean()
print("Average Salary by Designation:")
print(designation_salary)

#Add a new column 'Age' with default value 0
df['Age'] = 0
print("DataFrame with 'Age' Column:")
print(df)

#Select only the 'Name' and 'Salary' columns
selected_columns = df[['Name', 'Salary']]
print("Selected Columns:")
print(selected_columns)

#Filter employees with a salary greater than 100,000
high_salary_employees = df[df['Salary'] > 100000]
print("Employees with High Salary:")
print(high_salary_employees)

# Calculate the total salary for each city
city_salary_total = df.groupby('City')['Salary'].sum()
print("Total Salary by City:")
print(city_salary_total)

# Calculate the age based on the current year and assuming all employees are born in 1980
current_year = 2023
df['Age'] = current_year - 1980
print("DataFrame with Age Column:")
print(df)
