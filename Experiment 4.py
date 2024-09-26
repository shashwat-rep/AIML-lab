#Experiment - 4 :  Write a python program to import and export data using Pandas and show the details of the dataset like number of rows, columns, first five rows, size, number of missing values, sum, average, min and max values from the numerical columns.

import pandas as pd
from google.colab import files  # Used for uploading files in Google Colab
import io  # To handle file I/O operations

# Upload the CSV file
uploaded = files.upload()

# Read the CSV file into a Pandas DataFrame
# The 'io.BytesIO' is used to convert the uploaded binary file into a readable stream
df = pd.read_csv(io.BytesIO(list(uploaded.values())[0]))

# Display the number of rows in the dataset
print("Number of rows:", df.shape[0])

# Display the number of columns in the dataset
print("Number of columns:", df.shape[1])

# Display the first five rows of the dataset
print("\nFirst five rows:")
print(df.head())

# Display the total size (number of elements) in the dataset
print("\nSize of the dataset:", df.size)

# Check and display the number of missing values in each column
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

# Select only the numerical columns from the dataset
numerical_columns = df.select_dtypes(include=['number'])

# Calculate and display summary statistics (sum, mean, min, max) for the numerical columns
print("\nSummary statistics for numerical columns:")
print(numerical_columns.agg(['sum', 'mean', 'min', 'max']))
