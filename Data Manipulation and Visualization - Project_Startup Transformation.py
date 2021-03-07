''' 
Question 1
The management team of the company you work for is concerned about the status of the company after a global pandemic.
The CFO (Chief Financial Officer) asks you to perform some data analysis on the past six months of the company’s financial data, which has been loaded in the variable financial_data.
First, examine the first few rows of the data using print() and .head().

Question 2
Notice that financial_data has three columns – Month, Revenue, and Expenses.
Store each column in three separate variables called month, revenue, and expenses.

Question 3
Create a plot of Revenue over the past 6 months

Question 4
Add labels and format the plot 

Question 5
Create the same plot for Expenses 
Use 'clf' to separate the plot Expenses from the plot Revenue

Question 6
As shown, revenue seems to be quickly decreasing while expenses are increasing. If the current trend continues, expenses will soon surpass revenues, putting the company at risk.
After you show this chart to the management team, they are alarmed. They conclude that expenses must be cut immediately and give you a new file to analyze called expenses.csv.
Use pandas to read in expenses.csv and store it in a variable called expense_overview.
Print the first seven rows of the data.

Question 7
Notice that there are two columns:
Expense: indicates the expense category
Proportion: indicates how much of the overall expenses a specific category takes up
Store the Expense column in a variable called expense_categories and the Proportion column in a variable called proportions.

Question 8
Next, we want to create a pie chart of the different expense categories. Use plt.clf() again to clear the previous plot, then create a pie chart using the plt.pie() method, passing in two arguments:
  proportions
  labels = expense_categories
Give your pie chart a title using plt.title(), then use plt.show() at the end to show the plot.

Question 9
Notice that the pie chart currently looks deformed.
Above plt.show(), add in the following two lines of code to set the axis and adjust the spacing:
  plt.axis('Equal')
  plt.tight_layout()
Take a moment to look at the pie chart. Which expense categories make up most of the data, and which ones aren’t so significant?

Question 10
It seems that Salaries, Advertising, and Office Rent make up most of the expenses, while the rest of the categories make up a small percentage.
Before you hand this pie chart back to management, you would like to update the pie chart so that all categories making up less than 5% of the overall expenses (Equipment, Utilities, Supplies, and Food) are collapsed into an “Other” category.
Update the pie chart accordingly.

Question 11
You should now see four categories in your updated pie chart:
  Salaries
  Advertising
  Office Rent
  Other
This simplified pie chart helps the management team see a big picture view of the company’s expenses without getting distracted by noisy data.
If the company wants to cut costs in a big way, which category do you think they should focus on? Put your answer in a string variable called expense_cut.

Question 12
Salaries make up 62% of expenses. The management team determines that to cut costs in a meaningful way, they must let go of some employees.
Each employee at the company is assigned a productivity score based on their work. The management would like to keep the most highly productive employees and let go of the least productive employees.
First, use pandas to load in employees.csv and store it in a variable called employees.
Print the first few rows of the data.

Question 13
Notice that there is a Productivity column, which indicates the productivity score assigned to that employee.
Sort the employees data frame (in ascending order) by the Productivity column and store the result in a variable called sorted_productivity.
To sort a data frame, you can do the following:
sorted_data = dataframe_name.sort_values(by=['Column Name'])
Print sorted_productivity.

Question 14
You should now see the employees with the lowest productivity scores at the top of the data frame.
The company decides to let go of the 100 least productive employees.
Store the first 100 rows of sorted_productivity in a new variable called employees_cut and print out the result.
Unfortunately, this batch of employees won’t be so lucky.

Question 15
Your colleague Sarah, a data scientist at the company, would like to explore the relationship between Income and Productivity more in depth, but she points out that these two features are on vastly different scales.
For example, productivity is a feature that ranges from 0-100, but income is measured in the thousands of dollars.
Moreover, there are outliers in the data that add an additional layer of complexity.
She asks you for advice on how she should transform the data. Should she perform normalization, standardization, log transformation, or something else?
Put your answer in a string in a variable called transformation.

Question 16
The COO (Chief Operating Officer) is debating whether to allow employees to continue to work from home post-pandemic.
He first wants to take a look at roughly how long the average commute time is for employees at the company. He asks for your help to analyze this data.
The employees data frame has a column called Commute Time that stores the commute time (in minutes) for each employee.
Create a variable called commute_times that stores the Commute Time column.

Question 17
Let’s do some quick analysis on the commute times of employees.
Use print() and .describe() to print out descriptive statistics for commute_times.
What are the average and median commute times? Might it be worth it for the company to explore allowing remote work indefinitely so employees can save time during the day?

Question 18
Let’s explore the shape of the commute time data using a histogram.
First, use plt.clf() to clear the previous plots. Then use plt.hist() to plot the histogram of commute_times. Finally, use plt.show() to show the plot. Feel free to add labels above plt.show() if you would like to practice!
What do you notice about the shape of the data? Is it symmetric, left skewed, or right skewed?

Question 19
The data seems to be skewed to the right. To make it more symmetrical, we might try applying a log transformation.
Right under the commute_times variable, create a variable called commute_times_log that stores a log-transformed version of commute_times.
To apply log-transform, you can use numpy’s log() function.

Question 20
Replace the histogram for commute_times with one for commute_times_log.
Notice how the shape of the data changes from being right skewed to a more symmetrical (and even slightly left-skewed) in shape. After applying log transformation, the transformed data is more “normal” than before.

'''

import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')
# code goes here
print(financial_data.head())

# Step 6 - moved for readability
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head()) #Move to top so table together

# Step 12 - moved for readability
employees = pd.read_csv('employees.csv')
#print(employees.head())

# Step 13 - moved for readability
sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity.head())
# Step 14 - moved for readability
employees_cut = sorted_productivity.head(100)

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

plt.clf()
''' #Replaced by Section 10 on line 94
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()
'''
# Clean up the smaller sections of the pie-chart
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()
# What do you think should get an expense cut? 
expense_cut = 'Salaries'

# How would you change the range on one scale to fit on another?
transformation = 'standardization'

# We need to calculate average commute time 
commute_times = employees['Commute Time']

# Step 19 - Convert to log
commute_times_log = np.log(commute_times)

#print(commute_times.describe())
'''
Commute Time Specifics
count    300.000000
mean      33.441700 #Average commute time 
std       16.128369
min        3.220000
25%       21.667500
50%       31.060000
75%       42.190000
max      101.780000
'''

#Appears right skewed
plt.clf()
#plt.hist(commute_times)
plt.hist(commute_times_log)
plt.xlabel('Total Commutes')
plt.ylabel('Total Commute Time')
plt.title('Commute Times')
plt.show()






