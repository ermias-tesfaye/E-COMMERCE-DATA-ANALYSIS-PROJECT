# E-Commerce Data Analysis Project

## Overview
This project focuses on analyzing an e-commerce transactions dataset containing over 2 million rows. The dataset includes fields such as `event_time`, `order_id`, `product_id`, `category_code`, `brand`, `price`, and `user_id`. The goal is to build an end-to-end ETL (Extract, Transform, Load) pipeline to process and analyze the data, derive meaningful insights, and visualize key metrics using Microsoft Power BI.

---

## Objectives
1. **Data Extraction**: Load the dataset from a CSV file and perform initial exploration.
2. **Data Transformation**: Clean and preprocess the data to ensure consistency and usability.
3. **Data Storage**: Store the cleaned data in a PostgreSQL database for efficient querying.
4. **Data Visualization**: Create interactive dashboards in Power BI to visualize key insights.
5. **Insights and Recommendations**: Derive actionable insights to optimize e-commerce strategies.

---

## Please Unzip the data folder to access the csv data/dataset

## Tech Stack
The following tools, technologies, and frameworks were used in this project:

### **Data Extraction and Transformation**
- **Python**: Primary programming language for data processing.
- **Pandas**: Library for data manipulation and analysis.

### **Data Storage**
- **PostgreSQL**: Relational database for storing cleaned data.
- **SQLAlchemy**: Python library for connecting to and interacting with PostgreSQL.

### **Data Visualization**
- **Microsoft Power BI**: Tool for creating interactive dashboards and visualizations.

### **Version Control**
- **Git**: Version control system for tracking changes in the codebase.
- **GitHub**: Platform for hosting and sharing the project repository.

### **Development Environment**
- **VS Code**: Code editor for writing and debugging Python scripts.

## Dataset
The dataset contains the following columns:

| Column Name     | Data Type | Description                          |
|-----------------|-----------|--------------------------------------|
| `event_time`    | TIMESTAMP | Timestamp of the transaction.        |
| `order_id`      | BIGINT    | Unique identifier for the order.     |
| `product_id`    | BIGINT    | Unique identifier for the product.   |
| `category_id`   | BIGINT    | Unique identifier for the category.  |
| `category_code` | TEXT      | Product category (e.g., electronics).|
| `brand`         | TEXT      | Brand of the product.                |
| `price`         | FLOAT     | Price of the product.                |
| `user_id`       | BIGINT    | Unique identifier for the customer.  |

---

## Data Cleaning Steps
The dataset underwent the following transformations to ensure data quality:

1. **Handling Missing Values**:
   - Rows with missing `price` were dropped.
   - Missing `category_code` and `brand` values were filled with "unknown".

2. **Removing Duplicates**:
   - Duplicate rows were identified and removed.

3. **Data Type Formatting**:
   - `event_time` was converted to datetime format.
   - IDs (`order_id`, `product_id`, `category_id`) were converted to integers.

4. **Handling Outliers**:
   - Rows with unrealistic prices (e.g., `price = 0` or `price > 10,000`) were removed.

5. **Feature Engineering**:
   - A new column, `HourOfDay`, was created for time-based analysis.

---

## Database Schema
The cleaned data was stored in a PostgreSQL database with the following schema:

# E-Commerce Data Analysis Project

## Overview
This project focuses on analyzing an e-commerce transactions dataset containing over 2 million rows. The dataset includes fields such as `event_time`, `order_id`, `product_id`, `category_code`, `brand`, `price`, and `user_id`. The goal is to build an end-to-end ETL (Extract, Transform, Load) pipeline to process and analyze the data, derive meaningful insights, and visualize key metrics using Microsoft Power BI.

---

## Objectives
1. **Data Extraction**: Load the dataset from a CSV file and perform initial exploration.
2. **Data Transformation**: Clean and preprocess the data to ensure consistency and usability.
3. **Data Storage**: Store the cleaned data in a PostgreSQL database for efficient querying.
4. **Data Visualization**: Create interactive dashboards in Power BI to visualize key insights.
5. **Insights and Recommendations**: Derive actionable insights to optimize e-commerce strategies.

---

## Dataset
The dataset contains the following columns:

| Column Name     | Data Type | Description                          |
|-----------------|-----------|--------------------------------------|
| `event_time`    | TIMESTAMP | Timestamp of the transaction.        |
| `order_id`      | BIGINT    | Unique identifier for the order.     |
| `product_id`    | BIGINT    | Unique identifier for the product.   |
| `category_id`   | BIGINT    | Unique identifier for the category.  |
| `category_code` | TEXT      | Product category (e.g., electronics).|
| `brand`         | TEXT      | Brand of the product.                |
| `price`         | FLOAT     | Price of the product.                |
| `user_id`       | BIGINT    | Unique identifier for the customer.  |

---

## Data Cleaning Steps
The dataset underwent the following transformations to ensure data quality:

1. **Handling Missing Values**:
   - Rows with missing `price` were dropped.
   - Missing `category_code` and `brand` values were filled with "unknown".

2. **Removing Duplicates**:
   - Duplicate rows were identified and removed.

3. **Data Type Formatting**:
   - `event_time` was converted to datetime format.
   - IDs (`order_id`, `product_id`, `category_id`) were converted to integers.

4. **Handling Outliers**:
   - Rows with unrealistic prices (e.g., `price = 0` or `price > 10,000`) were removed.

5. **Feature Engineering**:
   - A new column, `HourOfDay`, was created for time-based analysis.

---

## Database Schema
The cleaned data was stored in a PostgreSQL database with the following schema:

```sql
CREATE TABLE transactions (
    event_time TIMESTAMP,
    order_id BIGINT,
    product_id BIGINT,
    category_id BIGINT,
    category_code TEXT,
    brand TEXT,
    price FLOAT,
    user_id BIGINT
);