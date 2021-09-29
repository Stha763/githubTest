# importing all libraries here
import pandas as pd
# import qsharp as Q
import numpy as np

# importing dataset as csv file
df = pd.read_csv('TravelInsurancePrediction.csv', index_col=0)


# df.info() to know about dataframe

# Dealing with missing values
rows, columns = df.shape
cell_count = rows * columns
number_of_nulls = df.isnull().sum()
missing_percentage = (number_of_nulls / cell_count) * 100
# print(f'Percentage of missing values: {missing_percentage}%')

# rename column
df = df.rename({"Employment Type": "EmploymentType"}, axis=1)

# Splitting categorical variable
# df[['Sector', 'EmploymentType']] = df.EmploymentType.str.split(expand=True, )
# print(df['EmploymentType'].values)

df[['Sector', 'EmploymentType']] = df.EmploymentType.str.split("/", expand=True, )

# print(df.columns)

# drop unnamed column
# setup index
# df.set_index(['Age', 'Sector', 'EmploymentType', 'GraduateOrNot', 'AnnualIncome', 'FamilyMembers'])
inserted_cols = ['Age', 'Sector', 'EmploymentType', 'GraduateOrNot', 'AnnualIncome', 'FamilyMembers']
cols = ([col for col in inserted_cols if col in df]
        + [col for col in df if col not in inserted_cols])
df = df[cols]

# print(df.head())

df.info()
print(len(df))
