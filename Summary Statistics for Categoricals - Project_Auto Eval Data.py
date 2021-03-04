'''
Question 1
manufacturer_country is a nominal categorical variable that indicates the country of the manufacturer of each car reviewed. Create a table of frequencies of all the cars reviewed by manufacturer_country. What is the modal category? Which country appears 4th most frequently? Print out your results.

Question 2
Calculate a table of proportions for countries that appear in manufacturer_country in the dataset. What percentage of cars were manufactured in Japan?

Question 3
buying_cost is a categorical variable which describes the cost of buying any car in the dataset. Print out a list of the possible values for this variable.

Question 4
buying_cost is an ordinal categorical variable, which means we can create an order associated with the values in the data and perform additional numeric operations on the variable. Create a new list, buying_cost_categories, that contains the unique values in buying_cost, ordered from lowest to highest.

Question 5
Convert buying_cost to type 'category' using the list you created in the previous exercise.

Question 6
Calculate the median category of the buying_cost variable and print the result.

Question 7
luggage is a categorical variable in the car evaluations dataset that records the luggage capacity for each reviewed car. Calculate a table of proportions for this variable and print the result.

Question 8
Are there any missing values in this column? Replicate the table of proportions from the previous exercise, but do not drop any missing values from the count. Print your result.

Question 9 
Without passing normalize = True to .value_counts(), can you replicate the result you got in the previous exercises?

Question 10
doors is a categorical variable in the car evaluations dataset that records the count of doors for each reviewed car. Find the count of cars that have 5 or more doors. You can identify cars with 5+ doors by looking for cars that have a value of '5more' in the doors column. Print your result.

Question 11
Find the proportion of cars that have 5+ doors and print the result.

'''

import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

# Get the number of manufacturing countries
manufacturer_country_counts = car_eval['manufacturer_country'].value_counts()
# Get the country with that manufacturers the most
highest_manufacturer_country = manufacturer_country_counts.index[0]

#print(manufacturer_country_counts) 
#print(highest_manufacturer_country) #Japan

# Get the calculated table for manufacturer countries
manufacturer_country_proportions = car_eval['manufacturer_country'].value_counts()/len(car_eval['manufacturer_country'])
#print(manufacturer_country_proportions) #0.228 or 22.8% were manufactured in Japan

# Find the unique values for buying cost 
#print(car_eval['buying_cost'].unique()) #['vhigh', 'med', 'low', 'high']

# Identify the correct order for buying cost categories 
buying_cost_categories = ['low', 'med', 'high', 'vhigh']
# Convert the buying cost column to the new categorical order
car_eval['buying_cost'] = pd.Categorical(
  car_eval['buying_cost'], buying_cost_categories, ordered=True
) 
#print(car_eval.buying_cost)

# Identify the median of buying cost (needs to be converted to int) (import numpy)

median_buying_index = np.median(car_eval['buying_cost'].cat.codes)
#rint(median_buying_index) #1.0
median_buying_cost = buying_cost_categories[int(median_buying_index)]
#print(median_buying_cost) #med

# Get the calculated table for the luggage
luggage_proportions = car_eval['luggage'].value_counts(normalize=True)
#print(luggage_proportions) #small = 0.339, med = 0.333, big = 0.328

# Are there any nan for the calculated table?
luggage_proportions1 = car_eval['luggage'].value_counts(dropna=False, normalize=True)
#print(luggage_proportions1) #small = 0.399, med = 0.333, big = 0.328

# What effect does removing 'normalize=True' have on the luggage proportions
luggage_proportions2 = car_eval['luggage'].value_counts()
#print(luggage_proportions2) #looks like the same effects

# What are the unique values in the doors column?
#print(car_eval['doors'].unique()) #2,3,4, 5more

# Find the total number of rows that have '5more'
list_of_doors = car_eval['doors'].value_counts()
#print(list_of_doors) #5more has 246 entries

# Find the proportion of cars that have '5more' doors
list_of_doors_proportions = car_eval['doors'].value_counts()/len(car_eval['doors'])
print(list_of_doors_proportions) #5more has 0.246 or 24.6% 














