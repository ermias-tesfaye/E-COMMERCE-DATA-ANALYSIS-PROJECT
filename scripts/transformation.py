import pandas as pd

# Load the dataset
data_path = "data/ecommerce_data.csv"
df = pd.read_csv(data_path)

print("Rows before cleaning:", len(df))

# Convert event_time to datetime
df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print("Rows after removing duplicates:", len(df))

# Handle missing values
## Drop rows where price is missing (since it's a critical value)
df = df.dropna(subset=['price'])
print("Rows after dropping missing price:", len(df))

## Fill missing category_code and brand using direct assignment
df = df.assign(
    category_code=df['category_code'].fillna('unknown'),
    brand=df['brand'].fillna('unknown')
)

# Convert IDs to integers (if possible)
df['order_id'] = df['order_id'].astype('int64')
df['product_id'] = df['product_id'].astype('int64')
df['category_id'] = df['category_id'].fillna(0).astype('int64')  # Fill NaN with 0

# Handle outliers in price
## Remove rows with price = 0 or extreme values (e.g., price > 10,000)
df = df[(df['price'] > 0) & (df['price'] <= 10000)]
print("Rows after handling outliers:", len(df))

# Save the cleaned dataset
cleaned_data_path = "data/ecommerce_data_cleaned.csv"
df.to_csv(cleaned_data_path, index=False)

print("Data cleaning complete! Cleaned dataset saved at:", cleaned_data_path)