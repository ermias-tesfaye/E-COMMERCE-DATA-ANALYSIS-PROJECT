import pandas as pd

# Load the dataset into a pandas DataFrame
file_path = 'data/ecommerce_data.csv'  # Path to the dataset
df = pd.read_csv(file_path)

# Inspect the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check the shape of the dataset (rows, columns)
print(f"\nDataset shape: {df.shape}")

# Get basic information about the dataset (columns, data types, non-null counts)
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for duplicates
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Describe numerical columns (summary statistics)
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Save the output to a text file for reference
with open('data/dataset_analysis.txt', 'w') as f:
    f.write("First 5 rows of the dataset:\n")
    f.write(str(df.head()) + "\n\n")
    f.write(f"Dataset shape: {df.shape}\n\n")
    f.write("Dataset info:\n")
    df.info(buf=f)
    f.write("\n\nMissing values in each column:\n")
    f.write(str(df.isnull().sum()) + "\n\n")
    f.write("Number of duplicate rows:\n")
    f.write(str(df.duplicated().sum()) + "\n\n")
    f.write("Summary statistics for numerical columns:\n")
    f.write(str(df.describe()) + "\n")