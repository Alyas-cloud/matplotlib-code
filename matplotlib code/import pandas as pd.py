import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data in a dictionary for the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [30500, 35600, 28300, 33900, 41400],
    'Expenses': [22000, 23400, 21000, 23500, 27000],
    'Profit': [8500, 12200, 7300, 10400, 14400]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# 1. Line plot: Sales and Expenses over months
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Sales'], label='Sales', marker='o', color='b')
plt.plot(df['Month'], df['Expenses'], label='Expenses', marker='o', color='r')
plt.title('Sales vs Expenses Over Months')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar chart: Sales and Expenses
df.plot(kind='bar', x='Month', y=['Sales', 'Expenses'], figsize=(8, 5), color=['blue', 'red'])
plt.title('Monthly Sales and Expenses')
plt.ylabel('Amount ($)')
plt.show()

# 3. Scatter plot: Sales vs Profit
plt.figure(figsize=(8, 5))
plt.scatter(df['Sales'], df['Profit'], color='green')
plt.title('Sales vs Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.show()

# 4. Histogram: Distribution of Sales
plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=5, color='purple', edgecolor='black', alpha=0.7)
plt.title('Sales Distribution')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.show()

# 5. Subplots with Pandas
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top left: Line plot (Sales)
df.plot(kind='line', x='Month', y='Sales', ax=axs[0, 0], color='b', marker='o', title='Sales')

# Top right: Line plot (Expenses)
df.plot(kind='line', x='Month', y='Expenses', ax=axs[0, 1], color='r', marker='o', title='Expenses')

# Bottom left: Bar chart (Profit)
df.plot(kind='bar', x='Month', y='Profit', ax=axs[1, 0], color='g', title='Profit')

# Bottom right: Scatter plot (Sales vs Profit)
axs[1, 1].scatter(df['Sales'], df['Profit'], color='purple')
axs[1, 1].set_title('Sales vs Profit')
axs[1, 1].set_xlabel('Sales')
axs[1, 1].set_ylabel('Profit')

plt.tight_layout()
plt.show()
