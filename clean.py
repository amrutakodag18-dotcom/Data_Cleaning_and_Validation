import pandas as pd

# 1. Load the dataset
# (Ensure your CSV file is in the same folder and named 'raw_dataset.csv')
file_name = 'raw_dataset.csv'
df = pd.read_csv(file_name)

print('--- 1. Original Dataset Preview ---')
print(df.head())
print(f'Original row count: {len(df)}')

# 2. Check for missing values and duplicates before cleaning
print('\n--- 2. Initial Quality Check ---')
print('Missing values per column:')
print(df.isnull().sum())
print(f'Duplicate rows count: {df.duplicated().sum()}')

# 3. Clean the data
# A. Remove duplicate rows
df = df.drop_duplicates()

# B. Standardize column headers (lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# C. Handle missing values (Example: Fill numeric missing values with median, text with 'Unknown')
for col in df.columns:
  if df[col].dtype in ['float64', 'int64']:
    df[col] = df[col].fillna(df[col].median())
  else:
    df[col] = df[col].fillna('Unknown')

# 4. Verify after cleaning
print('\n--- 4. Post-Cleaning Check ---')
print('Missing values after cleaning:')
print(df.isnull().sum())
print(f'Cleaned row count: {len(df)}')

# 5. Export the cleaned dataset to a new CSV file
output_file = 'cleaned_dataset.csv'
df.to_csv(output_file, index=False)
print(f'\nSuccess! Cleaned dataset saved as "{output_file}" in your folder.')