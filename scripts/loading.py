import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

# Database connection settings
DB_NAME = "ecommerce_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

# Load cleaned dataset
cleaned_data_path = "data/ecommerce_data_cleaned.csv"
df = pd.read_csv(cleaned_data_path)

# Create a connection to PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Define table schema and create tables
create_table_query = text("""
CREATE TABLE IF NOT EXISTS transactions (
    event_time TIMESTAMP,
    order_id BIGINT,
    product_id BIGINT,
    category_id BIGINT,
    category_code TEXT,
    brand TEXT,
    price FLOAT,
    user_id BIGINT
);
""")

# Execute table creation
with engine.connect() as conn:
    conn.execute(create_table_query)
    conn.commit()

# Load data into the PostgreSQL table
df.to_sql('transactions', engine, if_exists='append', index=False)

print("Data successfully loaded into PostgreSQL!")
