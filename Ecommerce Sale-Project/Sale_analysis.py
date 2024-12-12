import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

# Load the dataset

sale=pd.read_csv('ecommerce_dataset_updated.csv')

# 1. Category Analysis: Bar chart of product categories

plt.figure(figsize=(10, 6))
category_counts = sale['Category'].value_counts()
sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
plt.title('Product Categories by Sales Count')
plt.xlabel('Category')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.show()

# 2. Distribution of Product Prices

plt.figure(figsize=(10, 6))
sns.histplot(sale['Price (Rs.)'], kde=True, color='blue', bins=30)
plt.title('Distribution of Product Prices')
plt.xlabel('Price (Rs.)')
plt.ylabel('Frequency')
plt.show()

# 3. Comparison of Original Prices vs. Final Prices

plt.figure(figsize=(10, 6))
sns.scatterplot(x=sale['Price (Rs.)'], y=sale['Final_Price(Rs.)'], hue=sale['Category'], palette='tab10')
plt.title('Original Price vs Final Price by Category')
plt.xlabel('Original Price (Rs.)')
plt.ylabel('Final Price (Rs.)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# 4. Payment Method Preferences

plt.figure(figsize=(10, 6))
payment_counts = sale['Payment_Method'].value_counts()
sns.barplot(x=payment_counts.index, y=payment_counts.values, palette='coolwarm')
plt.title('Distribution of Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.show()
