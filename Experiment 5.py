# Experiment - 5 : Using Python language do the exploratory data analysis of dataset imported in the lab 4.

import pandas as pd  # Importing pandas library for data manipulation and analysis
from google.colab import files  # Used for uploading files in Google Colab

# Upload the CSV file
upload = files.upload()

import io  # Used for input/output operations
# Load the uploaded CSV file into a pandas DataFrame
df = pd.read_csv(io.BytesIO(upload['sample.csv']))

# Display the first 5 rows of the DataFrame to inspect the data
df.head(5)

# Display the last 5 rows of the DataFrame to inspect the tail end of the data
df.tail(5)

# Display general information about the DataFrame, including column names, data types, and memory usage
df.info()

# Display summary statistics for numerical columns (count, mean, std, min, 25%, 50%, 75%, max)
df.describe()

# Check for missing values in each column, showing the count of NaN values
df.isnull().sum()

# Loop through all categorical columns (data type 'object') and print the unique values in each column
for col in df.select_dtypes(include=['object']):
    print(f"\nUnique values in '{col}': {df[col].unique()}")

# Plot histograms for each numerical column to visualize distributions
df.hist(figsize=(15, 10))

# Plot boxplots for numerical columns to detect outliers and see the spread of the data
df.boxplot(figsize=(15, 10))
