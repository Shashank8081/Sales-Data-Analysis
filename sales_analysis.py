# ==========================================
# SALES DATA ANALYSIS PROJECT
# Python | Pandas | Matplotlib | Seaborn
# ==========================================

# 1. Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display plots in notebook
plt.style.use('ggplot')


# ==========================================
# 2. Load Dataset
# ==========================================

# Load CSV file
data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\project\project\project\Sales Data Analysis\sales_data.csv")

print("First 5 Rows of Dataset")
print(data.head())


# ==========================================
# 3. Dataset Information
# ==========================================

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())


# ==========================================
# 4. Data Cleaning
# ==========================================

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove missing values
data.dropna(inplace=True)

# Remove duplicate records
data.drop_duplicates(inplace=True)

# Convert Order Date to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Create new columns for analysis
data['Year'] = data['Order Date'].dt.year
data['Month'] = data['Order Date'].dt.month
data['Month Name'] = data['Order Date'].dt.month_name()


# ==========================================
# 5. Basic Sales Metrics
# ==========================================

# Total Sales
total_sales = data['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Total Profit
total_profit = data['Profit'].sum()
print("Total Profit:", total_profit)

# Total Orders
total_orders = data['Order ID'].nunique()
print("Total Orders:", total_orders)


# ==========================================
# 6. Monthly Sales Analysis
# ==========================================

monthly_sales = data.groupby('Month Name')['Sales'].sum()

print("\nMonthly Sales")
print(monthly_sales)


# ==========================================
# 7. Region Wise Sales
# ==========================================

region_sales = data.groupby('Region')['Sales'].sum()

print("\nRegion Sales")
print(region_sales)


# ==========================================
# 8. Category Wise Sales
# ==========================================

category_sales = data.groupby('Category')['Sales'].sum()

print("\nCategory Sales")
print(category_sales)


# ==========================================
# 9. Top Selling Products
# ==========================================

top_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)

print("\nTop 10 Products")
print(top_products.head(10))


# ==========================================
# 10. Sales Trend Visualization
# ==========================================

plt.figure(figsize=(10,5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.show()


# ==========================================
# 11. Top 10 Products Chart
# ==========================================

plt.figure(figsize=(10,6))

top_products.head(10).plot(kind='bar')

plt.title("Top 10 Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=60)

plt.show()


# ==========================================
# 12. Region Wise Sales Chart
# ==========================================

plt.figure(figsize=(8,5))

region_sales.plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


# ==========================================
# 13. Category Sales Pie Chart
# ==========================================

plt.figure(figsize=(7,7))

category_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Sales Distribution by Category")

plt.ylabel("")

plt.show()


# ==========================================
# 14. Correlation Heatmap
# ==========================================

plt.figure(figsize=(8,6))

sns.heatmap(data[['Sales','Quantity','Profit']].corr(),
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Between Sales, Quantity and Profit")

plt.show()


# ==========================================
# 15. Save Cleaned Dataset
# ==========================================

data.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

# ==========================================
# END OF PROJECT
# ==========================================