#Experiment - 4 :  Write a python program to import and export data using Pandas and show the details of the dataset like number of rows, columns, first five rows, size, number of missing values, sum, average, min and max values from the numerical columns.

import pandas as pd
from google.colab import files  # Used for uploading files in Google Colab
import io  # To handle file I/O operations

# Upload the CSV file
uploaded = files.upload()

# Read the CSV file into a Pandas DataFrame
# The 'io.BytesIO' is used to convert the uploaded binary file into a readable stream
df = pd.read_csv(io.BytesIO(upload['sample.csv']))

# Display the number of rows in the dataset
df.shape[0]

# Display the number of columns in the dataset
df.shape[1]

# Display the first five rows of the dataset
df.head(5)

# Display the total size (number of elements) in the dataset
df.size

# Check and display the number of missing values in each column
df.isnull().sum()

# Select only the numerical columns from the dataset
numerical_columns = df.select_dtypes(include=['number'])

# Calculate and display summary statistics (sum, mean, min, max) for the numerical columns
numerical_columns.agg(['sum', 'mean', 'min', 'max'])
