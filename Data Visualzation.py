# Visualize monthly transaction amounts over a year.

import pandas as pd
import matplotlib.pyplot as plt
# Sample data: Monthly transaction amounts in a bank
data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Transaction Amount': [20000, 25000, 22000, 27000, 28000,
30000, 31000, 35000, 33000, 36000, 34000, 37000]}
df = pd.DataFrame(data)
 # Plotting
plt.plot(df['Month'],df['Transaction Amount'],
linestyle='-', color='b')
plt.title('Monthly Transaction Amounts')
plt.xlabel('Month')
plt.ylabel('Transaction Amount ($)')
plt.grid(True)
plt.show()

data = {'Account Type': ['Savings', 'Checking', 'Credit', 'Loan'],
 'Number of Accounts': [15000, 10000, 5000, 3000]}
df = pd.DataFrame(data)
 # Plotting
plt.bar(df['Account Type'], df['Number of Accounts'], color='teal')
plt.title('Number of Accounts by Account Type')
plt.xlabel('Account Type')
plt.ylabel('Number of Accounts')
plt.grid(True)
plt.show()
 

import numpy as np
 # Simulate some transaction amount data
transaction_amounts = np.random.normal(1000, 200, 1000)
#1000 transactions with a mean of $1000
 # Plotting
plt.hist(transaction_amounts,
edgecolor='black')
bins=20,
plt.title('Distribution of Daily Transaction Amounts')
plt.xlabel('Transaction Amount ($)')
plt.ylabel('Frequency')
plt.show()

import seaborn as sns
data = {'Account Type': ['Savings', 'Savings', 'Checking', 'Checking',
'Credit', 'Credit', 'Loan', 'Loan'],
'Transaction Amount': [2000, 3000, 1500, 1600, 7000, 7200,
50000, 50500]}
df = pd.DataFrame(data)
  # Plotting
sns.boxplot(x='Account Type', y='Transaction Amount', data=df)
plt.title('Transaction Amount by Account Type')
plt.show()


# Sample correlation data
data = {'ATM Transactions': [50, 30, 20], 'Online Payments': [30, 20,
15], 'In-branch Transactions': [20, 15, 10]}
df = pd.DataFrame(data, index=['Savings', 'Checking', 'Credit'])
 # Plotting
sns.heatmap(df, annot=True, cmap='YlGnBu')
plt.title('Transaction Type Distribution by Account Type')
plt.xlabel('Transaction Type')
plt.ylabel('Account Type')
plt.show()

 # Customizing the Monthly Transaction Amounts line plot
plt.plot(df['Month'],df['Transaction Amount'], marker='o',
 linestyle='-', color='green', label='Transaction Amount')
plt.title('Monthly Transaction Amounts')
plt.xlabel('Month')
plt.ylabel('Transaction Amount ($)')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

 # Sample data: New customers added each year
data = {'Year': [2018, 2019, 2020, 2021, 2022],
'New Customers': [2000, 2500, 2800, 3000, 3500]}
df = pd.DataFrame(data)
 # Plotting
plt.plot(df['Year'], df['New Customers'], marker='o', linestyle='-',
color='blue')
plt.title('New Customer Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Number of New Customers')
plt.grid(True)
plt.show()


# Sample data: Revenue contribution by region
data = {'Region': ['North', 'South', 'East', 'West'],
'Revenue': [50000, 70000, 60000, 80000]}
df = pd.DataFrame(data)
# Plotting
plt.pie(df['Revenue'],
startangle=140)
labels=df['Region'],
plt.title('Revenue Contribution by Region')
plt.show()