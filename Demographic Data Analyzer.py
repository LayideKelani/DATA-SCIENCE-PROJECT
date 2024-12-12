import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\Lawal Modesola\Documents\DATA ANALYSIS PROJECT\dataset\adult.data.csv")

# 1. How many people of each race are represented in this dataset?
race_count = df['Race'].value_counts()

# 2. What is the average age of men?
average_age_men = df[df['Gender'] == 'Male']['Age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
bachelors_count = df[df['Education'] == 'Bachelors'].shape[0]
total_count = df.shape[0]
bachelors_percentage = (bachelors_count / total_count * 100) if total_count > 0 else 0

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
advanced_education_high_salary_count = advanced_education[advanced_education['Salary'] == '>50K'].shape[0]
advanced_education_count = advanced_education.shape[0]
advanced_education_high_salary_percentage = (advanced_education_high_salary_count / advanced_education_count * 100) if advanced_education_count > 0 else 0

# 5. What percentage of people without advanced education make more than 50K?
no_advanced_education = df[~df['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
no_advanced_education_high_salary_count = no_advanced_education[no_advanced_education['Salary'] == '>50K'].shape[0]
no_advanced_education_count = no_advanced_education.shape[0]
no_advanced_education_high_salary_percentage = (no_advanced_education_high_salary_count / no_advanced_education_count * 100) if no_advanced_education_count > 0 else 0

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = df['Hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_salary_high = df[df['Hours-per-week'] == min_hours_per_week]
min_hours_high_salary_count = min_hours_salary_high[min_hours_salary_high['Salary'] == '>50K'].shape[0]
min_hours_count = min_hours_salary_high.shape[0]
min_hours_high_salary_percentage = (min_hours_high_salary_count / min_hours_count * 100) if min_hours_count > 0 else 0

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_salary_percentage = df.groupby('Native-Country').apply(
    lambda x: (x[x['Salary'] == '>50K'].shape[0] / x.shape[0]) * 100 if x.shape[0] > 0 else 0
)
country_highest_salary_percentage = country_salary_percentage.idxmax()
highest_percentage = country_salary_percentage.max()

# 9. Identify the most popular occupation for those who earn >50K in India.
india_high_salary = df[(df['Native-Country'] == 'India') & (df['Salary'] == '>50K')]
if not india_high_salary.empty:
    most_popular_occupation_in_india = india_high_salary['occupation'].mode()[0]
else:
    most_popular_occupation_in_india = None

# Display results
print(f"Race count:\n{race_count}")
print(f"Average age of men: {average_age_men:.1f}")
print(f"Percentage with Bachelor's degree: {bachelors_percentage:.1f}%")
print(f"Percentage with advanced education earning >50K: {advanced_education_high_salary_percentage:.1f}%")
print(f"Percentage without advanced education earning >50K: {no_advanced_education_high_salary_percentage:.1f}%")
print(f"Minimum hours worked per week: {min_hours_per_week}")
print(f"Percentage of people who work the minimum hours and earn >50K: {min_hours_high_salary_percentage:.1f}%")
print(f"Country with highest percentage earning >50K: {country_highest_salary_percentage} ({highest_percentage:.1f}%)")
print(f"Most popular occupation in India for those earning >50K: {most_popular_occupation_in_india}")

