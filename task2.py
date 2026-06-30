import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = r"C:\Users\Aniket\Downloads\gender_submission.csv"
try:
    df = pd.read_csv(file_name)
    print(f"Successfully loaded {file_name}")
except FileNotFoundError:
    print(f"Error: {file_name} not found. Please ensure the path is correct.")
    exit()

print("\n--- Initial Data Overview ---")
print("Dataset Shape (Rows, Columns):", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values before cleaning:\n", df.isnull().sum())
print("\nFirst 5 rows:\n", df.head())

print("\n--- Starting Data Cleaning ---")

initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"Removed {initial_rows - df.shape[0]} duplicate rows.")

for col in df.columns:
    missing_count = df[col].isnull().sum()
    if missing_count > 0:
        if df[col].dtype in ['int64', 'float64']:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"Filled {missing_count} missing values in numeric column '{col}' with median: {median_val}")
        else:
            df[col] = df[col].fillna('Unknown')
            print(f"Filled {missing_count} missing values in categorical column '{col}' with 'Unknown'")

print("\nMissing values after cleaning:\n", df.isnull().sum())

print("\n--- Exploratory Data Analysis ---")
print("\nStatistical Summary of Numeric Columns:\n", df.describe())

if 'Survived' in df.columns:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Survived', palette='Set2')
    plt.title(f'Distribution of Survival in {file_name.split("\\")[-1]}')
    plt.xlabel('Survived (0 = No, 1 = Yes)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
elif 'Sales' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Sales'], bins=30, kde=True, color='blue')
    plt.title(f'Distribution of Sales in {file_name.split("\\")[-1]}')
    plt.xlabel('Sales Amount')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
else:
    print("\nNote: Specific target columns ('Survived' or 'Sales') were not found for automated plotting.")
    print("To plot a specific column, add code like: sns.histplot(df['Your_Column_Name'])")